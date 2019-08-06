from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from ..models import Pitch


class PitchForm(FlaskForm):
  title = StringField('Enter the Title', validators=[Required()])
  description= TextAreaField('Give brief description',validators=[Required()])
  submit = SubmitField('Submit')
 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

 
class Comments(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('SUBMIT')    
 