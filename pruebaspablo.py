import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QLineEdit, QLabel, QComboBox, QMainWindow
from PyQt5.uic import loadUi
from matplotlib.ticker import MaxNLocator

from filter_ui import Ui_Filter
from frontend_ui import Ui_MainWindow
from input_ui import Ui_Input

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # setear todos los callbacks de botones
        self.entrance = EntranceDialog()
        self.inputSelectButton.clicked.connect(self.clicked_input)
        self.filterSelectButton.clicked.connect(self.clickedFilter)
        self.outputConfigButton.clicked.connect(self.clickedOutput)

    def clicked_input(self):
        self.entrance.show()

    def clicked_filter(self):
        self.filter


class EntranceDialog(QtWidgets.QDialog, Ui_Input):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)


class FilterDialog(QtWidgets.QDialog, Ui_Filter):
    pass


# Grupo de un LineEdit y un label (el titulo de la propiedad)
class DataEntry:
    def __init__(self, line_edit, label):
        self.propertyTitle = label
        self.propertyLineEdit = line_edit
        self.userInputValue = None
        self.onlyNumbers = True
        self.set_only_numbers(self.onlyNumbers)
        self.hide_all()
        self.isHidden = True
        self.inError = False
        self.errorStyleSheet = "QLineEdit { background: rgb(255, 0, 0); selection-background-color: rgb(255, 0, 0); }"
        self.normalStyleSheet = "QLineEdit { background: rgb(255, 255, 255); selection-background-color: rgb(255, " \
                                "255, 255); } "
        self.propertyLineEdit.textChanged.connect(self.normal_style)

    def error_detected(self):
        self.propertyLineEdit.setStyleSheet(self.errorStyleSheet)
        self.inError = True

    def normal_style(self):
        if self.inError:
            self.propertyLineEdit.setStyleSheet(self.normalStyleSheet)
            self.inError = False

    def delete_text(self):
        self.propertyLineEdit.setText("")

    def hide_all(self):
        self.propertyLineEdit.hide()
        self.propertyTitle.hide()
        self.isHidden = True
        self.delete_text()

    def show_all(self):
        self.propertyLineEdit.show()
        self.propertyTitle.show()
        self.isHidden = False

    def is_hidden(self):
        return self.isHidden

    def update_user_input_value(self):
        self.userInputValue = self.propertyLineEdit.text()

    def get_user_input_value(self):
        self.update_user_input_value()
        return self.userInputValue

    def set_only_numbers(self, accept_only_numbers):
        self.onlyNumbers = accept_only_numbers
        if accept_only_numbers:
            validator = QDoubleValidator()
            self.propertyLineEdit.setValidator(validator)
        else:
            self.propertyLineEdit.setValidator(None)

    def set_property_title(self, title):
        self.propertyTitle.setText(title)


# Grupo de un Combo Box y un label (el titulo de la propiedad)
class DataEntryCombo:
    def __init__(self, combo_box, label):
        self.propertyTitle = label
        self.propertyComboBox = combo_box
        self.propertyValue = self.propertyComboBox.currentText()
        self.hide_all()
        self.isHidden = True

    def hide_all(self):
        self.propertyComboBox.hide()
        self.propertyTitle.hide()
        self.isHidden = True

    def show_all(self):
        self.propertyComboBox.show()
        self.propertyTitle.show()
        self.isHidden = False

    def is_hidden(self):
        return self.isHidden

    def update_property_value(self):
        self.propertyValue = self.propertyComboBox.currentText()

    def get_property_value(self):
        self.update_property_value()
        return self.propertyValue

    def set_property_title(self, title):
        self.propertyTitle.setText(title)


class OutputGraphics(QMainWindow):

    def __init__(self, x_values, y_values, x_title, y_title):
        QMainWindow.__init__(self)
        loadUi("probandofront.ui", self)

        self.setWindowTitle("Salida")
        self.xTitle = x_title
        self.yTitle = y_title
        self.xValues = x_values
        self.yValues = y_values
        self.graphicateButton.clicked.connect(self.update_graph)
        self.addToolBar(NavigationToolbar(self.GraphWidget.canvas, self))

    def update_graph(self):
        self.GraphWidget.canvas.axes.clear()
        self.GraphWidget.canvas.axes.plot(self.xValues, self.yValues)
        self.GraphWidget.canvas.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.GraphWidget.canvas.axes.set_xlabel(self.xTitle)
        self.GraphWidget.canvas.axes.set_ylabel(self.yTitle)
        self.GraphWidget.canvas.axes.set_title('Señal de salida')
        self.GraphWidget.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    a = [10, 20, 30, 40, 75, 95, 120]
    b = [60, 70, 80, 90, 65, 88, 77]
    window = OutputGraphics(a, b, 'Valores x', 'Valores y')
    window.show()
    app.exec()

