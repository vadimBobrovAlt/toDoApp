from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from apiClass import apiClass
from taskCreateScreenFw import Ui_taskCreateDialog


class Ui_taskListDialog(QDialog):

    def __init__(self, token):
        super(Ui_taskListDialog, self).__init__()
        self.setupUi(self)
        self.token = token
        self.loadData()

    def setupUi(self, laskListDialog):
        laskListDialog.setObjectName("laskListDialog")
        laskListDialog.resize(635, 379)
        self.createButton = QtWidgets.QPushButton(laskListDialog)
        self.createButton.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.createTaskClick)
        self.taskListView = QtWidgets.QTableView(laskListDialog)
        self.taskListView.setGeometry(QtCore.QRect(20, 60, 591, 221))
        self.taskListView.setObjectName("taskListView")

        self.retranslateUi(laskListDialog)
        QtCore.QMetaObject.connectSlotsByName(laskListDialog)

    def retranslateUi(self, laskListDialog):
        _translate = QtCore.QCoreApplication.translate
        laskListDialog.setWindowTitle(_translate("laskListDialog", "Dialog"))
        self.createButton.setText(_translate("laskListDialog", "Создать задачу"))

    def loadData(self):
        try:
            print(self.token)
            api = apiClass()
            res = api.get("tasks", self.token)
            data = res.get('tasks')

            resData = list()
            resData.append(["ID", "Заголовок", "Описание"])
            for val in data:
                resData.append(self.__item_constructor(val))

            self.model = TableModel(resData)
            self.taskListView.setModel(self.model)

        except Exception as error:
            print('Error: ' + repr(error))
            QMessageBox.critical(self, "Ошибка ", "Прав доступа недостаточно", QMessageBox.Ok)

    def createTaskClick(self):
        self.taskList = Ui_taskCreateDialog(self.token)
        self.taskList.show()
        self.close()

    def __item_constructor(self, item):
        return [item.get('id'), item.get('title'), item.get('description')]


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
