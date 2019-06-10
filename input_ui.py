# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Input(object):
    def setupUi(self, Input):
        Input.setObjectName("Input")
        Input.resize(374, 220)
        self.pushButton = QtWidgets.QPushButton(Input)
        self.pushButton.setGeometry(QtCore.QRect(294, 190, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Input)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 191, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Input)
        self.comboBox.setGeometry(QtCore.QRect(80, 40, 191, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Input)
        QtCore.QMetaObject.connectSlotsByName(Input)

    def retranslateUi(self, Input):
        _translate = QtCore.QCoreApplication.translate
        Input.setWindowTitle(_translate("Input", "Dialog"))
        self.pushButton.setText(_translate("Input", "Ok"))
        self.lineEdit.setText(_translate("Input", "Seleccione la entrada deseada"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Input = QtWidgets.QDialog()
    ui = Ui_Input()
    ui.setupUi(Input)
    Input.show()
    sys.exit(app.exec_())

