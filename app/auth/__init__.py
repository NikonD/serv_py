from flask import Blueprint

auth_module = Blueprint('auth', __name__)

from app.auth import views
