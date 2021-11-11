# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QPainter, QColor
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QSlider, QFileDialog
# from PIL import Image
# import random
# from PyQt5.QtCore import Qt
# class DisplayArea(QtWidgets.QLabel, QWidget):
#     def __init__(self):
#         super().__init__()
#         self.pix_map = QtGui.QPixmap()
#         self.initUI()
#
#     def initUI(self):
#         self.QP = None
#         self.setGeometry(500, 500, 500, 500)
#
#
#     def mousePressEvent(self, event):
#         self.dist = random.randint(50, 200)
#         self.r = random.randint(0, 255)
#         self.g = random.randint(0, 255)
#         self.b = random.randint(0, 255)
#         self.Fl = -1
#         self.x = event.x()
#         self.y = event.y()
#         self.button = event.button()
#         self.QP = QPainter()
#
#
#     def paintEvent(self, event):
#         if self.QP is not None:
#             self.QP = QPainter()
#             self.QP.begin(self)
#             self.QP.setBrush(QColor(self.r, self.g, self.b))
#             self.QP.setPen(QColor(self.r, self.g, self.b))
#             if self.button == Qt.RightButton:
#                 self.QP.drawRect(self.x, self.y, self.dist, self.dist)
#             if self.button == Qt.LeftButton:
#                 self.QP.drawEllipse(self.x, self.y, self.dist, self.dist)
#
#             self.QP.end()
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QMainWindow()
#     da = DisplayArea()
#     w.setCentralWidget(da)
#     w.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        mySlider = QSlider(Qt.Horizontal, self)
        mySlider.setGeometry(30, 40, 200, 30)
        mySlider.valueChanged[int].connect(self.changeValue)

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("Checkbox Example")
        self.show()

    def changeValue(self, value):
        print(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())