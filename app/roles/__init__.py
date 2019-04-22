from flask import Blueprint

role_model = Blueprint('roles' , __name__ )

from app.roles import role_view , usermodel