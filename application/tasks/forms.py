from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, validators

class TaskForm(FlaskForm):
    name = TextField("Task name", [validators.Length(min=2)])
    done = BooleanField('Done')
 
    class Meta:
        csrf = False
