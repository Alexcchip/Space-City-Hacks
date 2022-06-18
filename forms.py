from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField, RadioField, SelectMultipleField, SelectField, validators, EmailField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
     uLocation = StringField("Your Location (Country): ", [validators.DataRequired()])
     searchLocation = StringField("Chatter Location: ", [validators.DataRequired()])
     uLanguage = StringField("Your Language: ", [validators.DataRequired()])
