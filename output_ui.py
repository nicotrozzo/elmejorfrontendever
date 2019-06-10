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
        Output.resize(400, 300)
        self.okButton = QtWidgets.QPushButton(Output)
        self.okButton.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Output)
        QtCore.QMetaObject.connectSlotsByName(Output)

    def retranslateUi(self, Output):
        _translate = QtCore.QCoreApplication.translate
        Output.setWindowTitle(_translate("Output", "Dialog"))
        self.okButton.setText(_translate("Output", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Output = QtWidgets.QDialog()
    ui = Ui_Output()
    ui.setupUi(Output)
    Output.show()
    sys.exit(app.exec_())

