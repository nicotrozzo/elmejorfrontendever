# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputSelectButton.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.inputSelectButton.setObjectName("inputSelectButton")
        self.filterSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.filterSelectButton.setGeometry(QtCore.QRect(180, 10, 191, 51))
        self.filterSelectButton.setObjectName("filterSelectButton")
        self.outputConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputConfigButton.setGeometry(QtCore.QRect(390, 10, 151, 51))
        self.outputConfigButton.setObjectName("outputConfigButton")
        self.graphicateButton = QtWidgets.QPushButton(self.centralwidget)
        self.graphicateButton.setGeometry(QtCore.QRect(220, 410, 75, 23))
        self.graphicateButton.setObjectName("graphicateButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 100, 531, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.inputELine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputELine.setGeometry(QtCore.QRect(10, 70, 151, 20))
        self.inputELine.setReadOnly(True)
        self.inputELine.setObjectName("inputELine")
        self.filterELine = QtWidgets.QLineEdit(self.centralwidget)
        self.filterELine.setGeometry(QtCore.QRect(180, 70, 191, 20))
        self.filterELine.setReadOnly(True)
        self.filterELine.setObjectName("filterELine")
        self.outputELine = QtWidgets.QLineEdit(self.centralwidget)
        self.outputELine.setGeometry(QtCore.QRect(390, 70, 151, 20))
        self.outputELine.setDragEnabled(False)
        self.outputELine.setReadOnly(True)
        self.outputELine.setObjectName("outputELine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputSelectButton.setText(_translate("MainWindow", "Seleccionar Entrada"))
        self.filterSelectButton.setText(_translate("MainWindow", "Seleccionar Filtro"))
        self.outputConfigButton.setText(_translate("MainWindow", "Configurar Salida"))
        self.graphicateButton.setText(_translate("MainWindow", "Graficar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

