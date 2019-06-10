# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Filter(object):
    def setupUi(self, Filter):
        Filter.setObjectName("Filter")
        Filter.resize(727, 528)
        Filter.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Filter)
        self.label.setGeometry(QtCore.QRect(0, 20, 731, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.inputComboBox = QtWidgets.QComboBox(Filter)
        self.inputComboBox.setGeometry(QtCore.QRect(200, 150, 351, 41))
        self.inputComboBox.setObjectName("inputComboBox")
        self.labelInputComboBox = QtWidgets.QLabel(Filter)
        self.labelInputComboBox.setGeometry(QtCore.QRect(90, 120, 161, 20))
        self.labelInputComboBox.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInputComboBox.setObjectName("labelInputComboBox")
        self.label_2 = QtWidgets.QLabel(Filter)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 221, 20))
        self.label_2.setObjectName("label_2")
        self.titleProperty1 = QtWidgets.QLabel(Filter)
        self.titleProperty1.setGeometry(QtCore.QRect(44, 260, 211, 20))
        self.titleProperty1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty1.setObjectName("titleProperty1")
        self.titleProperty2 = QtWidgets.QLabel(Filter)
        self.titleProperty2.setGeometry(QtCore.QRect(44, 310, 211, 20))
        self.titleProperty2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty2.setObjectName("titleProperty2")
        self.titleProperty3 = QtWidgets.QLabel(Filter)
        self.titleProperty3.setGeometry(QtCore.QRect(44, 360, 211, 20))
        self.titleProperty3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty3.setObjectName("titleProperty3")
        self.titleProperty4 = QtWidgets.QLabel(Filter)
        self.titleProperty4.setGeometry(QtCore.QRect(44, 410, 211, 20))
        self.titleProperty4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty4.setObjectName("titleProperty4")
        self.titleProperty5 = QtWidgets.QLabel(Filter)
        self.titleProperty5.setGeometry(QtCore.QRect(44, 460, 211, 20))
        self.titleProperty5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleProperty5.setObjectName("titleProperty5")
        self.editProperty1 = QtWidgets.QLineEdit(Filter)
        self.editProperty1.setGeometry(QtCore.QRect(300, 260, 201, 22))
        self.editProperty1.setText("")
        self.editProperty1.setPlaceholderText("")
        self.editProperty1.setObjectName("editProperty1")
        self.editProperty2 = QtWidgets.QLineEdit(Filter)
        self.editProperty2.setGeometry(QtCore.QRect(300, 310, 201, 22))
        self.editProperty2.setObjectName("editProperty2")
        self.editProperty3 = QtWidgets.QLineEdit(Filter)
        self.editProperty3.setGeometry(QtCore.QRect(300, 360, 201, 22))
        self.editProperty3.setObjectName("editProperty3")
        self.editProperty4 = QtWidgets.QLineEdit(Filter)
        self.editProperty4.setGeometry(QtCore.QRect(300, 410, 201, 22))
        self.editProperty4.setObjectName("editProperty4")
        self.editProperty5 = QtWidgets.QLineEdit(Filter)
        self.editProperty5.setGeometry(QtCore.QRect(300, 460, 201, 22))
        self.editProperty5.setObjectName("editProperty5")
        self.okButton = QtWidgets.QPushButton(Filter)
        self.okButton.setGeometry(QtCore.QRect(580, 430, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setAutoFillBackground(False)
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Filter)
        QtCore.QMetaObject.connectSlotsByName(Filter)

    def retranslateUi(self, Filter):
        _translate = QtCore.QCoreApplication.translate
        Filter.setWindowTitle(_translate("Filter", "Dialog"))
        self.label.setText(_translate("Filter", "<html><head/><body><p><span style=\" color:#ff0000;\">SELECCIÓN DE ENTRADA</span></p></body></html>"))
        self.labelInputComboBox.setText(_translate("Filter", "Seleccione una entrada:"))
        self.label_2.setText(_translate("Filter", "Ingrese las siguientes propiedades:"))
        self.titleProperty1.setText(_translate("Filter", "Título 1"))
        self.titleProperty2.setText(_translate("Filter", "Título 2"))
        self.titleProperty3.setText(_translate("Filter", "Título 3"))
        self.titleProperty4.setText(_translate("Filter", "Título 4"))
        self.titleProperty5.setText(_translate("Filter", "Título 5"))
        self.okButton.setText(_translate("Filter", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Filter = QtWidgets.QDialog()
    ui = Ui_Filter()
    ui.setupUi(Filter)
    Filter.show()
    sys.exit(app.exec_())

