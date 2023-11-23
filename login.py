#5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "login"

@app.route('/')
def login1():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "sheetal" and password == "123":
            session['email'] = username
            return render_template("success.html", email=username)
        else:
            msg = "Invalid username/password"
            return render_template("login.html", msg=msg)

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        msg = "Login first"
        return render_template("login.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)


