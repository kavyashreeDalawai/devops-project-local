from flask import jsonify, request, abort
from service import db
from service.models import Account


def init_routes(app):
    """Registers all REST API endpoints with the Flask application instance"""

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="OK"), 200

    @app.route("/accounts", methods=["POST"])
    def create_accounts():
        data = request.get_json()
        account = Account()
        account.deserialize(data)
        db.session.add(account)
        db.session.commit()
        return jsonify(account.serialize()), 201

    @app.route("/accounts/<int:account_id>", methods=["GET"])
    def get_accounts(account_id):
        account = Account.query.get(account_id)
        if not account:
            abort(404, f"Account with id [{account_id}] could not be found.")
        return jsonify(account.serialize()), 200

    @app.route("/accounts/<int:account_id>", methods=["PUT"])
    def update_accounts(account_id):
        account = Account.query.get(account_id)
        if not account:
            abort(404, f"Account with id [{account_id}] could not be found.")
        data = request.get_json()
        account.deserialize(data)
        db.session.commit()
        return jsonify(account.serialize()), 200

    @app.route("/accounts/<int:account_id>", methods=["DELETE"])
    def delete_accounts(account_id):
        account = Account.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
        return "", 204

    @app.route("/accounts", methods=["GET"])
    def list_accounts():
        accounts = Account.query.all()
        results = [account.serialize() for account in accounts]
        return jsonify(results), 200
