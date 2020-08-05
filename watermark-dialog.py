# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watermark-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.btn_confirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
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
