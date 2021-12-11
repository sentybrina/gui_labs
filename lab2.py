import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QFileDialog, QMenuBar, QFrame, QAction

DEFAULT_SIZE = 600
MENUBAR_HEIGHT = 22
MENUBAR_WIDTH = 100
PINK_PEN = QPen(QColor(215, 24, 104), 3)


class ClickableContainer(QFrame):
    def __init__(self, root, onPress, onMove, onRelease):
        super().__init__(root)
        self.onPress = onPress
        self.onMove = onMove
        self.onRelease = onRelease

    def mousePressEvent(self, event):
        self.onPress(event)

    def mouseMoveEvent(self, event):
        self.onMove(event)

    def mouseReleaseEvent(self, event):
        self.onRelease(event)


class Lab2App(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Инициализация главного экрана приложения
        """
        super(Lab2App, self).__init__()

        self.resize(DEFAULT_SIZE, DEFAULT_SIZE + MENUBAR_HEIGHT)

        self.loadAction = QAction("Открыть картинку", self)
        self.saveAction = QAction("Сохранить картинку", self)

        self.loadAction.triggered.connect(self.loadImage)
        self.saveAction.triggered.connect(self.saveImage)

        self.menuBar = QMenuBar(self)
        self.menuBar.resize(DEFAULT_SIZE, MENUBAR_HEIGHT)

        self.fileMenu = self.menuBar.addMenu('Файл')
        self.fileMenu.addAction(self.loadAction)
        self.fileMenu.addAction(self.saveAction)

        self.image = None
        self.clickableContainer = ClickableContainer(self, self.onPress, self.onMove, self.onRelease)
        self.clickableContainer.setGeometry(0, 0, 0, 0)

        self.startPoint = QPoint()
        self.endPoint = QPoint()

        self.rects = []

    def paintEvent(self, event):
        if self.image is not None:
            painter = QPainter(self)
            painter.setPen(PINK_PEN)
            painter.drawPixmap(
                QtCore.QRect(
                    0,
                    MENUBAR_HEIGHT,
                    self.image.width(),
                    self.image.height()
                ),
                self.image
            )
            if self.startPoint != self.endPoint:
                painter.drawRect(
                    QtCore.QRect(
                        self.startPoint.x(),
                        self.startPoint.y() + MENUBAR_HEIGHT,
                        self.endPoint.x() + 1 - self.startPoint.x(),
                        self.endPoint.y() + 1 - self.startPoint.y()
                    )
                )

    def onPress(self, event):
        if self.image is not None:
            self.startPoint = event.pos()

    def onMove(self, event):
        if self.image is not None:
            self.endPoint = event.pos()
            self.update()

    def onRelease(self, event):
        if self.image is not None:
            self.endPoint = event.pos()
            painter = QPainter(self.image)
            painter.setPen(QPen(PINK_PEN))
            rect = QtCore.QRect(
                self.startPoint,
                self.endPoint
            )
            painter.drawRect(rect)
            self.rects.append(rect)
            self.update()

    def loadImage(self):
        fileName = QFileDialog.getOpenFileName(self, caption="Открыть", filter="Image Files (*.png *.jpg *.bmp)")[0]
        if fileName is None or len(fileName) == 0:
            return
        self.image = QPixmap(fileName)

        w, h = self.image.width(), self.image.height()

        scale = 1.0
        if max(w, h) > DEFAULT_SIZE:
            scale = float(max(w, h) / DEFAULT_SIZE)

        w, h = int(w / scale), int(h / scale)

        self.image = self.image.scaled(w, h)
        self.clickableContainer.setGeometry(
            QtCore.QRect(
                0,
                MENUBAR_HEIGHT,
                self.image.width(),
                self.image.height() + MENUBAR_HEIGHT
            )
        )
        self.resize(
            max(MENUBAR_WIDTH, self.image.width()),
            self.image.height() + MENUBAR_HEIGHT
        )
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def saveImage(self):
        if self.image is None:
            return
        fileName = QFileDialog.getSaveFileName(self, "Сохранить", filter="Image Files (*.png *.jpg *.bmp)")[0]
        if fileName is None or len(fileName) == 0:
            return
        self.image.save(fileName)
        rectFileName = fileName + "rect.txt"
        rectFile = open(rectFileName, mode='w')
        for r in self.rects:
            center = r.center()
            rectFile.write(
                "Center [x=" + str(center.x()) + ", y=" + str(center.y()) + "]\n"
            )
        rectFile.close()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = Lab2App()
    app.show()
    sys.exit(application.exec_())
