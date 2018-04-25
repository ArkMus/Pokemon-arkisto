from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PokeForm(FlaskForm):
    name = StringField("Name")
    number = StringField("Number")
  
    class Meta:
        csrf = False