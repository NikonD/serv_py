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
from flask import render_template
from app import app , session , db
from app.auth.forms import FlaskForm
from app.roles.usermodel import manage_persons



@app.route('/')
@app.route('/index')
def index():

    if 'username' in session:
        print(session['username'])
        print(manage_persons)
        return render_template('index.html' , user=session['username'])
    else:
        return render_template('auth/login.html' , form=LoginForm())


