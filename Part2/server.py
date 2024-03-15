from flask import Flask, render_template
from flask_socketio import SocketIO
HOST = "192.168.235.131"
PORT = 5000
app = Flask(__name__,template_folder='templates')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Message received:', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True, host = HOST)

