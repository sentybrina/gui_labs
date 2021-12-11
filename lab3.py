import sys
from PyQt5 import QtWidgets

from PyQt5.QtCore import QRect, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QLabel, QComboBox

from lab3_signal import MONTHS, MonthInfo

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 150

FONT = QFont("Times New Roman", 14)


class Lab3App(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lab3App, self).__init__()
        month_list = list(MONTHS.keys())

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.monthComboBox = QComboBox(self)
        self.monthComboBox.setGeometry(QRect(80, 20, 210, 30))
        self.monthComboBox.setFont(FONT)
        self.monthComboBox.addItems(month_list)
        self.monthLabel = QLabel(self)
        self.monthLabel.setFont(FONT)
        self.monthLabel.setText("Месяц")
        self.monthLabel.setGeometry(QRect(10, 20, 70, 30))

        self.numberValueLabel = QLabel(self)
        self.numberValueLabel.setGeometry(QRect(80, 60, 220, 30))
        self.numberValueLabel.setFont(FONT)
        self.numberLabel = QLabel(self)
        self.numberLabel.setFont(FONT)
        self.numberLabel.setText("Номер")
        self.numberLabel.setGeometry(QRect(10, 60, 70, 30))

        self.seasonValueLabel = QLabel(self)
        self.seasonValueLabel.setGeometry(QRect(80, 100, 220, 30))
        self.seasonValueLabel.setFont(FONT)
        self.seasonLabel = QLabel(self)
        self.seasonLabel.setFont(FONT)
        self.seasonLabel.setText("Сезон")
        self.seasonLabel.setGeometry(QRect(10, 100, 70, 30))

        self.monthInfo = MonthInfo()

        self.monthInfo.signal.connect(lambda x: self.monthInfo.update_value(x))
        self.monthComboBox.activated[str].connect(self.on_combo_changed)
        self.on_combo_changed(month_list[0])

    def on_combo_changed(self, text):
        self.monthInfo.signal.emit(text)
        self.numberValueLabel.setText(self.monthInfo.number)
        self.seasonValueLabel.setText(self.monthInfo.season)

if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = Lab3App()
    app.show()
    sys.exit(application.exec_())
