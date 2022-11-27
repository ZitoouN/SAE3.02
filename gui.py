import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__OS = QPushButton("OS")
        self.__RAM = QPushButton("RAM")
        self.__CPU = QPushButton("CPU")
        self.__IP = QPushButton("IP")
        self.__NAME = QPushButton("NAME")


        self.__ESPACE = QLabel("")
        self.__ESPACE2 = QLabel("")
        self.__ESPACE3 = QLabel("")

        self.__CONNECTION_LABEL = QLabel("IP :")
        self.__COMMANDE = QLabel("Commande :")
        self.__CONNECTION = QPushButton("Connection")
        self.__SEND = QPushButton("Envoyer")

        self.__DISCONNECT = QPushButton("DISCONNECT")
        self.__CON_INFO = QPushButton("Connexion info")
        self.__KILL = QPushButton("KILL")
        self.__RESET = QPushButton("RESET")

        self.__ADRESSE_IP = QLineEdit("")
        self.__CMD = QLineEdit("")


        grid.addWidget(self.__OS, 6, 0)  # composant, ligne, colonne
        grid.addWidget(self.__RAM, 6, 1)  # composant, ligne, colonne
        grid.addWidget(self.__CPU, 6, 2)  # composant, ligne, colonne
        grid.addWidget(self.__IP, 6, 3)  # composant, ligne, colonne
        grid.addWidget(self.__NAME, 6, 4)  # composant, ligne, colonne

        grid.addWidget(self.__ESPACE, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE2, 4, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE3, 7, 0)  # composant, ligne, colonne

        grid.addWidget(self.__CONNECTION_LABEL, 0, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ADRESSE_IP, 0, 1)  # composant, ligne, colonne
        grid.addWidget(self.__CONNECTION, 0, 2)  # composant, ligne, colonne

        grid.addWidget(self.__COMMANDE, 8, 0)  # composant, ligne, colonne
        grid.addWidget(self.__CMD, 8, 1)  # composant, ligne, colonne
        grid.addWidget(self.__SEND, 8, 2)  # composant, ligne, colonne

        grid.addWidget(self.__DISCONNECT, 0, 4)  # composant, ligne, colonne
        grid.addWidget(self.__CON_INFO, 1, 4)  # composant, ligne, colonne
        grid.addWidget(self.__KILL, 2, 4)  # composant, ligne, colonne
        grid.addWidget(self.__RESET, 3, 4)  # composant, ligne, colonne

        self.setWindowTitle("Interface de surveillance de serveurs ou de machines clients")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec()





'''import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__ok = QPushButton("Ok")
        self.__nom = QLabel("")
        self.__quit = QPushButton("Quitter")

        grid.addWidget(self.__lab, 0, 0)  # composant, ligne, colonne
        grid.addWidget(self.__text, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ok, 2, 0)  # composant, ligne, colonne
        grid.addWidget(self.__nom, 3, 0)  # composant, ligne, colonne
        grid.addWidget(self.__quit, 4, 0)  # composant, ligne, colonne

        self.__ok.clicked.connect(self._actionOk)
        self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        self.__nom.setText(f"Bonjour {self.__text.text()}")

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()'''