from flask import Blueprint

app = Blueprint('errors', __name__)

from app.errors import views
