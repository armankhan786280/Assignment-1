import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("An error occurred! Exiting...")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('utf-8'))

recv_thread = threading.Thread(target=receive)
recv_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
