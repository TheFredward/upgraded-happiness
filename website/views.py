from flask import Blueprint, render_template, request
import psycopg2 as psy 

views = Blueprint('views', __name__,
        template_folder='templates')

@views.route('/')
def home():
    return render_template("about.html")

@views.route('/recipes')
def recipes():
    return render_template("recipes.html")

@views.route('/create')
def create():
    return render_template("create.html")
