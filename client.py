import socket
import threading
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class Client:
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


    def envoie(self,message):
        try:
            self.__socket.send(message.encode())
            data = self.__socket.recv(1024).decode()
        except:
            print("ERREUR")
        else:
            return data


    def __envoi(self):
        msg = input("CLIENT>")
        try:
            self.__socket.send(msg.encode())
        except BrokenPipeError:
            print("ERREUR, SOCKET FERME")


    def get_message(self):
        return self.__message

    def set_message(self, msg):
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
        print('La connexion à pu être établie')





######################################################################################################################################################################################



class GUI(QMainWindow):
    singleton: 'GUI' = None

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)


        with open('client.css', 'r') as f:
            client = f.read()
        app.setStyleSheet(client)

        self.txtcmd = ""

        self.__CONNECTION_LABEL = QLabel("IP - Port :")
        self.__LOG_LABEL = QLabel("LOGS")
        self.__COMMANDE = QLabel("Commande :")
        self.__CONNECTION = QPushButton("Connexion")
        self.__ADRESSE_IP = QLineEdit("127.0.0.1")
        self.__PORT_EDIT = QLineEdit("10013")
        self.__CMD = QLineEdit("RAM")
        self.__TB = QTextBrowser()
        self.__TB.setAcceptRichText(True)
        self.__LOG = QTextBrowser()
        self.__LOG.setAcceptRichText(True)
        self.__ENTRER = QPushButton('OK')
        self.__CLEAR = QPushButton('Clear')
        self.__CLEAR2 = QPushButton('Clear')
        self.__ETAT = QLabel("DÉCONNECTÉ")
        self.__ETAT.setStyleSheet("color: red; font-weight: bold;")
        self.__SOCKET = socket.socket()
        self.__list = QComboBox()
        self.__list.addItems(['RAM','CPU','OS','IP','Name','Connexion information'])
        self.__ESPACE = QLabel("")
        self.__ESPACE2 = QLabel("")



        grid.addWidget(self.__CMD, 9,1 , 1,5)  # composant, ligne, colonne
        grid.addWidget(self.__TB, 3,1 , 4,10) # ligne, colonne, hauteur, largueur
        grid.addWidget(self.__LOG, 3,12, 4, 10)  # ligne, colonne, hauteur, largueur
        grid.addWidget(self.__CLEAR, 10,1 , 1,10)
        grid.addWidget(self.__CLEAR2, 9, 15, 1, 4)
        grid.addWidget(self.__ENTRER, 9,6, 1,2)
        grid.addWidget(self.__ETAT, 0,0)
        grid.addWidget(self.__list, 9,10, 1,1)
        grid.addWidget(self.__CONNECTION_LABEL, 2,0)  # composant, ligne, colonne
        grid.addWidget(self.__LOG_LABEL, 2, 16,1, 4)  # composant, ligne, colonne
        grid.addWidget(self.__ADRESSE_IP, 2, 1, 1,3)  # composant, ligne, colonne
        grid.addWidget(self.__PORT_EDIT, 2, 4, 1,3)  # composant, ligne, colonne
        grid.addWidget(self.__CONNECTION, 2, 7, 1,4)  # composant, ligne, colonne
        grid.addWidget(self.__COMMANDE, 9, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE2, 0, 11)  # composant, ligne, colonne

        d = "Veuillez vous connectez s'il vous plaît."
        self.__TB.append(d)

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)

        self.setWindowTitle("Interface de surveillance de serveurs ou de machines clients")
        self.__CONNECTION.clicked.connect(self._connexion)
        self.__ENTRER.clicked.connect(self._ajout_commande)
        self.__CLEAR.clicked.connect(self._clear)
        self.__CLEAR2.clicked.connect(self._clear2)



    def _connexion(self):
        host = str(self.__ADRESSE_IP.text())
        port = int(self.__PORT_EDIT.text())
        self.__socket = Client(host, port)
        try:
            self.__socket.Connect()
            self.__ETAT.setText("CONNECTÉ")
            self.__ETAT.setStyleSheet("""
            QLabel {
                    color: #00FF00;
                    font-weight: bold;
                    }
                    """)
        except ConnectionRefusedError:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Warning)
            mess.setText("CONNECTION ERREUR SERVEUR !")
            mess.exec()
            return -1
        except ConnectionError:
            print("CONNECTION ERROR")
            return -1
        except ConnectionResetError:
            print('CONNECTION RESET ERROR')
            return -1
        else:
            c = "Connexion réussie !"
            self.__TB.append(c)
            return 0



    def _ajout_commande(self):
        try:
            self.cmd = self.__CMD.text()
            self.__TB.append("client>" + self.cmd)
            self.__LOG.append("Message du client : " + self.cmd)

            Client.set_message(self.__socket, self.__CMD.text())
            msg = Client.get_message(self.__socket)
            data = Client.envoie(self.__socket, msg)

            if msg == 'kill':
                m = 'SERVEUR FERMER !'
                self.__TB.append(m)
                QCoreApplication.instance().quit()

            elif msg == 'reset':
                m = 'Redémarrage ...'
                self.__TB.append(m)
                d = "Veuillez vous connectez s'il vous plaît."
                self.__TB.append(d)
                i = 'DÉCONNECTÉ'
                self.__ETAT.setText(i)
                self.__ETAT.setStyleSheet("color: red; font-weight: bold;")


            elif msg == 'disconnect':
                m = 'Deconnexion ... !'
                self.__TB.append(m)
                QCoreApplication.instance().quit()

        except:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Warning)
            mess.setText("VOUS N'ETES PAS CONNECTER !")
            mess.exec()
        else:
            self.__TB.append(data)

    def _clear(self):
        self.__TB.clear()

    def _clear2(self):
        self.__LOG.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec()
