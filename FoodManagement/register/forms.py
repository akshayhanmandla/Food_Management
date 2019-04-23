from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField     

class RegisterForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Email = EmailField('Email', validators=[DataRequired()])
    # PhoneNumber = IntegerField('Phone Number', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Type = SelectField('Programming Language', choices=[('Kitchen', 'KITCHEN'), ('NGO', 'NGO')])
    Register = SubmitField('Register')
