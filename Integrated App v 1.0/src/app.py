from flask import Flask, jsonify, request, render_template, session, redirect, url_for, flash, logging
from common.database import Database
from wtforms import Form, StringField, PasswordField, validators
from find_people import Find_People
from passlib.hash import sha256_crypt
from datetime import datetime
import time

#Flask Section
from registerform import RegisterForm

app = Flask(__name__)
current_session = ""

@app.route('/')
def index():
    if 'userid' in session:
        return 'You are logged in as '+session['userid']
        return render_template('session.html')
    else:
        return render_template('index.html')

@app.route('/register_button')
def register_button():
    return render_template("register.html")

@app.route('/register-page',methods=['POST'])
def register_page():
    fname = request.form['First Name']
    sname = request.form['Sur Name']
    uname = request.form['Last Name']
    email = request.form['email']
    password = request.form['pwd']
    confirm = request.form['Confirm password']
    university = request.form['University']
    department = request.form['Department']
    # print(fname)
    # return render_template("dummy.html")
    registrationData = {'fname': fname, 'sname': sname, 'uname': uname, 'email': email, 'password': password,
                       'confirm': confirm, 'university': university, 'department': department}
    Database.insert(collection="user_profiles",data=registrationData)

    return render_template('regsuccess.html')

@app.route('/useraccount')
def useraccount():
    print()
    return render_template("home.html")

@app.route('/userlogin')
def userlogin():
    return render_template("login.html")


#--------------------------------------------------------------------------------

@app.route('/addskill')
def addskill():
  return render_template('addskill.html')

@app.route('/addskill/add', methods=['POST'])
def skillform():
    skills = request.form['skills']
    newSkill = request.form['newSkill']
    message = "no message"
    if (skills == "") and (newSkill == ""):
        message = "Failed to add skills"
    else:
        message = "Skills Added"
    return render_template("addskill.html",msg = message)


@app.route('/skill')
def home():
  return render_template('search.html')


@app.route('/search/skill', methods=['POST'])
def login_user():
    Skill = request.form['Skill']
    s = "Skill being requested: {}"
    print(s.format(Skill))

    #Searching people in MongoDB for skill = Skill:
    results = Find_People.search_from_mongo(skill=Skill)
    print("List of people with requested skill:")
    peopleNames=[]
    for people in results:
        peopleNames.append(people['Name'])
        print(people['Name'])

    # return render_template("search2.html", Skill=session['Skill'])
    # return render_template("search2.html")
    return render_template("search.html", results=peopleNames)


@app.before_first_request
def initialize_database():
    Database.initialize()

if __name__ == '__main__':
    app.run(port=4995, debug=True)
