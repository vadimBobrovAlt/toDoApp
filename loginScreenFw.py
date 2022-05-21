from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from apiClass import apiClass
from taskListScreenFw import Ui_taskListDialog

class Ui_loginDialog(QDialog):

    def __init__(self):
        super(Ui_loginDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 269)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(50, 210, 151, 41))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.loginClick)
        self.loginEdit = QtWidgets.QLineEdit(Dialog)
        self.loginEdit.setGeometry(QtCore.QRect(30, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginEdit.setFont(font)
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordEdit.setGeometry(QtCore.QRect(30, 150, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setObjectName("passwordEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 135, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginButton.setText(_translate("Dialog", "Авторизация"))
        self.label.setText(_translate("Dialog", "Авторизация"))
        self.label_2.setText(_translate("Dialog", "User name"))
        self.label_3.setText(_translate("Dialog", "Password"))

    def loginClick(self):
        try:
            api = apiClass()
            body = {"username": self.loginEdit.text(), "password": self.passwordEdit.text()}
            res = api.post('login',body)
            token = res.get('access_token')
            self.taskList = Ui_taskListDialog(token)
            self.taskList.show()
            self.close()
        except Exception as error:
            print('Error: ' + repr(error))
            QMessageBox.critical(self, "Ошибка ", "Данные не верны", QMessageBox.Ok)
