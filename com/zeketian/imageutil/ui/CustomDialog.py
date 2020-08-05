# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watermark-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog


class WatermarkDialog(QDialog):
    """
    设置水印信息的对话框
    """

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.btn_confirm = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_confirm.setOrientation(QtCore.Qt.Horizontal)
        self.btn_confirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.__current_position = "左上角"  # 水印位置初始值为左上角

        self.retranslateUi(Dialog)
        self.comboBox.activated.connect(self.handle_activated)
        self.btn_confirm.accepted.connect(Dialog.accept)
        self.btn_confirm.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "左上角"))
        self.comboBox.setItemText(1, _translate("Dialog", "右上角"))
        self.comboBox.setItemText(2, _translate("Dialog", "中间"))
        self.comboBox.setItemText(3, _translate("Dialog", "左下角"))
        self.comboBox.setItemText(4, _translate("Dialog", "右下角"))

    def get_watermark_text(self):
        return self.lineEdit.text()

    def get_watermark_position(self):
        return self.__current_position

    def handle_activated(self, index):
        self.__current_position = self.comboBox.itemText(index)


class OcrDialog(QDialog):
    """
    显示 OCR 结果的对话框
    """

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 302)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(Dialog)
        self.btn_ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OCR结果"))
        self.btn_ok.setText(_translate("Dialog", "OK"))


class CompressDialog(QDialog):
    """
    设置压缩信息的对话框
    """

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 100)
        Dialog.setMinimumSize(QtCore.QSize(300, 100))
        Dialog.setMaximumSize(QtCore.QSize(300, 100))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_width = QtWidgets.QLabel(Dialog)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_2.addWidget(self.label_width)
        self.input_width = QtWidgets.QLineEdit(Dialog)
        self.input_width.setObjectName("input_width")
        self.horizontalLayout_2.addWidget(self.input_width)
        self.label_height = QtWidgets.QLabel(Dialog)
        self.label_height.setObjectName("label_height")
        self.horizontalLayout_2.addWidget(self.label_height)
        self.input_height = QtWidgets.QLineEdit(Dialog)
        self.input_height.setObjectName("input_height")
        self.horizontalLayout_2.addWidget(self.input_height)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 设置输入框内容的整型验证器，从而限制输入的数据类型
        self.input_width.setValidator(QIntValidator())
        self.input_height.setValidator(QIntValidator())

        self.retranslateUi(Dialog)
        self.btn_ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "请输入目标图片大小"))
        self.label_width.setText(_translate("Dialog", "Width:"))
        self.label_height.setText(_translate("Dialog", "Height:"))
        self.btn_ok.setText(_translate("Dialog", "OK"))


class FilterDialog(QDialog):
    """
       选择滤镜效果的对话框
       """

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 150)
        Dialog.setMinimumSize(QtCore.QSize(200, 150))
        Dialog.setMaximumSize(QtCore.QSize(200, 150))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb_black_white = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_black_white.setGeometry(QtCore.QRect(10, 10, 115, 19))
        self.rb_black_white.setObjectName("rb_black_white")
        self.rb_sketch = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_sketch.setGeometry(QtCore.QRect(90, 10, 115, 19))
        self.rb_sketch.setObjectName("rb_sketch")
        self.rb_embossment = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_embossment.setGeometry(QtCore.QRect(10, 40, 115, 19))
        self.rb_embossment.setObjectName("rb_embossment")
        self.rb_reminiscence = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_reminiscence.setGeometry(QtCore.QRect(90, 40, 115, 19))
        self.rb_reminiscence.setObjectName("rb_reminiscence")
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        self.filter_type = "黑白"  # 默认选择为 “黑白” 效果
        self.rb_black_white.setChecked(True)

        self.rb_black_white.toggled.connect(self.__select_filter)
        self.rb_sketch.toggled.connect(self.__select_filter)
        self.rb_embossment.toggled.connect(self.__select_filter)
        self.rb_reminiscence.toggled.connect(self.__select_filter)
        self.btn_ok.clicked.connect(Dialog.accept)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "滤镜"))
        self.rb_black_white.setText(_translate("Dialog", "黑白"))
        self.rb_sketch.setText(_translate("Dialog", "素描"))
        self.rb_embossment.setText(_translate("Dialog", "浮雕"))
        self.rb_reminiscence.setText(_translate("Dialog", "怀旧"))
        self.btn_ok.setText(_translate("Dialog", "OK"))

    def __select_filter(self):
        if self.rb_black_white.isChecked():
            self.filter_type = "黑白"
        elif self.rb_sketch.isChecked():
            self.filter_type = "素描"
        elif self.rb_embossment.isChecked():
            self.filter_type = "浮雕"
        elif self.rb_reminiscence.isChecked():
            self.filter_type = "怀旧"