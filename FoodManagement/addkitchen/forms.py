from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class AddKitchenForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Quantity = IntegerField('Quantity', validators=[DataRequired()])
    Veg = BooleanField('Veg/Non Veg', validators=[DataRequired()])
    Submit = SubmitField('Add/Update')