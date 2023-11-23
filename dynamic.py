#3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return "You are successful! Your marks: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You have failed! Your marks: " + str(score)

@app.route('/result/<int:marks>')
def results(marks):
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)



