#10. Design a Flask app with proper error handling for 404 and 500 errors.
from flask import Flask ,render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'),500
@app.route('/')
def index():
    return "Welcome to the Flask App!"
@app.route('/trigger_error')
def trigger_error():
    # Simulate an internal server error
    a = 1 / 0  # This will raise a ZeroDivisionError
    return "This won't be reached because of the error above"
if __name__ == '__main__':
    app.run(debug = True)