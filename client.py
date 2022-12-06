import socket, threading, sys


class Client():
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = socket.socket()
        self.__thread = None

    def host(self, host):
        self.__host = host

    def port(self, port):
        self.__port = port


    def connection(self) -> int:
        try:
            self.__socket.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("CONNECTION ERREUR SERVEUR")
            return -1
        except ConnectionError:
            print("CONNECTION ERROR")
            return -1
        except ConnectionResetError:
            print('CONNECTION RESET ERROR')
            return -1
        else:
            print("Connexion réussie !")
            return 0

    def Connect(self):
        self.__socket.connect((self.__host, self.__port))


    def dialogue(self):
        msg = ""
        self.__thread = threading.Thread(target=self.__reception, args=[self.__socket, ])
        self.__thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.__envoi()
        self.__thread.join()
        self.__socket.close()


    def __envoi(self):
        msg = input("CLIENT>")
        try:
            self.__socket.send(msg.encode())
        except BrokenPipeError:
            print("ERREUR, SOCKET FERME")

    def message_obtenue(self):
        return self.__message

    def message_(self, msg):
        self.__message = msg


    def __reception(self, conn):
        msg = ""
        try:
            while msg != "kill" and msg != "disconnect" and msg != "reset":
                msg = conn.recv(1024).decode()
                print(msg)
        except ConnectionResetError:
            return -1



if __name__ == "__main__":
    if len(sys.argv) < 3:
        client = Client("127.0.0.1", 8080)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        client = Client(host, port)
    try:
        client.connection()
        client.dialogue()
    except KeyboardInterrupt:
        print("INTERRUPTION CLAVIER !")

