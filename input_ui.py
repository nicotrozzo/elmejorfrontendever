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
        Input.resize(727, 528)
        Input.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Input)
        self.label.setGeometry(QtCore.QRect(0, 20, 731, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.inputComboBox = QtWidgets.QComboBox(Input)
        self.inputComboBox.setGeometry(QtCore.QRect(200, 150, 351, 41))
        self.inputComboBox.setObjectName("inputComboBox")
        self.labelInputComboBox = QtWidgets.QLabel(Input)
        self.labelInputComboBox.setGeometry(QtCore.QRect(90, 120, 161, 20))
        self.labelInputComboBox.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInputComboBox.setObjectName("labelInputComboBox")
        self.label_2 = QtWidgets.QLabel(Input)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 221, 20))
        self.label_2.setObjectName("label_2")
        self.titleProperty1 = QtWidgets.QLabel(Input)
        self.titleProperty1.setGeometry(QtCore.QRect(44, 260, 211, 20))
        self.titleProperty1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty1.setObjectName("titleProperty1")
        self.titleProperty2 = QtWidgets.QLabel(Input)
        self.titleProperty2.setGeometry(QtCore.QRect(44, 310, 211, 20))
        self.titleProperty2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty2.setObjectName("titleProperty2")
        self.titleProperty3 = QtWidgets.QLabel(Input)
        self.titleProperty3.setGeometry(QtCore.QRect(44, 360, 211, 20))
        self.titleProperty3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty3.setObjectName("titleProperty3")
        self.titleProperty4 = QtWidgets.QLabel(Input)
        self.titleProperty4.setGeometry(QtCore.QRect(44, 410, 211, 20))
        self.titleProperty4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty4.setObjectName("titleProperty4")
        self.titleProperty5 = QtWidgets.QLabel(Input)
        self.titleProperty5.setGeometry(QtCore.QRect(44, 460, 211, 20))
        self.titleProperty5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty5.setObjectName("titleProperty5")
        self.editProperty1 = QtWidgets.QLineEdit(Input)
        self.editProperty1.setGeometry(QtCore.QRect(300, 260, 201, 22))
        self.editProperty1.setText("")
        self.editProperty1.setPlaceholderText("")
        self.editProperty1.setObjectName("editProperty1")
        self.editProperty2 = QtWidgets.QLineEdit(Input)
        self.editProperty2.setGeometry(QtCore.QRect(300, 310, 201, 22))
        self.editProperty2.setObjectName("editProperty2")
        self.editProperty3 = QtWidgets.QLineEdit(Input)
        self.editProperty3.setGeometry(QtCore.QRect(300, 360, 201, 22))
        self.editProperty3.setObjectName("editProperty3")
        self.editProperty4 = QtWidgets.QLineEdit(Input)
        self.editProperty4.setGeometry(QtCore.QRect(300, 410, 201, 22))
        self.editProperty4.setObjectName("editProperty4")
        self.editProperty5 = QtWidgets.QLineEdit(Input)
        self.editProperty5.setGeometry(QtCore.QRect(300, 460, 201, 22))
        self.editProperty5.setObjectName("editProperty5")
        self.okButton = QtWidgets.QPushButton(Input)
        self.okButton.setGeometry(QtCore.QRect(580, 430, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setAutoFillBackground(False)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Input)
        QtCore.QMetaObject.connectSlotsByName(Input)

    def retranslateUi(self, Input):
        _translate = QtCore.QCoreApplication.translate
        Input.setWindowTitle(_translate("Input", "Dialog"))
        self.label.setText(_translate("Input", "<html><head/><body><p><span style=\" color:#ff0000;\">SELECCIÓN DE ENTRADA</span></p></body></html>"))
        self.labelInputComboBox.setText(_translate("Input", "Seleccione una entrada:"))
        self.label_2.setText(_translate("Input", "Ingrese las siguientes propiedades:"))
        self.titleProperty1.setText(_translate("Input", "Título 1"))
        self.titleProperty2.setText(_translate("Input", "Título 2"))
        self.titleProperty3.setText(_translate("Input", "Título 3"))
        self.titleProperty4.setText(_translate("Input", "Título 4"))
        self.titleProperty5.setText(_translate("Input", "Título 5"))
        self.okButton.setText(_translate("Input", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Input = QtWidgets.QDialog()
    ui = Ui_Input()
    ui.setupUi(Input)
    Input.show()
    sys.exit(app.exec_())

