#12. Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update(data):
    # Process incoming data
    # For instance, you can broadcast the updated data to all clients
    socketio.emit('data_updated', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
