from flask import render_template
from app import app
@app.route('/some')
def some():
    return '<h1>some</h1>'
