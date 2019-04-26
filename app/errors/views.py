from app.errors import errors_module
from flask import render_template , session

@errors_module.route('/error')
def error():
    return render_template('errors/e404.html' , msg=session['error_view'])
