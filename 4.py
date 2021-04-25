import os
import sys
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QWidget
from PyQt5 import uic


class MapApi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.v = 'map'
        self.latitude, self.longitude, self.scale = '37.530887', '55.703118', '0.002'
        uic.loadUi('4.ui', self)
        self.showmap.clicked.connect(self.mapCreate)
        self.map_request = ['http://static-maps.yandex.ru/1.x/?ll=', self.latitude, ',', self.longitude,
                            '&spn=', self.scale, ',', self.scale, '&l=map', self.v]
        self.mapCreate()
        self.focus()

    def movement(self, n):
        if n.key() == Qt.Key_PageUp:
            try:
                self.mashtab.setPlainText(str(float(self.mashtab.toPlainText()) + 0.01))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)
        if n.key() == Qt.Key_PageDown:
            try:
                self.mashtab.setPlainText(str(float(self.mashtab.toPlainText()) - 0.01))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)
        if n.key() == Qt.Key_Up:
            print(2)
            try:
                self.edit_y.setPlainText(str(float(self.edit_y.toPlainText()) -
                                             2 * float(self.mashtab.toPlainText())))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)
        if n.key() == Qt.Key_Down:
            print(1)
            try:
                self.edit_y.setPlainText(str(float(self.edit_y.toPlainText()) +
                                             2 * float(self.mashtab.toPlainText())))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)
        if n.key() == Qt.Key_Right:
            try:
                self.edit_x.setPlainText(str(float(self.edit_x.toPlainText()) +
                                             2 * float(self.mashtab.toPlainText())))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)
        if n.key() == Qt.Key_Left:
            try:
                self.edit_x.setPlainText(str(float(self.edit_x.toPlainText()) -
                                             2 * float(self.mashtab.toPlainText())))
                self.setImageToPixmap()
            except FloatingPointError as e:
                print(e)

    def showIm(self):
        self.latitude = self.x.toPlainText().strip()
        self.longitude = self.y.toPlainText().strip()
        self.scale = self.mashtab.toPlainText().strip()
        if self.task4.currentIndex() == 0:
            self.v = 'map'
        if self.task4.currentIndex() == 1:
            self.v = 'sat'
        if self.task4.currentIndex() == 2:
            self.v = 'skl'
        self.map_request = ''.join(['http://static-maps.yandex.ru/1.x/?ll=', self.latitude, ',',
                                    self.longitude, '&spn=', self.scale, ',', self.scale, '&l=', self.v])
        response = requests.get(self.map_request)
        if self.task4.currentIndex() == 2 or self.task4.currentIndex() == 0:
            self.map_file = "map.png"
        if self.task4.currentIndex() == 1:
            self.map_file = "map.jpeg"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        return True

    def mapCreate(self):
        fl = self.showIm()
        if fl:
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        self.focus()

    def focus(self):
        self.setFocusPolicy(Qt.StrongFocus)

    def close(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapApi()
    ex.show()
    sys.exit(app.exec())