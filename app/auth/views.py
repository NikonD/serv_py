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
    ckey=request.values['key']
    print(ckey)
    # return render_template('auth/login.html' , form=LoginForm())
    return "done"

@app.route('/get_inds' , methods=['GET' , 'POST'])
def get_inds():
    ckey = request.values['key']
    print(ckey)
    return render_template("get_data.html" , var="var_in_template")

@auth_module.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        p = request.values
        print(p['login'])
        return render_template('index.html')
    else:
        return render_template('auth/login.html' , form=LoginForm())

@auth_module.route('/log_ajax')
def log():
    print('что тут не так....')
    return render_template('index.html')