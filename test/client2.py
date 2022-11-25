import threading, sys
from socket import socket
from validators import ipv4

# CLIENT


def connect():
    print('--- CONNECT TO SOCKET ---')
    ip = input('Insert IP address: ')
    while not ipv4(ip):
        ip = str(input('Please insert valid IP address (A.B.C.D): '))
    port = int(input(f"Insert the socket's port {ip}:"))
    client_socket = socket()
    try:
        client_socket.connect((ip, port))
    except:
        print('There was an error while connecting to socket')
        sys.exit(-1)
    else:
        print('Connection was a success.')
        return client_socket


def disconnect(client_socket):
    global stop_threads
    client_socket.close()
    stop_threads = True


def recieve(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        if stop_threads:
            sys.exit()


def write(client_socket):
    global username
    global exit
    while True:
        msg = input(f"{username}> ")
        try:
            if len(msg) > 0:
                if msg[0] == '/':
                    if msg == '/help':
                        print('List of commands: \n /rename <NAME> (Changes username of client) \n /disconnect (Diconnect from server) \n /exit (Closes application and disconnects Client) \n /shutdown (Shuts down the server)')
                    elif msg == '/disconnect':
                        disconnect(client_socket)
                    elif msg.split(' ')[0] == '/rename':
                        if len(msg.split(' ')) != 2:
                            print('Error. Usage : /rename <NAME>')
                        else:
                            username = msg.split(' ')[1]
                    elif msg == '/exit':
                        disconnect(client_socket)
                        exit = True
                        sys.exit()
                    elif msg == '/shutdown':
                        message = f'<user_requestSD7231UEIQS823>SHUTDOWN'
                        disconnect(client_socket)
                        sys.exit()
                    else:
                        print('Unknown command. Type /help for a list of commands')
                else:
                    if len(msg) > 0:
                        message =f'{username}> {msg}'
                        client_socket.send(message.encode())
        except:
            print('Connection with server was lost.')
            disconnect(client_socket)
            sys.exit(-2)
        if stop_threads:
            sys.exit()


def main():
    global stop_threads
    global username
    if username is None:
        username = input('Insert username: ')
    client_socket = connect()
    T1 = threading.Thread(target=write, args=[client_socket])
    T2 = threading.Thread(target=recieve, args=[client_socket])
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    client_socket.close()
    print('Successfully disconnected from socket')
    stop_threads = False
    if not exit:
        main()
    else:
        sys.exit()


if __name__ == '__main__':
    threads = []
    exit = False
    username = None
    stop_threads = False
    main()