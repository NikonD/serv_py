import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l
import os
from config import Config

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()

babel = Babel()

app = Flask(__name__);
app.secret_key = 'SHH!'
app.config.from_object(__name__)

from app.errors import app as errors_bp
app.register_blueprint(errors_bp)

from app.auth import auth_module as auth_bp
app.register_blueprint(auth_bp, url_prefix='/')

from app.main import app as main_bp
app.register_blueprint(main_bp)

from app.api import app as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import models

