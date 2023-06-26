from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from config import db_user, db_pass,KEY
import psycopg2

# Initialize alchemy and define the database
db = SQLAlchemy()
DB_NAME = "webdatabase"

def create_app():
    # Import the views and set up the pages with blueprint
    # Set up the location of postgresql database
    app = Flask(__name__)
    app.config['SECRET_KEY'] = KEY 
    app.config['SQLALCHEMY_DATABASE_URI']= f'postgresql+psycopg2://{db_user}:{db_pass}@localhost:5432/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Recipe
    create_database(app)
    return app


def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created database')
        else:
            print('Already Created')
