from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'pass'
    app.config['SQLALCHEMY_DATABASE_URI']= f'postgres+psycopg2://postgres:password@localhost:5432/recipes'
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
