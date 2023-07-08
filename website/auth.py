from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from re import fullmatch


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", boolean=True)

@auth.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        data = request.form
        new_email = data.get('email')
        new_first_name = data.get('firstName')
        new_password = data.get('password')
        verify_password = data.get('verify_password')

        user = User.query.filter_by(email=new_email).first()
        if fullmatch(regex, new_email) == 'None':
            flash('Invalid e-mail address', 'error')
        elif user:
            flash('Email already exists', category='error')
        elif len(new_first_name) < 2:
            flash('Invalid name', 'error')
        elif new_password != verify_password:
            flash('Passwords do not match', 'error')
        else:
            new_user = User(email=new_email, password=generate_password_hash(new_password, method='sha256'), first_name=new_first_name)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

