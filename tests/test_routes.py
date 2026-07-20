import unittest
from service import create_app, db
from service.models import Account

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_health(self):
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)

    def test_create_account(self):
        new_account = {"name": "John Doe", "email": "john@doe.com", "address": "123 Lane"}
        resp = self.client.post("/accounts", json=new_account)
        self.assertEqual(resp.status_code, 201)

    def test_get_account_list(self):
        """It should retrieve a list of all accounts"""
        resp = self.client.get("/accounts")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.get_json()), 0)

    def test_read_and_update_and_delete_account(self):
        """It should successfully cycle through Read, Update, and Delete actions"""
        # 1. Seed data record
        new_account = {"name": "Alice Smith", "email": "[email protected]", "address": "456 Side St"}
        post_resp = self.client.post("/accounts", json=new_account)
        account_id = post_resp.get_json()["id"]

        # 2. Test READ (GET)
        get_resp = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.get_json()["name"], "Alice Smith")

        # 3. Test UPDATE (PUT)
        updated_data = {"name": "Alice Jones", "email": "[email protected]", "address": "789 New St"}
        put_resp = self.client.put(f"/accounts/{account_id}", json=updated_data)
        self.assertEqual(put_resp.status_code, 200)
        self.assertEqual(put_resp.get_json()["name"], "Alice Jones")

        # 4. Test DELETE
        del_resp = self.client.delete(f"/accounts/{account_id}")
        self.assertEqual(del_resp.status_code, 204)

        # 5. Verify 404 block handler
        missing_resp = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(missing_resp.status_code, 404)
        
        missing_put = self.client.put(f"/accounts/{account_id}", json=updated_data)
        self.assertEqual(missing_put.status_code, 404)
