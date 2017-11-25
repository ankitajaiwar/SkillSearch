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
from flask_socketio import SocketIO, send, join_room, emit

app = Flask(__name__)
app.secret_key = 'skillsearch'
socketio = SocketIO(app)


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        message = "Welcome Back! " + username
        return redirect(url_for('user_home', message=message))
        # return render_template('userhome.html', msg="Welcome Back! "+username,unname=username)

    return render_template('index.html')

@app.route('/about')
def about_button():
    return render_template("about.html")

@app.route('/contactus')
def contact_button():
    return render_template("contactus.html")

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
        uname = fName
        return redirect(url_for('user_home',message=message))
        # return render_template('userhome.html', msg = message, unname=uname)
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

@app.route('/userhome/<message>')
def user_home(message):
    # For displaying skills and scores of user profile
    print("inside User Home ****")
    skillName = []
    skillScore = []
    skillRecords = Find_People.search_from_mongo2(name=session['username'])

    # for skillDetails in skillRecords:
    #     skillName.append(skillDetails['skill'])
    #     skillScore.append(skillDetails['score'])
    #     # print(skillDetails['skill'])
    #     # print(skillDetails['score'])
    # skillNamesDistinct = list(set(skillName))

    skillItems = []
    for skillDetails in skillRecords:
        # dict == {}
        # you just don't have to quote the keys
        an_item = dict(skillName=skillDetails['skill'], skillScore=skillDetails['score'])
        skillItems.append(an_item)
    return render_template('userhome.html',unname=session['username'],msg=message,skillItems=skillItems)

@app.route('/addskill', methods = ['GET','POST'])
def add_skill():
    if 'username' in session:
        skill_list = ListSkill.list_skills()
        # print (skill_list)
        return render_template('addskill.html', skill_list=skill_list)
    else:
        # return render_template('index.html')
        return redirect(url_for('index'))

@app.route('/skilladded', methods=['GET','POST'])
def skillform():
    skill = request.form['skills']
    newSkill = request.form['newSkill']
    print (skill, newSkill)
    message = "no message"
    skill_list = ListSkill.list_skills()
    if (skill != ""):
        skillUpdate = skill
        message = "Skills Added"
    elif(newSkill != ""):
        skillUpdate = newSkill
        message = "Skills Added"
    else:
        message = "Failed to add skills"
        return render_template("addskill.html", msg=message, skill_list=skill_list)
        
    _name = session['username']
    print(_name)
    user_skill_list = ListSkill.user_skills(_name)
    if(skillUpdate in user_skill_list):
        message = skillUpdate + " skill is already added."
    else:
        Database.insert(collection="skillset",data={'name':_name,'skill':skillUpdate,'score':0 })
    skill_list = ListSkill.list_skills()
    # print (skill_list)
    return render_template("addskill.html",msg = message, skill_list=skill_list)


@app.route('/searchpeople')
def search_people():
    if 'username' in session:
        skill_list = ListSkill.list_skills()
        return render_template('search.html',skillList=skill_list)
    else:
        return redirect(url_for('index'))

@app.route('/skilledpeople',methods=['POST'])
def skilled_people():
    Skill = request.form.getlist('Skill')
    print("The skills requested are:")
    for s in Skill:
        print(s)

    # Searching people in MongoDB for skill = Skill:
    print("List of people with requested skill:")
    message = "List of people with requested skill:"
    peopleNames = []

    for sk in Skill:
        results = Find_People.search_from_mongo(skill=sk)
        for people in results:
            peopleNames.append(people['name'])
            print(people['name'])
    peopleNamesDistinct = list(set(peopleNames))
    skill_list = ListSkill.list_skills()
    return render_template("search.html", results=peopleNamesDistinct, msg = message, skillList=skill_list,Skill=Skill)


@app.route('/logout')
def log_out():
    session.pop('username',None)
    message = "Log Out Successful"
    return render_template('login.html', msg = message)
    # return redirect(url_for('login_button',msg = message))

