import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel


class Lab1App(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lab1App, self).__init__()

        self.setFixedSize(250, 125)

        font = QFont("Times New Roman", 14)

        self.button = QPushButton(self)
        self.button.setFont(font)
        self.button.setText("Сгенерировать!")
        self.button.setGeometry(QRect(25, 75, 200, 25))

        self.label = QLabel(self)
        self.label.setFont(font)
        self.label.setGeometry(QRect(25, 25, 200, 25))

        self.button.clicked.connect(self.on_button_click)
        self.on_button_click()

    def on_button_click(self):
        self.label.setText("Рандомное число {}".format(random.randint(1, 100)))

if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = Lab1App()
    app.show()
    sys.exit(application.exec_())
