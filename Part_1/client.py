import socket 
import threading

nickname = input("choose a nickname")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.128.1', 59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "nickname ?":
                client.send(nickname.encode('utf-8'))
            else:
                print (message)

        except:
            print ('Error')
            client.close()
            break


def client_send():
    while True:
        message_content = input("Message : ")
        # Créer le message en utilisant une f-string
        message = f'{nickname} : {message_content}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()




