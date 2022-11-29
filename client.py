from socket import socket
import platform
import threading
import os

def connection():
    global client
    print('-----CONNEXION AU SERVEUR-----')
    a = str(input('Entrer une adresse IP : '))
    p = int(input('Entrer le port du serveur : '))
    client = socket()
    try:
        client.connect((a, p))
    except:
        print('Une erreur a été détecté, veuillez réessayer')
        return connection()
    else:
        print('La connexion à pu être établie')


def communication(client):
    global user
    while True:
        message = input(f"{user}>")
        client.send(message.encode())
        if message == "disconnect":
            client.close()
            break
        elif message == "close":
            print ("Client disconnected")
            exit()


def reception(client):
    while True:
        data = client.recv(1024).decode()
        print(data)


def main():
    global user
    print('-----CLIENT-----')
    user = input('Inserer le nom du client : ')
    connection()
    t1 = threading.Thread(target=reception, args=[client])
    t2 = threading.Thread(target=communication, args=[client])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    client.close()
    print('Successfully disconnected from socket')


if __name__ == '__main__':
   main()
