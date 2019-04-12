from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , PasswordField , Field , BooleanField
from wtforms.widgets.core import html_params
from wtforms.widgets import HTMLString
from markupsafe import Markup
class InlineButtonWidget(object):
    """
    Render a basic ``<button>`` field.
    """
    html = """
    <button type="submit" title="%s"><span>%s</span></button>
    """
    input_type = 'submit'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs ):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault('value', field.label.text)
        return HTMLString('<button %s>' % self.html_params(name=field.name, **kwargs))


class InlineSubmitField(BooleanField):
    """
    Represents an ``<button type="submit">``.  This allows checking if a given
    submit button has been pressed.
    """
    html = """
    <button type="submit" title="%s"><span>%s</span></button>
    """
    widget = InlineButtonWidget()


class LoginForm(FlaskForm):
    login = StringField('login')
    password = PasswordField('password')
    sbt  = SubmitField('button')
    btn  = Field(label='ok_lol' , widget=SubmitField)
    button = Markup('<input onclick="login_gen();" value="ok" type="button" id="submit">')