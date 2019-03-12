from flask_wtf import FlaskForm
from wtforms import TextField , BooleanField , PasswordField , SelectField , SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    btn_sbt     = SubmitField("OK" , validators=[DataRequired])
    
    text         = TextField("логин", validators=[DataRequired()])
    iin_text     = TextField("ИИН" , validators=[DataRequired()])
    f_name       = TextField("first name" , validators=[DataRequired()])
    s_name       = TextField("second name" , validators=[DataRequired()])
    t_name       = TextField("third name" , validators=[DataRequired()])
    iin_key_text = TextField("iin" , validators=[DataRequired()])
    f_name       = TextField("first name" , validators=[DataRequired()])
    s_name       = TextField("second name" , validators=[DataRequired()])
    t_name       = TextField("third name" , validators=[DataRequired()])

    category     = SelectField('Category', choices=[("admin", "админ"),("methodist", "методист"),("gauptman", "заведующий")])
    
    pass_field   = PasswordField("enter a password" , validators=[DataRequired()])
    pass_repeat  = PasswordField("repeat a password" , validators=[DataRequired()])
    pas          = PasswordField("password", validators=[DataRequired()])