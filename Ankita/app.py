# author : Ankita Singh
from base64 import encode

import bcrypt as bcrypt
from flask import Flask, render_template, redirect, request, url_for, flash, session, logging
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt




from datetime import datetime
import time


import pymongo
from bson.objectid import ObjectId

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['skillsearch']
collection = database['registration']
app = Flask(__name__)


@app.route('/')
def index():
    if 'userid' in session:
        return 'You are logged in as '+session['userid']
        return render_template('session.html')
    else:
        return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')



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

@app.route('/register.html', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        fname = form.fname.data
        sname = form.fname.data
        uname = form.fname.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        confirm = form.confirm.data
        university = form.university.data
        department = form.department.data
        collection.insert({'fname': fname,'sname': sname, 'uname': uname, 'email': email, 'password': password, 'confirm': confirm, 'university': university, 'department': department} )
        return render_template('regsuccess.html')


    return render_template('register.html', form = form)


if __name__ == '__main__':
    app.run(port=4995, debug=True)






