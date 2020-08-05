from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtWidgets


class ImageLabel(QLabel):
    """"
    用于显示图片的 Label
    """

    # x0 = 0
    # y0 = 0
    # x1 = 0
    # y1 = 0
    # flag = False
    def __init__(self, parent=None):
        # super(ImageLabel, self).__init__(parent)
        super().__init__(parent)

        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False  # 标记是否能够绘制矩形
        self.__isClear = False  # 标记是否是清除矩形
        self.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.setFrameShape(QtWidgets.QFrame.Box)  # 设置边框
        self.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(218, 218, 218)")
        self.setText("")

        self.__w, self.__h = 0, 0
        self.pixmap_width, self.pixmap_height = 0, 0  # pixmap 的宽度、高度
        self.pixmap_x_start, self.pixmap_y_start = 0, 0  # pixmap 在 label 中的起点位置
        self.pixmap_x_end, self.pixmap_y_end = 0, 0  # pixamp 在 label 中的终点位置

        self.img_x_start, self.img_y_start = 0, 0  # 图片中选择的矩形区域的起点位置
        self.img_x_end, self.img_y_end = 0, 0  # 图片中选择的矩形区域的终点位置
        self.autoFillBackground()

    # 鼠标点击事件
    def mousePressEvent(self, event):
        # self.flag = True
        # 鼠标点击，相当于开始绘制矩形，将 isClear 置为 False
        self.__isClear = False
        self.x0 = event.x()
        self.y0 = event.y()

        # 计算 Pixmap 在 Label 中的位置
        self.__w, self.__h = self.width(), self.height()
        self.pixmap_x_start = (self.__w - self.pixmap_width) / 2
        self.pixmap_y_start = (self.__h - self.pixmap_height) / 2
        self.pixmap_x_end = self.pixmap_x_start + self.pixmap_width
        self.pixmap_y_end = self.pixmap_y_start + self.pixmap_height

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        # self.flag = False
        self.setCursor(Qt.ArrowCursor)  # 鼠标释放，矩形已经绘制完毕，恢复鼠标样式

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.pixmap_width, self.pixmap_height = pixmap.width(), pixmap.height()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)

        # 判断是否是清除
        if self.__isClear:
            return  # 是清除，则不需要执行下面的绘制操作。即此次 paint 事件没有绘制操作，因此界面中没有绘制的图形（从而相当于清除整个界面中已有的图形）

        # 判断用户起始位置是否在图片区域，只有在图片区域才画选择的矩形图
        if (self.pixmap_x_start <= self.x0 <= self.pixmap_x_end) \
                and (self.pixmap_y_start <= self.y0 <= self.pixmap_y_end):
            # 判断结束位置是否在图片区域内，如果超过，则直接设置成图片区域的终点
            if self.x1 > self.pixmap_x_end:
                self.x1 = self.pixmap_x_end
            elif self.x1 < self.pixmap_x_start:
                self.x1 = self.pixmap_x_start

            if self.y1 > self.pixmap_y_end:
                self.y1 = self.pixmap_y_end
            elif self.y1 < self.pixmap_y_start:
                self.y1 = self.pixmap_y_start
            rect = QRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)

            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)

            # 计算矩形区域在图片中的位置
            self.img_x_start = int(self.x0 - self.pixmap_x_start)
            self.img_x_end = int(self.x1 - self.pixmap_x_start)
            self.img_y_start = int(self.y0 - self.pixmap_y_start)
            self.img_y_end = int(self.y1 - self.pixmap_y_start)

    def clearRect(self):
        # 清除
        self.__isClear = True
        self.update()
