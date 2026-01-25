from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
''' Forms For Flask Projects '''
class TextConvertForm(FlaskForm):
    '''
    Form for converting text
    '''
    # create a text field
    textarea = StringField('Enter Text Here', validators=[DataRequired()])
    
    # create 4 submit field each representing different text cases
    uppercase = SubmitField('Change to uppercase')
    lowercase = SubmitField('Change to lowercase')
    sentence_case = SubmitField('Change to sentence case')
    title_case = SubmitField('Change to title case')