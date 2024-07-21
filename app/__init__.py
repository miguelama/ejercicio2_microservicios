from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carts.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
