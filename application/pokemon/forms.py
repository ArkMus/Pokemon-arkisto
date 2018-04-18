from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators

class PokeForm(FlaskForm):
    name = StringField("Name")
    number = IntegerField("Number")
  
    class Meta:
        csrf = False