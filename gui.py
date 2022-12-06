import sys
from PyQt5.QtWidgets import *

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
        self.__CONNECTION = QPushButton("Connection")
        self.__SEND = QPushButton("Envoyer")

        self.__ADRESSE_IP = QLineEdit("")
        self.__PORT_EDIT = QLineEdit("")
        self.__CMD = QLineEdit("")

        self.__msg = QMessageBox()


        grid.addWidget(self.__ESPACE, 1, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE2, 4, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ESPACE3, 7, 0)  # composant, ligne, colonne

        grid.addWidget(self.__CONNECTION_LABEL, 0, 0)  # composant, ligne, colonne
        grid.addWidget(self.__ADRESSE_IP, 0, 1)  # composant, ligne, colonne
        grid.addWidget(self.__PORT_EDIT, 0, 2)  # composant, ligne, colonne
        grid.addWidget(self.__CONNECTION, 0, 3)  # composant, ligne, colonne


        grid.addWidget(self.__COMMANDE, 8, 0)  # composant, ligne, colonne
        grid.addWidget(self.__CMD, 8, 1,1,2)  # composant, ligne, colonne
        grid.addWidget(self.__SEND, 8, 3)  # composant, ligne, colonne

        self.setWindowTitle("Interface de surveillance de serveurs ou de machines clients")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec()
