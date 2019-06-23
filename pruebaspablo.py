import sys
from enum import Enum

from PyQt5 import QtWidgets
from PyQt5.QtGui import QDoubleValidator
import matplotlib as mpl

from filter_ui import Ui_Filter
from frontend_ui import Ui_MainWindow
from input_ui import Ui_Input

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


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


# Class which links a LineEdit with a Label. The Label indicates the property title (Shown as a text next to it)
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
        if accept_only_numbers:
            validator = QDoubleValidator()
            self.propertyLineEdit.setValidator(validator)
        else:
            self.propertyLineEdit.setValidator(None)

    def set_property_title(self, title):
        self.propertyTitle.setText(title)


# Group of a Combo Box and a Label (which shows the title of the Combo Box)
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


class Out:
    @staticmethod
    def return_out():
        a = [10, 20, 30, 40, 75, 95, 120]
        b = [60, -70, 80, 90, 65, 88, 77]
        c = [10, 50, 80, 99, 120, 180, 222, 4000, 84444, 95555, 3333333, 5555555555555]
        d = [20, 45, -88, 100, -151, 174, 188, 555, 800, 1050, 9999, 400]
        e = [20, 20, 85, 85, -40, -280, 252]
        f = [60, -60, 80, -80, 64, 55, 22]
        graphic1 = GraphicProperties("Ceros", "Re", "Im", a, b, GraphicTypes.Zeros)
        graphic2 = GraphicProperties("Polos", "Re", "Im", e, f, GraphicTypes.Poles)
        graphic3 = GraphicProperties("Output", "x", "y", a, f, GraphicTypes.Output)
        graphic4 = GraphicProperties("Bode Phase", "x", "y", c, d, GraphicTypes.BodePhase)
        graphic5 = GraphicProperties("Bode Module", "x", "y", a, b, GraphicTypes.BodeModule)

        graphics = [graphic1, graphic2]

        dict = {
            "Zeros and Poles Diagram": [graphic1, graphic2],
            "Output Signal": [graphic3],
            "Module Bode": [graphic5],
            "Phaee Bode": [graphic4]
        }

        return dict


