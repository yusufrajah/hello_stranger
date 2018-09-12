from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello_stranger():
	return 'Hello stranger!'

@app.route("/hello/<name>")
def hello_name(name):
	return 'Hello %s!' % name
