# Authors: Vigneshwar, Jaswanth, Ankita, Tejaswini
from flask import Flask, jsonify, request, render_template, session, redirect, url_for, flash, logging
from pymongo import response

from common.database import Database
from wtforms import Form, StringField, PasswordField, validators
from find_people import Find_People
from enlist import ListSkill
from passlib.hash import sha256_crypt
from datetime import datetime
import time
from registerform import RegisterForm
from user import User

app = Flask(__name__)
app.secret_key = 'skillsearch'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('userhome.html', msg="Welcome Back! "+username)

    return render_template('index.html')

@app.route('/register')
def register_button():
    return render_template('register.html')

@app.route('/login')
def login_button():
    return render_template('login.html')

@app.route('/login_auth', methods =['POST'])
def login_authentication():
    user_name='somejunk'
    pwd='somejunk'
    user_name = request.form['username']
    pwd = request.form['pwd']

    print(user_name,pwd)

    message = ""
    if User.validateUser(user_name=user_name,pwd=pwd):
        fName = User.getName(username=user_name)
        session['username'] = fName
        message = 'Log in Successful. Welcome '+fName
        return render_template('userhome.html', msg = message)
    else:
        message = 'Please Try Again'
        return render_template('login.html', msg = message)

@app.route('/register_page',methods=['POST'])
def register_page():
    fname = request.form['FirstName']
    lname = request.form['LastName']
    uname = request.form['Username']
    email = request.form['email']
    password = sha256_crypt.encrypt(str(request.form['pwd']))
    confirm = sha256_crypt.encrypt(str(request.form['ConfirmPassword']))
    university = request.form['University']
    department = request.form['Department']

    registrationData = {'fname': fname, 'sname': lname, 'uname': uname, 'email': email, 'password': password,
                        'confirm': confirm, 'university': university, 'department': department}
    Database.insert(collection="user_profiles", data=registrationData)

    return render_template('regsuccess.html')

@app.route('/userhome')
def user_home():
    return render_template('userhome.html')


@app.route('/addskill', methods = ['GET','POST'])
def add_skill():
    if 'username' in session:
        skill_list = ListSkill.list_skills()
        # print (skill_list)
        return render_template('addskill.html', skill_list=skill_list)
    else:
        # return render_template('index.html')
        return redirect(url_for('index'))

@app.route('/skilladded', methods=['POST'])
def skillform():

    skill = request.form['skills']
    newSkill = request.form['newSkill']
    message = "no message"
    if (skill != ""):
        skillUpdate = skill
        message = "Skills Added"
    elif(newSkill != ""):
        skillUpdate = newSkill
        message = "Skills Added"
    else:
        message = "Failed to add skills"
        return render_template("addskill.html", msg=message)
        
    _name = session['username']
    print(_name)
    Database.insert(collection="skillset",data={'name':_name,'skill':skillUpdate})
    skill_list = ListSkill.list_skills()
    # print (skill_list)
    return render_template("addskill.html",msg = message, skill_list=skill_list)


@app.route('/searchpeople')
def search_people():
    if 'username' in session:
        return render_template('search.html')
    else:
        return redirect(url_for('index'))

@app.route('/skilledpeople',methods=['POST'])
def skilled_people():
    Skill = request.form['Skill']
    s = "Skill being requested: {}"
    print(s.format(Skill))

    # Searching people in MongoDB for skill = Skill:
    results = Find_People.search_from_mongo(skill=Skill)
    print("List of people with requested skill:")
    message = "List of people with requested skill:"
    peopleNames = []
    for people in results:
        peopleNames.append(people['name'])
        print(people['name'])

    return render_template("search.html", results=peopleNames, msg = message)

@app.route('/logout')
def log_out():
    session.pop('username',None)
    message = "Log Out Successful"
    # return render_template('login.html', msg = message)
    return redirect(url_for('login_button',msg = message))


@app.before_first_request
def initialize_database():
    Database.initialize()

if __name__ == '__main__':
    app.run(port=4995, debug=True)