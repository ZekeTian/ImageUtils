# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compress-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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

        self.retranslateUi(Dialog)
        self.btn_ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_width.setText(_translate("Dialog", "Width:"))
        self.label_height.setText(_translate("Dialog", "Height:"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
