import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app , session
from flask_login import login_user, logout_user, current_user , login_manager
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l
# from flask_sqlalchemy import SQLAlchemy
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

# db = SQLAlchemy(app)


from app.errors import errors_module as errors_bp
app.register_blueprint(errors_bp)

from app.auth import auth_module as auth_bp
app.register_blueprint(auth_bp, url_prefix='/')

from app.main import app as main_bp
app.register_blueprint(main_bp)

from app.api import app as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.database import app as db_bp
app.register_blueprint(db_bp)

from app.signup import sigup_module as su_bp
app.register_blueprint(su_bp , url_prefix='/')

from app.gen_functions import function_module as f_bp
app.register_blueprint(f_bp)

from app import models , view_test ,view_indicators
from app.auth import views


