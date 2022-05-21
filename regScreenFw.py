from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from apiClass import apiClass


class Ui_regDialog(QDialog):

    def __init__(self):
        super(Ui_regDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 321)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.regButton = QtWidgets.QPushButton(Dialog)
        self.regButton.setGeometry(QtCore.QRect(50, 270, 151, 41))
        self.regButton.setObjectName("regButton")
        self.regButton.clicked.connect(self.regClick)
        self.userEdit = QtWidgets.QLineEdit(Dialog)
        self.userEdit.setGeometry(QtCore.QRect(30, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userEdit.setFont(font)
        self.userEdit.setObjectName("userEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.loginEdit = QtWidgets.QLineEdit(Dialog)
        self.loginEdit.setGeometry(QtCore.QRect(30, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginEdit.setFont(font)
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.passwordEdit_2.setGeometry(QtCore.QRect(30, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordEdit_2.setFont(font)
        self.passwordEdit_2.setObjectName("passwordEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Регистрация"))
        self.regButton.setText(_translate("Dialog", "Регистрация"))
        self.label_2.setText(_translate("Dialog", "User name"))
        self.label_3.setText(_translate("Dialog", "User"))
        self.label_4.setText(_translate("Dialog", "Password"))

    def regClick(self):
        try:
            api = apiClass()
            body = {
                "username": self.loginEdit.text(),
                "name": self.userEdit.text(),
                "password": self.passwordEdit_2.text()
            }
            api.post('signUp', body)
            self.close()
        except Exception as error:
            print('Error: ' + repr(error))
            QMessageBox.critical(self, "Ошибка ", "Данные не верны", QMessageBox.Ok)
