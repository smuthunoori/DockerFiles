from flask import Flask
app = Flask(__name__)

@app.route("/greetings")
def hello():
    return "Hello, World!"

