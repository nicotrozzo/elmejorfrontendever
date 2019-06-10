# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Entrada(object):
    def setupUi(self, Entrada):
        Entrada.setObjectName("Entrada")
        Entrada.resize(374, 220)
        self.pushButton = QtWidgets.QPushButton(Entrada)
        self.pushButton.setGeometry(QtCore.QRect(294, 190, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Entrada)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 191, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Entrada)
        self.comboBox.setGeometry(QtCore.QRect(80, 40, 191, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Entrada)
        QtCore.QMetaObject.connectSlotsByName(Entrada)

    def retranslateUi(self, Entrada):
        _translate = QtCore.QCoreApplication.translate
        Entrada.setWindowTitle(_translate("Entrada", "Dialog"))
        self.pushButton.setText(_translate("Entrada", "Ok"))
        self.lineEdit.setText(_translate("Entrada", "Seleccione la entrada deseada"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Entrada = QtWidgets.QDialog()
    ui = Ui_Entrada()
    ui.setupUi(Entrada)
    Entrada.show()
    sys.exit(app.exec_())

