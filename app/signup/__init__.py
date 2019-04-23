from flask import Blueprint

sigup_module = Blueprint('signup' , __name__)

from app.signup import views