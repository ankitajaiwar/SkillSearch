from flask import Flask, render_template, request, session
Authentication = Flask(_name_)
Authentication.secret_key ="skill"

@Authentication.route('/')
def hello_method():
    return render_template('login.html')

@Authentication.before_first_request
def initialize_database():
    Database.initialize()
@Authentication.route('/login', methods=['GET','POST'])
def login_user():
    username=request.form['username']
    password=request.form['password']

    if User.login_valid(username,password):
       User.login(username)

    else:
        session['username'] = None

    return render_template("homepage.html", username=session['username'])

if _name_ == '_main_':
    Authentication.run(port=4995)