from flask import render_template
from app.roles import role_model
from app.roles.getpage import manage_persons_page

@role_model.route('/role')
def role():
    return render_template(manage_persons_page(0))