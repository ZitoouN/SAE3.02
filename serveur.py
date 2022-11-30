import socket
import platform
import os

host = "127.0.0.1" # "", "127.0.0.1
port = 8080
disc = True

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print('En attente de connexion client ...')
conn, address = server_socket.accept()
print(f'Client connecté : {address}')

while disc:
    data = conn.recv(1024).decode()
    if data == 'OS':
        conn.send(f"{platform.system()}".encode())
        print(f"Message du client : OS")
    else :
        print(f"Message du client : {data}")
