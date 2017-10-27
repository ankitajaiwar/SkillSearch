from flask import Flask, render_template

app = Flask(__name__)

#socketio = SocketIO(app)

@app.route('/')
def index():
	return "Hello There!"
	#return render_template('index.html')

if __name__ == "__main__":
	app.run(port=4995,debug=True)