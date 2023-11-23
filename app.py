from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
app.secret_key = 'your-secret-key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_user'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        try:
            with mysql.connection.cursor() as cur:
                cur.execute(f"SELECT username, password FROM tbl_user WHERE username = '{username}'")
                user = cur.fetchone()
                if user and pwd == user[1]:
                    session['username'] = user[0]
                    return redirect(url_for('home'))
                else:
                    return render_template('login.html', error='Invalid username or password')
        except Exception as e:
            print("Error:", e)
            return render_template('login.html', error='Error connecting to the database')
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
