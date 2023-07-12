from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from .models import Recipe
from . import db

views = Blueprint('views', __name__,
        template_folder='templates')

@views.route('/')
def home():
    return render_template("about.html", user=current_user)

@views.route('/recipes')
def recipes():
    return render_template("recipes.html", user=current_user)

@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        data = request.form
        new_title = data.get('title')
        new_url = data.get('url')
        new_comment = data.get('comments')
        new_recipe = Recipe( title=new_title, link=new_url, comment=new_comment)
    return render_template("create.html", user=current_user)
