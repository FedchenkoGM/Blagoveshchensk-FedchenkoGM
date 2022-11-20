import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint, choice

from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw(self, qp):
        colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                  'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        qp.setPen(QPen(QColor(choice(colors)), 5, Qt.SolidLine))
        r = randint(30, 200)
        x, y = randint(5, 795 - r), randint(30, 595 - r)
        qp.drawEllipse(x, y, r, r)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())