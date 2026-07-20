import unittest
from service import create_app, db
from service.models import Account, DataValidationError


class TestAccountModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_an_account(self):
        account = Account(name="John Doe", email="john@doe.com", address="123 Lane")
        db.session.add(account)
        db.session.commit()
        self.assertEqual(account.id, 1)

    def test_deserialize_missing_keys(self):
        """It should raise DataValidationError when missing required keys"""
        account = Account()
        bad_data = {"name": "John Doe"}
        with self.assertRaises(DataValidationError):
            account.deserialize(bad_data)

    def test_deserialize_bad_data_type(self):
        """It should raise DataValidationError when data type is invalid"""
        account = Account()
        bad_data = "This is a plain string, not a dictionary structure"
        with self.assertRaises(DataValidationError):
            account.deserialize(bad_data)
