# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UsernameForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    submit = SubmitField('Sprawdź')

class SelectRangeForm(FlaskForm):
    range = SelectField('Pasmo')