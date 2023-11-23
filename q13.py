#13. Implement notifications in a Flask app using websockets to notify users of updates.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('q13.html')

@socketio.on('connect')
def handle_connect():
    emit('notification', 'Connected to notifications.')

def send_notification(message):
    socketio.emit('notification', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
