import jinja2
from flask import render_template, redirect, url_for, flash, request
from flask_babel import _
import hashlib
# from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
# from app.models import User
# from app.auth.email import send_password_reset_email
from flask_login import login_user, logout_user, current_user
from app import app , session
from app.auth import auth_module
from app.auth.forms import LoginForm
from app.database.smdb import DataManager
from app.roles.usermodel import manage_persons ,list_user

dm = DataManager()
# @auth_module.route('/gen_key' , methods=['GET' , 'POST'])
# def gen_key():
#     ckey=request.values['key']
#     print(ckey)
#     # return render_template('auth/login.html' , form=LoginForm())
#     return "done"

@auth_module.route('/get_inds' , methods=['GET' , 'POST'])
def get_inds():
    # ckey = request.values['key']
    # print(ckey)
    return render_template("get_data.html" , var="var_in_template")

@app.route('/somee')
def somee():
    return '<p>somee</p>'

@auth_module.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        p = request.values
        print(p['login']+'\n'+p['password']+'\n'+p['ckey'])
        if dm.VerifyPassword(p['login'] , p['password']):
            manage_persons['login']         = p['login']
            manage_persons['ckey']          = p['ckey']
            manage_persons['privileges']    = dm.GetManagePersonsPrivileges(p['login'])
            session['username'] =p['login']
            print(session.values())
            list_user.append(manage_persons)
            for row in list_user:
                print(row)
            # print(manage_persons['login'])
            # TODO goto in gen_functions by privileges
            return redirect(url_for('roles' , user= session['username']))
        else:
            return render_template('auth/login.html' , form=LoginForm() , err="wrong password")
    else:
        return render_template('auth/login.html' , form=LoginForm())

@auth_module.route('/exit' , methods=['GET' , 'POST'])
def logout():
    if request.method == 'POST':
        manage_persons.clear()
        session.pop('username' , None)
    return render_template('auth/login.html' , form=LoginForm())

@auth_module.route('/log_ajax')
def log():
    print('что тут не так....')
    return render_template('index.html')

