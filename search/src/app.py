from flask import Flask, jsonify, request, render_template, session

from common.database import Database

app = Flask(__name__)

@app.route('/skill')
def home():
  return render_template('search.html')


@app.route('/search/skill', methods=['POST'])
def login_user():
    Skill = request.form['Skill']
    print(Skill)
    # return render_template("search2.html", Skill=session['Skill'])
    return render_template("search2.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


if __name__ == '__main__':
    app.run(port=4995, debug=True)
