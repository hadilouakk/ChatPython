from flask import Flask, render_template
from flask_socketio import SocketIO,send

app= Flask(__name__)
app.config['SECRET']="secret!123"
socketio = SocketIO(app,cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print('message reçu: ' + message)
    if message != "Utilisateur connecté":
        send(message,broadcast="True")

@app.route('/')
def index():
    return render_template("session.html")

if __name__ == '__main__':
    socketio.run(app,host="192.168.128.1")