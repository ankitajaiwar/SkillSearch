from flask import Flask, jsonify, request, render_template, session
from common.database import Database
from find_people import Find_People

#Flask Section

app = Flask(__name__)

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
