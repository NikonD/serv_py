from flask import  Blueprint

function_module = Blueprint('gen_func' , __name__)

from app.gen_functions import function