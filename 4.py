import os
import os
import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5 import uic
from PIL import Image


class MyMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.latitude, self.longitude, self.scale = '37.530887', '55.703118', '0.002'
        uic.loadUi('4.ui', self)
        self.showmap.clicked.connect(self.mapCreate)
        self.map_request = ['http://static-maps.yandex.ru/1.x/?ll=', self.latitude, ',', self.longitude,
                            '&spn=', self.scale, ',', self.scale, '&l=map']
        self.mapCreate()

    def getImage(self):
        self.latitude = self.edit_x.toPlainText()
        self.longitude = self.edit_y.toPlainText()
        self.scale = self.mashtab.toPlainText()
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
        return 'успех'

    def mapCreate(self):
        is_all_secc = self.getImage()
        if is_all_secc == 'успех':
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        else:
            self.image.setText(is_all_secc)

    def close(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMap()
    ex.show()
    sys.exit(app.exec())