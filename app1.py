#1. Create a Flask app that displays "Hello, World!" on the homepage.
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug = True)