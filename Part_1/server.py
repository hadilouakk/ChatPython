import socket 
import threading

host = '192.168.235.131'
port = 59000

#Creation connexion TCP avec socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

#Autorise les connexions entrantes
server.listen()

clients = []
nicknames = []

def broadcast(message):

    #Afficher les messsages de chaque client dans le terminal 
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]
            nicknames.remove(nickname)
            break

def receive():

    while True:
        print ("server is running ...")
        #On recupère à partir du server les clients et leur adress
        client, address = server.accept()


        print (f'connection with {str(address)}')
        client.send('nickname ?'.encode('utf-8'))

        #On recupere la reponse du client
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)
        
        #On affiche le nom du client connecté 
        print(f'{nickname} is connected '.encode('utf-8'))

        #On affiche dans le terminal du client qu'il est connecté
        client.send("you are connected ".encode('utf-8'))
        
        thread = threading.Thread(target = handle_client, args = (client,))
        thread.start()

receive()


