from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QLCDNumber, QCheckBox
import sys
from PyQt5 import uic

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 400, 125)
        # self.setWindowTitle('программа')

        uic.loadUi("D:\Python\le.ui", self)
        self.textEdit.setText("Hello")
        # self.letters = ["a", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # #Rezult TextBox
        # self.textBox = QLineEdit(self)
        # self.textBox.move(100, 5)
        # self.textBox.resize(100, 25)
        #
        # # Text which we are writting into button
        # self.a = ""
        #
        # # button Coords
        # self.x = 10
        # self.y = 5
        # for i in range(len(self.letters) - 1):
        #     self.button_letter = QPushButton(self)
        #     self.button_letter.resize(20, 20)
        #     self.a += self.letters[i]
        #     self.x += 22
        #     if self.x >= 360:
        #         self.x = 5
        #         self.y += 22
        #     self.button_letter.move(self, self.x, self.y)
        #     self.button_letter.clicked.connect(self.textBox.setText(self.a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
