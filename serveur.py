import socket

def Serveur():
    server_host = '127.0.0.1'
    port = 8080

    serveur = socket.socket()
    serveur.bind((server_host, port))

    serveur.listen(1)
    msg = ""


    while msg != 'arret':
        conn, adress = serveur.accept()
        msg = conn.recv(1024).decode()
        print('Client :', msg)
        conn.send(msg.encode())
        while msg != 'arret' and 'bye':
            msg = conn.recv(1024).decode()
            conn.send(msg.encode())
            print('Client :', msg)
        if msg == 'bye':
            conn.send(msg.encode())
            conn.close()
    conn.send(msg.encode())
    serveur.close()


if __name__ == '__main__':
    Serveur()