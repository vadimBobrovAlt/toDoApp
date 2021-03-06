# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from loginScreenFw import Ui_loginDialog
from regScreenFw import Ui_regDialog


class Ui_MainDialog(QDialog):

    def __init__(self):
        super(Ui_MainDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(222, 160)
        self.loginButton = QtWidgets.QPushButton(MainDialog)
        self.loginButton.setGeometry(QtCore.QRect(40, 30, 151, 41))
        self.loginButton.setObjectName("loginButton")
        self.regButton = QtWidgets.QPushButton(MainDialog)
        self.regButton.setGeometry(QtCore.QRect(40, 90, 151, 41))
        self.regButton.setObjectName("regButton")
        self.loginButton.clicked.connect(self.openLoginWindows)
        self.regButton.clicked.connect(self.openRegWindows)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog"))
        self.loginButton.setText(_translate("MainDialog", "Авторизация"))
        self.regButton.setText(_translate("MainDialog", "Регистрация"))


    def openLoginWindows(self):
        self.login = Ui_loginDialog()
        self.login.show()
        self.close()

    def openRegWindows(self):
        self.reg = Ui_regDialog()
        self.reg.show()
