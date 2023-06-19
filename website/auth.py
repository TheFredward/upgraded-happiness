from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        print(data)
        print(data.get('email'))
        print(data.get('password'))
        return "<p> Working on it</p>"
    else:
        return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Logout logic coming soon</h1>"


