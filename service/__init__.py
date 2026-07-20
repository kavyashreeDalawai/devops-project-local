import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_cors import CORS

db = SQLAlchemy()

# Move the models import out of the factory block so it runs globally on initialization
from service import models

def create_app():
    """Initializes and builds the core Flask microservice application"""
    app = Flask(__name__)
    
    database_uri = os.getenv("DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "secret-project-key"
    
    db.init_app(app)
    
    with app.app_context():
        from service.routes import init_routes
        from service.common.cli_commands import db_create
        
        init_routes(app)
        app.cli.add_command(db_create)
    
    # Security Configuration
    Talisman(app, force_https=False)
    CORS(app)
        
    return app
