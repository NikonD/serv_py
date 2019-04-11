from flask import Blueprint

app = Blueprint('database', __name__)

from app.database import views