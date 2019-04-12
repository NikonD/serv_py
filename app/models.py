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
from app import app
@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')