@app.route('/chat',methods=['POST'])
def chatHandler():
    chatuser = request.form['roomname']
    if chatuser==' ':
        chatuser = session['username']
        print("Setting Roomname to default")
    print(session['username']+" requested chat to: "+ chatuser)
    session['room'] = chatuser
    return render_template("chat.html")

@app.route('/chatself')
def selfChatHandler():
    print("Setting Roomname for Own")
    session['room'] = session['username']
    return render_template("chat.html")

@app.route('/testsuite',methods=['POST'])
def test_suite():
    skName = request.form['skName']
    qnRecords = Find_People.search_from_mongo3(skill=skName)
    qItems = []
    qnCount=0
    for qns in qnRecords:
        qnCount = qnCount+1
        _item = dict(qno=qns['qno'], qn=qns['qn'],opt1=qns['opt1'],opt2=qns['opt2'],opt3=qns['opt3'],opt4=qns['opt4'])
        qItems.append(_item)
    if qnCount == 0:
        return "No questions yet, please come back later :)"
    else:
        return render_template("test_suite.html",qItems=qItems, sk=skName, qnCount=qnCount)

@app.route('/evaltest',methods=['POST'])
def eval_test():
    skillName = request.form['skillName']
    qnRecords = Find_People.search_from_mongo3(skill=skillName)
    skillCount = request.form['skillCount']
    answers = []
    for i in range(1,int(skillCount)+1):
        option = request.form[str(i)]
        print(option)
        answers.append(option)
    correctAnswers = []
    for qns in qnRecords:
        print("Correct answers")
        print(qns['ans'])
        correctAnswers.append(qns['ans'])
    noOfCorrect = 0
    for i in range(0, int(skillCount)):
        if answers[i] == correctAnswers[i]:
            noOfCorrect = noOfCorrect + 1
    # noOfCorrect = set(answers) & set(correctAnswers)
    # noOfCorrect = set(answers).intersection(correctAnswers)
    print("The #Correct: "+str(noOfCorrect))
    Database.update(collection="skillset", name=session['username'], skill=skillName, score=str(noOfCorrect))
    message = "Test Complete. Score Updated"
    return redirect(url_for('user_home', message=message))

@socketio.on('text')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ':' + message['msg']}, room=room)

@socketio.on('joined')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    newRoom = session['room']
    print(session['username']+" Joining Room : "+newRoom)
    join_room(newRoom)
    emit('status', {'msg': session.get('username') + ' has entered the room.'}, room=newRoom)

@app.before_first_request
def initialize_database():
    Database.initialize()
    Database.dropCollection("testsuite")
    testQuestions = {"skill":"Android","qno":"1","qn":"Which term corresponds to UI?","opt1":"Service","opt2":"Background","opt3":"Activity","opt4":"Thread","ans":"opt3"}
    Database.insert(collection="testsuite", data=testQuestions)
    testQuestions = {"skill": "Android", "qno": "2", "qn": "Which file tells aboutt he apps permissions ", "opt1": "Service file",
     "opt2": "Broadcast file", "opt3": "Manifest", "opt4": "log file", "ans": "opt3"}
    Database.insert(collection="testsuite", data=testQuestions)
    testQuestions={"skill": "Java", "qno": "1", "qn": "Pick the one which is not an OOP's concept?", "opt1": "Inheritance",
     "opt2": "Polymorphism", "opt3": "Classes", "opt4": "Integer variables", "ans": "opt4"}
    Database.insert(collection="testsuite", data=testQuestions)
    testQuestions = {"skill":"Java","qno":"2","qn":"Using which library you can get inputs ","opt1":"Math","opt2":"Arrays","opt3":"Scanner","opt4":"Swing","ans":"opt3"}
    Database.insert(collection="testsuite", data=testQuestions)

if __name__ == '__main__':
    socketio.run(app,port=4995,debug=True)
    # app.run(port=4995, debug=True)
