from flask import Blueprint

errors_module = Blueprint('errors', __name__)

from app.errors import views
