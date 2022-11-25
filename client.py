import socket
import platform

def client_connect():
    print('Veuillez vous connecter à un serveur')
    a = input('Entrer une adresse IP : ')
    p = input('Entrer le port du serveur : ')
    client_socket = socket.socket()
    try:
        client_socket.connect((a,p))
    except:
        print('Une erreur a été détecté, veuillez réessayer')
        return reconnect()
    else:
        print('La connexion à pu être établie')

def reconnect():
    adr = input('Adresse IP : ')
    port = input('Port : ')
    client_socket = socket.socket()
    client_socket.connect((adr, port))


def communication(client_socket):
    while True:
        mess = input(f"{client} -> ")
        try
            if mess = 'os':
                return platform.processor()
            if mess = 'ram':
                return 