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
        Filter.resize(400, 300)
        self.okButton = QtWidgets.QPushButton(Filter)
        self.okButton.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Filter)
        QtCore.QMetaObject.connectSlotsByName(Filter)

    def retranslateUi(self, Filter):
        _translate = QtCore.QCoreApplication.translate
        Filter.setWindowTitle(_translate("Filter", "Dialog"))
        self.okButton.setText(_translate("Filter", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Filter = QtWidgets.QDialog()
    ui = Ui_Filter()
    ui.setupUi(Filter)
    Filter.show()
    sys.exit(app.exec_())

