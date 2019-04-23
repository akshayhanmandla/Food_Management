from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class CartForm(FlaskForm):
    Submit = SubmitField('Place Order')