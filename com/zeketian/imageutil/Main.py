import sys, os
from com.zeketian.imageutil.ui.MainUI import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore


class MyWindow(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = MyWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
