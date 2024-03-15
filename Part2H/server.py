#  from flask import Flask, render_template
# from flask_socketio import SocketIO
# import tkinter
# import tkinter.scrolledtext
# from tkinter import simpledialog

# import threading
# import socket

# app = Flask(__name__)
# socketio = SocketIO(app)

# HOST = "10.21.0.34"
# PORT = 9090

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen()

# clients = []
# usernames = []

# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             print(f"{usernames[clients.index(client)]} dit : {message}")
#             broadcast(message)

#         except Exception as e:
#             print(f"Erreur lors de la gestion du client : {e}")
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             username = usernames[index]
#             usernames.remove(username)
#             break  

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('connect')
# def handle_connect():
#     while True:
#         client, address = server.accept()
#         print(f"Connecté avec {str(address)}") 

#         client.send("username".encode("utf-8"))
#         username = client.recv(1024).decode()
#         usernames.append(username)
#         clients.append(client)

#         print(f"Nom d'utilisateur du client : {username}") 
#         broadcast(f"{username} connecté au serveur".encode("utf-8"))
#         client.send("Connecté au serveur".encode("utf-8"))
             
#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()
#         print("Attente Connexion...")

# ##if __name__ == '__main__':
#    ## socketio.run(app, debug=True)
# class Client:
#     def __init__(self, host, port):
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.connect((host, port))
#         msg = tkinter.Tk()
#         msg.withdraw()
#         self.username = simpledialog.askstring("Username", "Enter your username", parent=msg)
#         self.gui_done = False
#         self.running = True
#         gui_thread = threading.Thread(target=self.gui_loop)
#         receive_thread = threading.Thread(target=self.receive_loop)
#         gui_thread.start()
#         receive_thread.start()

#     def gui_loop(self):
#         self.win = tkinter.Tk()
#         self.win.config(bg="cyan")

#         self.chat_label = tkinter.Label(self.win, text="(Chat)", bg="cyan")
#         self.chat_label.configure(font="arial 12")
#         self.chat_label.pack(padx=20, pady=5)

#         self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
#         self.text_area.pack(padx=20, pady=5)
#         self.text_area.config(state="disabled")

#         self.msg_label = tkinter.Label(self.win, text="Message", bg="cyan")
#         self.msg_label.pack(padx=20, pady=5)
#         self.saisit= tkinter.Text(self.win,height=3)
#         self.saisit.pack(padx=20,pady=5)
#         self.btn_send=tkinter.Button(self.win,text="send",command=self.write)
#         self.btn_send.config(font='arial 12')
#         self.btn_envoie.pack(padx=20,pady=5)
#         self.gui_done=True
#         self.win.protocol("delete_window",self.stop)
#         self.win.mainloop()



#     def write(self):
#         message =f"(self.username):(self.saisit.get('1.0','end))"
#         self.sock.send(message.encode("utf-8"))
#         self.saisit.delet('1.0','end')   
#     def stop(self):
#         self.running = false
#         self.win.distroy()
#         self.sock.close()
#         exit(0)

#     def receive_loop(self):
#         while self.running:
#             try:
#                 message=self.sock.recv(1024)
#                 if message=="username":
#                     self.sock.send(self.username.encode("utf-8"))
#                 else:
            
#                  if self.gui_done:
#                     self.text_area.config(states="normal")
#                     self.text_area.insert("end",message)
#                     self.text_area.yview("end")
#                     self.text_area.config(state="disabled")
#             except ConnectionAbortedError: 
#                 break

#             except:
#                 print("Erreur")
#                 self.sock.close()
#                 break

        

# client = Client(HOST, PORT)

from flask import Flask, render_template
from flask_socketio import SocketIO
HOST = "192.168.56.1"
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
    socketio.run(app, debug=True)

