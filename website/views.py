from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import  login_required, current_user
from .models import Recipe
from . import db
import json

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
        new_recipe = Recipe( title=new_title, link=new_url, comment=new_comment, user_id=current_user.id)
        recipe = Recipe.query.filter_by(link=new_url).first()
        if recipe:
            flash('Recipe already exists!', category='error')
        else:
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added!', category='success')

    return render_template("create.html", user=current_user)


@views.route('/delete-recipe', methods=['POST'])
def delete_recipe():
    recipe = json.loads(request.data)
    recipeId = recipe['recipeId']
    recipe = Recipe.query.get(recipeId)
    if recipe:
        if recipe.user_id == current_user.id:
            db.session.delete(recipe)
            db.session.commit()
    return jsonify({})


@views.route('/update-route', methods=['Get','POST'])
@login_required
def update_route():
    recipe = json.loads(request.data)
    recipeID = recipe['recipeId']
    recipe = Recipe.query.get(recipeID) 
    return jsonify({})
