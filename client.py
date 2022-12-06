import socket
import threading
import sys
from PyQt5.QtWidgets import *


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


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)


        self.__ESPACE = QLabel("")
        self.__ESPACE2 = QLabel("")
        self.__ESPACE3 = QLabel("")

        self.__CONNECTION_LABEL = QLabel("IP - Port :")
        self.__COMMANDE = QLabel("Commande :")
        self.__CONNECTION = QPushButton("Connexion")

        self.__ADRESSE_IP = QLineEdit("127.0.0.1")
        self.__PORT_EDIT = QLineEdit("8080")

        self.__CMD = QLineEdit()

        self.__TB = QTextBrowser()
        self.__TB.setAcceptRichText(True)

        self.__CLEAR = QPushButton('Clear')


        grid.addWidget(self.__CMD, 8,1 , 1,2)  # composant, ligne, colonne
        grid.addWidget(self.__TB, 4,1 , 1,2)
        grid.addWidget(self.__CLEAR, 8, 3)

        grid.addWidget(self.__ESPACE, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE2, 4, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE3, 7, 0)  # composant, ligne, colonne

        grid.addWidget(self.__CONNECTION_LABEL, 0, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ADRESSE_IP, 0, 1)  # composant, ligne, colonne
        grid.addWidget(self.__PORT_EDIT, 0, 2)  # composant, ligne, colonne
        grid.addWidget(self.__CONNECTION, 0, 3)  # composant, ligne, colonne

        grid.addWidget(self.__COMMANDE, 8, 0)  # composant, ligne, colonne

        self.setWindowTitle("Interface de surveillance de serveurs ou de machines clients")

        self.__CONNECTION.clicked.connect(self._connexion)
        self.__CMD.returnPressed.connect(self._ajout_commande)
        self.__CLEAR.pressed.connect(self._clear)


    def _ajout_commande(self):
        text = self.__CMD.text()
        self.__TB.append(text)
        self.__CMD.clear()

    def _clear(self):
        self.__TB.clear()
