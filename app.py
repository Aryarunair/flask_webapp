from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This is my python assignment to create a python web application."