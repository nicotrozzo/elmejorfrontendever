# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Filter(object):
    def setupUi(self, Filter):
        Filter.setObjectName("Filter")
        Filter.resize(907, 688)
        Filter.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Filter)
        self.label.setGeometry(QtCore.QRect(270, 40, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.filterComboBox = QtWidgets.QComboBox(Filter)
        self.filterComboBox.setGeometry(QtCore.QRect(280, 160, 351, 41))
        self.filterComboBox.setObjectName("filterComboBox")
        self.labelFilterComboBox = QtWidgets.QLabel(Filter)
        self.labelFilterComboBox.setGeometry(QtCore.QRect(280, 170, 351, 20))
        self.labelFilterComboBox.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFilterComboBox.setObjectName("labelFilterComboBox")
        self.label_2 = QtWidgets.QLabel(Filter)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 221, 20))
        self.label_2.setObjectName("label_2")
        self.titleProperty1 = QtWidgets.QLabel(Filter)
        self.titleProperty1.setGeometry(QtCore.QRect(290, 310, 55, 16))
        self.titleProperty1.setObjectName("titleProperty1")
        self.titleProperty2 = QtWidgets.QLabel(Filter)
        self.titleProperty2.setGeometry(QtCore.QRect(290, 360, 55, 16))
        self.titleProperty2.setObjectName("titleProperty2")
        self.titleProperty3 = QtWidgets.QLabel(Filter)
        self.titleProperty3.setGeometry(QtCore.QRect(290, 410, 55, 16))
        self.titleProperty3.setObjectName("titleProperty3")
        self.titleProperty4 = QtWidgets.QLabel(Filter)
        self.titleProperty4.setGeometry(QtCore.QRect(290, 460, 55, 16))
        self.titleProperty4.setObjectName("titleProperty4")
        self.titleProperty5 = QtWidgets.QLabel(Filter)
        self.titleProperty5.setGeometry(QtCore.QRect(290, 510, 55, 16))
        self.titleProperty5.setObjectName("titleProperty5")
        self.editProperty1 = QtWidgets.QLineEdit(Filter)
        self.editProperty1.setGeometry(QtCore.QRect(390, 310, 201, 22))
        self.editProperty1.setPlaceholderText("")
        self.editProperty1.setObjectName("editProperty1")
        self.editProperty2 = QtWidgets.QLineEdit(Filter)
        self.editProperty2.setGeometry(QtCore.QRect(390, 360, 201, 22))
        self.editProperty2.setObjectName("editProperty2")
        self.editProperty3 = QtWidgets.QLineEdit(Filter)
        self.editProperty3.setGeometry(QtCore.QRect(390, 410, 201, 22))
        self.editProperty3.setObjectName("editProperty3")
        self.editProperty4 = QtWidgets.QLineEdit(Filter)
        self.editProperty4.setGeometry(QtCore.QRect(390, 460, 201, 22))
        self.editProperty4.setObjectName("editProperty4")
        self.editProperty5 = QtWidgets.QLineEdit(Filter)
        self.editProperty5.setGeometry(QtCore.QRect(390, 510, 201, 22))
        self.editProperty5.setObjectName("editProperty5")
        self.okButton = QtWidgets.QPushButton(Filter)
        self.okButton.setGeometry(QtCore.QRect(710, 570, 131, 81))
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
        self.label.setText(_translate("Filter", "<font color=\'red\'>SELECCIÓN DE FILTRO</font>"))
        self.labelFilterComboBox.setText(_translate("Filter", "Seleccione un filtro"))
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

