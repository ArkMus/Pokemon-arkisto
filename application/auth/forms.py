from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, validators
  
class LoginForm(FlaskForm):
    name = TextField("Name")
    username = TextField("Username")
    password = PasswordField("Password")

    
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = TextField("Name")
    username = TextField("Username")
    password = PasswordField("Password", [validators.Length(min=8)])
    
    class Meta:
        csrf = False
