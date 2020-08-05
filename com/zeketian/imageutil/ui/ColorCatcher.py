from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QGuiApplication, QColor, QCursor
from PyQt5.QtWidgets import QWidget, QApplication, QDialog

from com.zeketian.imageutil.ui.UiColorCatcher import ColorCatcherDialog


class ColorCatcher(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = ColorCatcherDialog()
        self.ui.setupUi(self)
        self.ui.lineEditMark.setText("按空格键确定")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.catch)
        self.timer.start(100)
        self.nowColor = None
        self.setCursor(Qt.CrossCursor)
        self.show()

    def catch(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()
        pixmap = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, 1, 1)
        if not pixmap.isNull():
            image = pixmap.toImage()
            if not image.isNull():
                if (image.valid(0, 0)):
                    color = QColor(image.pixel(0, 0))
                    r, g, b, _ = color.getRgb()
                    self.nowColor = color
                    self.ui.lineEditMove.setText('(%d, %d, %d) %s' % (r, g, b, color.name().upper()))
                    self.ui.lineEditMove.setStyleSheet('QLineEdit{border:2px solid %s;}' % (color.name()))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.ui.lineEditMark.setText(self.ui.lineEditMove.text())
            self.ui.lineEditMark.setStyleSheet('QLineEdit{border:2px solid %s;}' % (self.nowColor.name()))
