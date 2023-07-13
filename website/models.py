from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ ='user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(100))
    recipes = db.relationship('Recipe')


class Recipe(db.Model):
    # Create the model needed for interacting with recipe_database
    # Link the user and recipe input by using foreign key to data being added
    __tablename__='recipe'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    link = db.Column(db.String(250))
    comment = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
