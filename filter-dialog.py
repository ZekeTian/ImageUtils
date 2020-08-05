# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.tb_sketch = QtWidgets.QRadioButton(self.groupBox_2)
        self.tb_sketch.setGeometry(QtCore.QRect(90, 10, 115, 19))
        self.tb_sketch.setObjectName("tb_sketch")
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
        self.btn_ok.clicked.connect(Dialog.accept)
        self.rb_black_white.toggled['bool'].connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rb_black_white.setText(_translate("Dialog", "黑白"))
        self.tb_sketch.setText(_translate("Dialog", "素描"))
        self.rb_embossment.setText(_translate("Dialog", "浮雕"))
        self.rb_reminiscence.setText(_translate("Dialog", "怀旧"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
