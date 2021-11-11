import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test1.ui', self)  # Загружаем дизайн

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.count = 0

    def run(self):
        self.count += 1
        self.lcdNumber.display(self.count)


if __name__ == 'main':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())