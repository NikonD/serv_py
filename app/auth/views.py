from flask import render_template, redirect, url_for, flash, request
import jinja2
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from flask_babel import _
# from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
# from app.models import User
# from app.auth.email import send_password_reset_email
from flask_login import login_user, logout_user, current_user
from app import app
from app.auth import auth_module
from app.auth.forms import LoginForm

@auth_module.route('/gen_key' , methods=['GET' , 'POST'])
def gen_key():
    if request.method == 'GET':
        ckey=request.values['key']
        print(ckey)
    return render_template('auth/login.html' , form=LoginForm())

@auth_module.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(login)
        print(password)
    return render_template('auth/login.html' , form=LoginForm())