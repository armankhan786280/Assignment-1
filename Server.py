import socket
import threading

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    print("Server is running and listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"👤 Nickname of the client is {nickname}")
        broadcast(f"🔔 {nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
