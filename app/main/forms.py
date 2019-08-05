from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from ..models import Pitches

class Pitch(FlaskForm):
  title = StringField('Enter the Title', validators=[Required()])
  description= TextAreaField('Give brief description',validators=[Required()])
  submit = SubmitField('Submit')
