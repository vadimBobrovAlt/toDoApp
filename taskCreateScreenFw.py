from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from apiClass import apiClass



class Ui_taskCreateDialog(QDialog):

    def __init__(self, token):
        super(Ui_taskCreateDialog, self).__init__()
        self.setupUi(self)
        self.token = token

    def setupUi(self, taskCreateDialog):
        taskCreateDialog.setObjectName("taskCreateDialog")
        taskCreateDialog.resize(348, 315)
        self.createButton = QtWidgets.QPushButton(taskCreateDialog)
        self.createButton.setGeometry(QtCore.QRect(100, 260, 151, 41))
        self.createButton.clicked.connect(self.createTaskClick)
        self.createButton.setObjectName("createButton")
        self.label_2 = QtWidgets.QLabel(taskCreateDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(taskCreateDialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.titleEdit = QtWidgets.QLineEdit(taskCreateDialog)
        self.titleEdit.setGeometry(QtCore.QRect(30, 80, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titleEdit.setFont(font)
        self.titleEdit.setObjectName("titleEdit")
        self.label_3 = QtWidgets.QLabel(taskCreateDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.label_3.setObjectName("label_3")
        self.descriptionEdit = QtWidgets.QTextEdit(taskCreateDialog)
        self.descriptionEdit.setGeometry(QtCore.QRect(30, 150, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descriptionEdit.setFont(font)
        self.descriptionEdit.setObjectName("descriptionEdit")

        self.retranslateUi(taskCreateDialog)
        QtCore.QMetaObject.connectSlotsByName(taskCreateDialog)

    def retranslateUi(self, taskCreateDialog):
        _translate = QtCore.QCoreApplication.translate
        taskCreateDialog.setWindowTitle(_translate("taskCreateDialog", "Dialog"))
        self.createButton.setText(_translate("taskCreateDialog", "Создать"))
        self.label_2.setText(_translate("taskCreateDialog", "Title"))
        self.label.setText(_translate("taskCreateDialog", "Создание задачи"))
        self.label_3.setText(_translate("taskCreateDialog", "Description"))

    def createTaskClick(self):
        try:
            api = apiClass()
            body = {"title": self.titleEdit.text(), "description": self.descriptionEdit.toPlainText()}
            data = api.post('tasks', body, self.token)
            print(data)

            from taskListScreenFw import Ui_taskListDialog
            self.taskList = Ui_taskListDialog(self.token)
            self.taskList.show()
            self.close()
        except Exception as error:
            print('Error: ' + repr(error))
            QMessageBox.critical(self, "Ошибка ", "Данные не корректны", QMessageBox.Ok)
