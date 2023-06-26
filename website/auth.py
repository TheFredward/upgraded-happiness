from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from re import fullmatch

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        return render_template("login.html")
         
    else:
        return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Logout logic coming soon</h1>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        data = request.form
        email = data.get('email')
        first_name = data.get('firstName')
        password = data.get('password')
        verify_password = data.get('verify_password')

        if fullmatch(regex, email) == 'None':
            flash('Invalid e-mail address', 'error')
        elif len(first_name) < 2:
            flash('Invalid name', 'error')
        elif password != verify_password:
            flash('Passwords do not match', 'error')
        return render_template("sign_up.html")
    else:
        return render_template("sign_up.html")


