from PyQt5 import QtWidgets
from mainScreenFw import Ui_MainDialog
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Ui_MainDialog()
    application.show()
    sys.exit(app.exec())