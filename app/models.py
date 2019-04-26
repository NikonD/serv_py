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
from app import app , session
from app.auth.forms import FlaskForm
from app.roles.usermodel import manage_persons
from app.roles.getpage import manage_persons_page
from app.errors import views

dm = DataManager()

@app.route('/')
@app.route('/index')
def index():
    session['guest'] = True
    if 'username' in session:
        print(session['username'])
        return redirect(url_for('roles' , user=session['username']))
    elif request.method == 'POST':
        manage_persons.clear()
        p = request.values
        print(p['login']+'\n'+p['password']+'\n'+p['ckey'])
        if dm.VerifyPassword(p['login'] , p['password']):
            session['username']             = p['login']
            session['guest']                = False
            # print(session.values())
            # TODO goto in gen_functions by privileges
            return redirect(url_for('roles' , user=session['username']))
        else:
            print('wrong')
            return render_template('auth/login.html' , form=LoginForm() , err="wrong password")
    return render_template('auth/login.html' , form=LoginForm() , warnning="not in session")

@app.route('/roles/<user>')
def roles(user):
    session.pop('error_view' , None)
    print(session)
    if  session['guest'] == True:
        session['error_view']= 'Вы не авторизованы'
        return redirect(url_for('errors.error'))
    else:
        if user != session['username']:
            session['error_view']= 'переход по урлу'
            return redirect(url_for('errors.error'))
    return render_template(manage_persons_page(manage_persons['privileges']) , user=user)
