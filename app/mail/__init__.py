from flask import Blueprint

bp = Blueprint('mail', __name__)

from app.errors import handlers