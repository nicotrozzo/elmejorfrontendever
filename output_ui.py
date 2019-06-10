# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Output(object):
    def setupUi(self, Output):
        Output.setObjectName("Output")
        Output.resize(727, 529)
        Output.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Output)
        self.label.setGeometry(QtCore.QRect(0, 20, 721, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.outputComboBox = QtWidgets.QComboBox(Output)
        self.outputComboBox.setGeometry(QtCore.QRect(210, 170, 351, 41))
        self.outputComboBox.setObjectName("outputComboBox")
        self.labelOutputComboBox = QtWidgets.QLabel(Output)
        self.labelOutputComboBox.setGeometry(QtCore.QRect(40, 130, 221, 20))
        self.labelOutputComboBox.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutputComboBox.setObjectName("labelOutputComboBox")
        self.label_2 = QtWidgets.QLabel(Output)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 221, 20))
        self.label_2.setObjectName("label_2")
        self.titleProperty1 = QtWidgets.QLabel(Output)
        self.titleProperty1.setGeometry(QtCore.QRect(64, 290, 211, 20))
        self.titleProperty1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty1.setObjectName("titleProperty1")
        self.titleProperty2 = QtWidgets.QLabel(Output)
        self.titleProperty2.setGeometry(QtCore.QRect(64, 340, 211, 20))
        self.titleProperty2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty2.setObjectName("titleProperty2")
        self.titleProperty3 = QtWidgets.QLabel(Output)
        self.titleProperty3.setGeometry(QtCore.QRect(64, 390, 211, 20))
        self.titleProperty3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty3.setObjectName("titleProperty3")
        self.titleProperty4 = QtWidgets.QLabel(Output)
        self.titleProperty4.setGeometry(QtCore.QRect(64, 440, 211, 20))
        self.titleProperty4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty4.setObjectName("titleProperty4")
        self.okButton = QtWidgets.QPushButton(Output)
        self.okButton.setGeometry(QtCore.QRect(590, 440, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setAutoFillBackground(False)
        self.okButton.setObjectName("okButton")
        self.comboProperty1 = QtWidgets.QComboBox(Output)
        self.comboProperty1.setGeometry(QtCore.QRect(330, 290, 151, 22))
        self.comboProperty1.setObjectName("comboProperty1")
        self.comboProperty2 = QtWidgets.QComboBox(Output)
        self.comboProperty2.setGeometry(QtCore.QRect(330, 340, 151, 22))
        self.comboProperty2.setObjectName("comboProperty2")
        self.comboProperty3 = QtWidgets.QComboBox(Output)
        self.comboProperty3.setGeometry(QtCore.QRect(330, 390, 151, 22))
        self.comboProperty3.setObjectName("comboProperty3")
        self.comboProperty4 = QtWidgets.QComboBox(Output)
        self.comboProperty4.setGeometry(QtCore.QRect(330, 440, 151, 22))
        self.comboProperty4.setObjectName("comboProperty4")

        self.retranslateUi(Output)
        QtCore.QMetaObject.connectSlotsByName(Output)

    def retranslateUi(self, Output):
        _translate = QtCore.QCoreApplication.translate
        Output.setWindowTitle(_translate("Output", "Dialog"))
        self.label.setText(_translate("Output", "<html><head/><body><p><span style=\" color:#ff0000;\">SELECCIÓN DE SALIDA</span></p></body></html>"))
        self.labelOutputComboBox.setText(_translate("Output", "Seleccione un formato para la salida:"))
        self.label_2.setText(_translate("Output", "Ingrese las siguientes propiedades:"))
        self.titleProperty1.setText(_translate("Output", "Título 1"))
        self.titleProperty2.setText(_translate("Output", "Título 2"))
        self.titleProperty3.setText(_translate("Output", "Título 3"))
        self.titleProperty4.setText(_translate("Output", "Título 4"))
        self.okButton.setText(_translate("Output", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Output = QtWidgets.QDialog()
    ui = Ui_Output()
    ui.setupUi(Output)
    Output.show()
    sys.exit(app.exec_())

