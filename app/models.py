import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
import os
from time import time
from flask import current_app, url_for ,request
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.forms import LoginForm
from app.roles.usermodel import manage_persons
from app.database.smdb import DataManager
from flask import render_template ,redirect
from app import app , session , db
from app.auth.forms import FlaskForm

dm = DataManager()

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        print(session['username'])
        return redirect(url_for('roles' , user=session['username']))
    elif request.method == 'POST':
        p = request.values
        print(p['login']+'\n'+p['password']+'\n'+p['ckey'])
        if dm.VerifyPassword(p['login'] , p['password']):
            session['username']             = p['login']
            print(session.values())
            # TODO goto in gen_functions by privileges
            return redirect(url_for('roles' , user=session['username']))
        else:
            print('wrong\033[33m')
            return render_template('auth/login.html' , form=LoginForm() , err="wrong password")
    return render_template('auth/login.html' , form=LoginForm())

@app.route('/roles/<user>')
def roles(user):
    return render_template('roles/admin/main.html' , user=user)