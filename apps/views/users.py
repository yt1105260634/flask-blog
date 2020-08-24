from flask import Blueprint, render_template

_users = Blueprint('users',__name__)

@_users.route('/login/')
def login():
    return render_template('users/login.html')


@_users.route('/register/')
def register():
    return render_template('users/register.html')