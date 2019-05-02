from flask import Blueprint

diagram_module = Blueprint('diagrams', __name__)

from app.diagrams import views
