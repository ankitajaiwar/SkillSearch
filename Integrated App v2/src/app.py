from flask import Flask, jsonify, request, render_template, session, redirect, url_for, flash, logging
from common.database import Database
from wtforms import Form, StringField, PasswordField, validators
from find_people import Find_People
from passlib.hash import sha256_crypt
from datetime import datetime
import time
from registerform import RegisterForm
from user import User

app = Flask(__name__)
app.secret_key = 'skillsearch'

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/register')
def register_button():
    return render_template('register.html')

@app.route('/login')
def login_button():
    return render_template('login.html')

@app.route('/login_auth', methods =['POST'])
def login_authentication():
    user_name = request.form['username']
    pwd = request.form['pwd']

    user = User(username=user_name, pwd=pwd)
    if user.validateUser(user_name=user_name,pwd=pwd):
        print('successful login')
        fName = User.getName(username=user_name)
        session['username'] = fName
        return render_template('userhome.html')

    else:
        print('invalid credentials')
        return render_template('login.html')

@app.route('/register_page',methods=['POST'])
def register_page():
    fname = request.form['First Name']
    lname = request.form['Last Name']
    uname = request.form['Username']
    email = request.form['email']
    password = sha256_crypt.encrypt(str(request.form['pwd']))
    confirm = sha256_crypt.encrypt(str(request.form['Confirm password']))
    university = request.form['University']
    department = request.form['Department']

    registrationData = {'fname': fname, 'sname': lname, 'uname': uname, 'email': email, 'password': password,
                        'confirm': confirm, 'university': university, 'department': department}
    Database.insert(collection="user_profiles", data=registrationData)

    return render_template('regsuccess.html')

@app.route('/userhome')
def user_home():
    return render_template('userhome.html')

@app.route('/addskill')
def add_skill():
    return render_template('addskill.html')

@app.route('/skilladded', methods=['POST'])
def skillform():
    skill = request.form['skills']
    newSkill = request.form['newSkill']
    message = "no message"
    if (skill == "") and (newSkill == ""):
        message = "Failed to add skills"
    else:
        message = "Skills Added"

    _name = session['username']
    print(_name)
    Database.insert(collection="skillset",data={'name':_name,'skill':skill})
    return render_template("addskill.html",msg = message)



@app.route('/searchpeople')
def search_people():
    return render_template('search.html')

@app.route('/skilledpeople',methods=['POST'])
def skilled_people():
    Skill = request.form['Skill']
    s = "Skill being requested: {}"
    print(s.format(Skill))

    # Searching people in MongoDB for skill = Skill:
    results = Find_People.search_from_mongo(skill=Skill)
    print("List of people with requested skill:")
    peopleNames = []
    for people in results:
        peopleNames.append(people['Name'])
        print(people['Name'])

    return render_template("search.html", results=peopleNames)

@app.route('/logout')
def log_out():
    session.pop('username',None)
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()

if __name__ == '__main__':
    app.run(port=4995, debug=True)