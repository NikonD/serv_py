from flask_wtf import FlaskForm
from wtforms import TextField  , BooleanField , PasswordField , SelectField , SubmitField , DateField
from wtforms.validators import DataRequired , Email
from markupsafe import Markup

class EditInds(FlaskForm):
    select_inds = SelectField("select indicators" , render_kw={"onchange":"load_indicators()"})
    text_name_ind = TextField("name indicator" , render_kw={"placeholder": "имя индикатора", "class":"r"})
    text_id_ind = TextField("number indicator" , render_kw={"placeholder": "номер", "class":"r"})
    btn_add = Markup('<a onclick="add_inds();" class="btn btn-primary">ADD</a>')
    btn_del = Markup('<a onclick="del_inds();" class="btn btn-primary">Del</a>')

    def gen_select(self , data):
        self.select_inds.choices = data
