# Author: Ankita
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from datetime import datetime
import time
import date

# register
class RegisterForm(Form):
    fname = StringField('FirstName', [validators.Length(min = 1, max = 50)])
    lname = StringField('LastName', [validators.Length(min=1, max=50)])
    uname = StringField('Username', [validators.Length(min=5, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50), validators.Email()])
    password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo('confirm', message = 'Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    university = StringField('University')
    department = StringField('Department')
    

