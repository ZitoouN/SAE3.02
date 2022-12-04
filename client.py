import sys
from socket import socket
import threading

mess = ''
data = ''
arret = 'arret'
bye = 'bye'

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
        mess = input(f"{user}>")
        client.send(mess.encode())
        if mess == "kill":
            client.send(mess.encode("kill"))
            client.close()
        elif mess == "disconnect":
            message = "disconnect"
            client.send(mess.encode({message}))


def reception(client):
    global user
    while True:
        data = client.recv(1024).decode()
        print(data)


def main():
    global s_t
    global user
    print('-----CLIENT-----')
    user = input('Inserer le nom du client : ')
    connection()
    t1 = threading.Thread(target=communication, args=[client])
    t2 = threading.Thread(target=reception, args=[client])
    t1.start()
    t2.start()
    t1.join()
    t2.join()



if __name__ == '__main__':
   main()
