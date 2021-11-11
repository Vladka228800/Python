import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QAction, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


class Button(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self._closable = False
        # self.title = u'Тест'

        self.coords = [40, 40]
        self.btn_size = [50, 20]
        self.d = 15
        self.w = 500
        self.h = 400
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('тест')

        self.btn2 = Button(self)
        self.btn2.setMouseTracking(True);
        self.btn2.setText("да")
        self.btn2.resize(*self.btn_size)
        self.btn2.move(100, 100)
        self.btn2.clicked.connect(self.fun)

        self.btn = Button(self)
        self.btn.setMouseTracking(True);
        self.btn.setText("нет")
        self.btn.resize(*self.btn_size)
        self.btn.move(170, 100)
        self.btn.mouseMoved.connect(self.moveButton)

        self.lbl = QLabel(self)
        self.lbl.resize(40, 10)
        self.lbl.move(150, 10)
        self.lbl.setText('ты лох?')

        self.lbl2 = QLabel(self)
        self.lbl2.resize(40, 10)
        self.lbl2.move(150, 30)

        # self.button = QPushButton(u'Закрыть', self)
        # self.button.clicked.connect(self.on_click)

        self.show()

    def moveButton(self):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.btn.move(*self.coords)

    def fun(self):
        self.lbl2.setText('я знал')

    def closeEvent(self, evnt):
        if self._closable:
            super(app, self).closeEvent(evnt)
        else:
            evnt.ignore()

    # @pyqtSlot()
    # def on_click(self):
    #     self._closable = True
    #     self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())