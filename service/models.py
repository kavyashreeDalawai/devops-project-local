import logging
from datetime import date
from service import db

logger = logging.getLogger("flask.app")

class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""
    pass

class Account(db.Model):
    """Class that represents an Account"""
    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=True)
    phone_number = db.Column(db.String(32), nullable=True)
    date_joined = db.Column(db.Date, nullable=False, default=date.today)

    def serialize(self):
        """Serializes an Account into a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
            "date_joined": self.date_joined.isoformat() if isinstance(self.date_joined, date) else self.date_joined
        }

    def deserialize(self, data):
        """Deserializes an Account from a dictionary"""
        try:
            self.name = data["name"]
            self.email = data["email"]
            self.address = data.get("address")
            self.phone_number = data.get("phone_number")
            if "date_joined" in data:
                self.date_joined = date.fromisoformat(data["date_joined"])
        except KeyError as error:
            raise DataValidationError(f"Invalid Account: missing {error.args[0]}")
        except TypeError as error:
            raise DataValidationError(f"Invalid Account: body of request contained bad data - {error}")
        return self