# Main class of the output window.
class OutputGraphics(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("probandofront.ui", self)
        self.setWindowTitle("Salida")
        self.graphics = None
        self.nextGraphicToShow = None
        self.graphCounter = 0
        self.maxIndex = None
        self.prevGraphicButton.clicked.connect(self.previous_graph)
        self.nextGraphicButton.clicked.connect(self.next_graph)
        self.fetch_graphics_information()
        self.graphButton.clicked.connect(self.graph_button_action)
        self.addToolBar(NavigationToolbar(self.GraphWidget.canvas, self))

    def __graph_button_action__(self):
        self.fetch_graphics_information()
        self.update_graph()

    # Calls a function that returns the values of the graphics to show.
    def __fetch_graphics_information__(self):
        if Out.return_out() is not None:
            self.graphics = None
            self.nextGraphicToShow = None
            self.graphCounter = 0
            self.maxIndex = None
            self.graphics = list(Out.return_out().values())

            if len(self.graphics) == 1:
                self.nextGraphicToShow = self.graphics
                self.prevGraphicButton.hide()
                self.nextGraphicButton.hide()

            else:
                self.maxIndex = len(self.graphics) - 1
                self.prevGraphicButton.show()
                self.nextGraphicButton.show()
                self.nextGraphicToShow = self.graphics[0]
                self.check_counter()

    # Internal usage functions
    def __previous_graph__(self):
        self.graphCounter -= 1
        self.nextGraphicToShow = self.graphics[self.graphCounter]
        self.check_counter()
        self.update_graph()

    def __next_graph__(self):
        self.graphCounter += 1
        self.nextGraphicToShow = self.graphics[self.graphCounter]
        self.check_counter()
        self.update_graph()

    def __check_counter__(self):
        if self.graphCounter == 0:
            self.prevGraphicButton.hide()
        else:
            self.prevGraphicButton.show()

        if self.graphCounter == self.maxIndex:
            self.nextGraphicButton.hide()
        else:
            self.nextGraphicButton.show()

    def __update_graph__(self):

        self.GraphWidget.canvas.axes.clear()

        for graph in self.nextGraphicToShow:
            self.__plot_graph__(graph)

    def __plot_graph__(self, graph):
        self.fix_axes_titles_position(graph)
        if graph.graphicType == GraphicTypes.Output:

            self.GraphWidget.canvas.axes.plot(graph.xValueArray, graph.yValueArray)
            self.GraphWidget.canvas.axes.set_title(graph.title)
            self.GraphWidget.canvas.axes.grid()
            self.GraphWidget.canvas.draw()

        elif graph.graphicType == GraphicTypes.BodeModule or \
                graph.graphicType == GraphicTypes.BodePhase:

            self.GraphWidget.canvas.axes.semilogx(graph.xValueArray,
                                                  graph.yValueArray)
            self.GraphWidget.canvas.axes.set_title(graph.title)
            self.GraphWidget.canvas.axes.grid()
            self.GraphWidget.canvas.draw()

        elif graph.graphicType == GraphicTypes.Zeros:

            self.GraphWidget.canvas.axes.spines['top'].set_color('none')
            self.GraphWidget.canvas.axes.spines['bottom'].set_position('zero')
            self.GraphWidget.canvas.axes.spines['left'].set_position('zero')
            self.GraphWidget.canvas.axes.spines['right'].set_color('none')

            for i in range(len(graph.xValueArray)):
                self.GraphWidget.canvas.axes.plot(graph.xValueArray[i],
                                                  graph.yValueArray[i], color='blue',
                                                  markersize=10, marker='o')

            self.GraphWidget.canvas.axes.set_title("Ceros y Polos")
            self.GraphWidget.canvas.axes.grid()
            self.GraphWidget.canvas.draw()

        elif graph.graphicType == GraphicTypes.Poles:

            self.GraphWidget.canvas.axes.spines['top'].set_color('none')
            self.GraphWidget.canvas.axes.spines['bottom'].set_position('zero')
            self.GraphWidget.canvas.axes.spines['left'].set_position('zero')
            self.GraphWidget.canvas.axes.spines['right'].set_color('none')

            for j in range(len(graph.xValueArray)):
                self.GraphWidget.canvas.axes.plot(graph.xValueArray[j],
                                                  graph.yValueArray[j],
                                                  color='black', markersize=10, marker='x')

            self.GraphWidget.canvas.axes.set_title("Ceros y Polos")
            self.GraphWidget.canvas.axes.grid()
            self.GraphWidget.canvas.draw()

    def __fix_axes_titles_position__(self, graph):
        self.__fix_y_title_position__(graph)
        self.__fix_x_title_position__(graph)

    def __fix_x_title_position__(self, graph):
        ticklabelpad = mpl.rcParams['xtick.major.pad']
        self.GraphWidget.canvas.axes.annotate(graph.xTitle, xy=(1, 0), xytext=(0, -ticklabelpad),
                                              ha='left', va='top',
                                              xycoords='axes fraction', textcoords='offset points')

    def __fix_y_title_position__(self, graph):
        ticklabelpad = mpl.rcParams['ytick.major.pad']
        self.GraphWidget.canvas.axes.annotate(graph.yTitle, xy=(0, 1), xytext=(-50, -ticklabelpad),
                                              ha='left', va='top',
                                              xycoords='axes fraction', textcoords='offset points', rotation=90)


##Class GraphicProperties
# This class is used to unify the properties of the graphs to show.
class GraphicProperties:
    def __init__(self, title, x_title, y_title, x_value_array, y_value_array, graphic_type):
        self.title = title
        self.xValueArray = x_value_array
        self.yValueArray = y_value_array
        self.graphicType = graphic_type
        self.xTitle = x_title
        self.yTitle = y_title


class GraphicTypes(Enum):
    BodeModule = "BodeModule"
    BodePhase = "BodePhase"
    Output = "Output"
    Zeros = "Zeros"
    Poles = "Poles"


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = OutputGraphics()
    window.show()
    app.exec()
