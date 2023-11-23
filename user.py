#4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('user.html', user_input=user_input)
    return render_template('user.html', user_input=None)

if __name__ == '__main__':
    app.run(debug=True)


    