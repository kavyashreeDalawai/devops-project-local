import click
from flask.cli import with_appcontext
from service import db

@click.command('db-create')
@with_appcontext
def db_create():
    """Creates the database tables"""
    db.create_all()
    print("Database tables created successfully.")
