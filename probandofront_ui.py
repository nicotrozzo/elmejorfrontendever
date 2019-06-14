# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'probandofront.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 760)
        MainWindow.setStyleSheet("background:rgb(238,238,238)")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputSelectButton.setGeometry(QtCore.QRect(20, 10, 231, 61))
        self.inputSelectButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.inputSelectButton.setObjectName("inputSelectButton")
        self.filterSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.filterSelectButton.setGeometry(QtCore.QRect(280, 10, 241, 61))
        self.filterSelectButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.filterSelectButton.setObjectName("filterSelectButton")
        self.outputConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputConfigButton.setGeometry(QtCore.QRect(550, 10, 241, 61))
        self.outputConfigButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.outputConfigButton.setObjectName("outputConfigButton")
        self.graphicateButton = QtWidgets.QPushButton(self.centralwidget)
        self.graphicateButton.setGeometry(QtCore.QRect(10, 620, 791, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.graphicateButton.setFont(font)
        self.graphicateButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.graphicateButton.setObjectName("graphicateButton")
        self.inputELine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputELine.setGeometry(QtCore.QRect(20, 80, 231, 41))
        self.inputELine.setReadOnly(True)
        self.inputELine.setObjectName("inputELine")
        self.filterELine = QtWidgets.QLineEdit(self.centralwidget)
        self.filterELine.setGeometry(QtCore.QRect(280, 80, 241, 41))
        self.filterELine.setReadOnly(True)
        self.filterELine.setObjectName("filterELine")
        self.outputELine = QtWidgets.QLineEdit(self.centralwidget)
        self.outputELine.setGeometry(QtCore.QRect(550, 80, 241, 41))
        self.outputELine.setDragEnabled(False)
        self.outputELine.setReadOnly(True)
        self.outputELine.setObjectName("outputELine")
        self.GraphWidget = GraphWidget(self.centralwidget)
        self.GraphWidget.setGeometry(QtCore.QRect(60, 140, 691, 461))
        self.GraphWidget.setObjectName("GraphWidget")
        self.nextGraphicButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextGraphicButton.setGeometry(QtCore.QRect(760, 320, 41, 28))
        self.nextGraphicButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.nextGraphicButton.setObjectName("nextGraphicButton")
        self.prevGraphicButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevGraphicButton.setGeometry(QtCore.QRect(10, 330, 41, 28))
        self.prevGraphicButton.setStyleSheet("background: rgb(52,73,85);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;")
        self.prevGraphicButton.setObjectName("prevGraphicButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
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
        self.graphicateButton.setText(_translate("MainWindow", "GRAFICAR"))
        self.nextGraphicButton.setText(_translate("MainWindow", ">"))
        self.prevGraphicButton.setText(_translate("MainWindow", "<"))

from graphwidget import GraphWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

