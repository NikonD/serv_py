from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , PasswordField , Field , BooleanField , IntegerField
from markupsafe import Markup
class SignupForm(FlaskForm):
    login       = StringField('login' ,  render_kw={"placeholder": "Login"})
    password    = PasswordField('password' ,  render_kw={"placeholder": "Password"})
    privileges  = IntegerField('privileges' ,  render_kw={"placeholder": "Privileges(number)"})
    button      = Markup('<input onclick="signup();" value="ok" type="button" id="submit">')