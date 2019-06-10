from frontend_ui import *
from input_ui import *
from filter_ui import *
from output_ui import *
from backend import *
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QLineEdit, QLabel
from pruebaspablo import DataEntry, DataEntryCombo
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, backend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #setear todos los callbacks de botones
        self.backend = backend
        self.inputWindow = InputDialog(self, backend.signals())
        self.filterWindow = FilterDialog(self, backend.filters())
        self.outputWindow = OutputDialog(self, backend.outputconfig())
        self.inputSelectButton.clicked.connect(self.clicked_input)
        self.filterSelectButton.clicked.connect(self.clicked_filter)
        self.outputConfigButton.clicked.connect(self.clicked_output)
        self.graphicateButton.clicked.connect(self.graphicate)

    def clicked_input(self):
        self.inputWindow.show()

    def clicked_filter(self):
        self.filterWindow.show()

    def clicked_output(self):
        self.outputWindow.show()

    def graphicate(self):
        pass
        #x,y,z = backend.simulate(inputWindow.get_data(), filterWindow.get_data(), outputWindow.get_data())

    # éste metodo lo llaman los cuadros de diálogo cuando terminan, la idea es actualizar los line edits con la nueva informacion
    def update(self):
        self.inputELine.setText(self.inputWindow.get_selected_input())
        self.filterELine.setText(self.filterWindow.get_selected_filter())
        self.outputELine.setText(self.outputWindow.get_selected_output())


# clase base de los cuadros de dialogo de input, filter y output. Al apretarse el boton de Ok se ocultan y le avisan
# a la main window que hubo un cambio (algo asi como MVC)
class AbstractDialog(QtWidgets.QDialog):
    def __init__(self, main_window, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okButton.clicked.connect(self.finished_selecting)
        self.mainWindow = main_window


class InputDialog(AbstractDialog, Ui_Input):
    def __init__(self, all_signals, main_window, *args, **kwargs):
        AbstractDialog.__init__(self, main_window, *args, **kwargs)
        self.okButton.clicked.connect(self.finished_selecting)
        self.dataentries = []
        self.dataentries.append(DataEntry(self.editProperty1, self.titleProperty1))
        self.dataentries.append(DataEntry(self.editProperty2, self.titleProperty2))
        self.dataentries.append(DataEntry(self.editProperty3, self.titleProperty3))
        self.dataentries.append(DataEntry(self.editProperty4, self.titleProperty4))
        self.dataentries.append(DataEntry(self.editProperty5, self.titleProperty5))
        for sig in all_signals:
            self.inputComboBox.addItem(sig.name().upper())         #agrega todas las señales al menu desplegable
        self.signals = all_signals
        self.inputComboBox.currentIndexChanged.connect(self.showCurrentProperties)
        self.showCurrentProperties()
        self.done = False

    def showCurrentProperties(self):
        for x in self.dataentries:
            x.hide_all()
        for sig in self.signals:
            if sig.name().lower() == self.inputComboBox.currentText().lower():
                i = 0
                for key in sig.properties():
                    self.dataentries[i].show_all()
                    self.dataentries[i].set_property_title(key)
                    i += 1
                break

    def finished_selecting(self):
        for sig in self.signals:
            if sig.name().lower() == self.inputComboBox.currentText().lower():
                i = 0
                for key in sig.properties():
                    sig.properties[key] = self.dataentries[i].getUserInputValue()
                    i += 1
                if sig.validate():
                    self.hide()
                    self.mainWindow.update()
                    self.done = True
                    break
                else:
                    self.dataentries[i].error()

    #devuelve las properties del elemento seleccionado
    def get_data(self):
        ret = {}
        for sig in self.signals:
            if sig.name().lower() == self.inputComboBox.currentText().lower():
                ret = sig.properties()
                break
        return ret

    def get_selected_input(self):
        ret = ""
        if self.done:
            for sig in self.signals:
                if sig.name().lower() == self.inputComboBox.currentText().lower():
                    ret = sig.name()
                    break
        return ret

class FilterDialog(AbstractDialog, Ui_Filter):
    def __init__(self, all_filters, main_window, *args, **kwargs):
        AbstractDialog.__init__(self, main_window, *args, **kwargs)
        self.okButton.clicked.connect(self.finished_selecting)
        self.dataentries.append(DataEntry(self.editProperty1, self.titleProperty1))
        self.dataentries.append(DataEntry(self.editProperty2, self.titleProperty2))
        self.dataentries.append(DataEntry(self.editProperty3, self.titleProperty3))
        self.dataentries.append(DataEntry(self.editProperty4, self.titleProperty4))
        self.dataentries.append(DataEntry(self.editProperty5, self.titleProperty5))
        self.filters = all_filters
        for fil in all_filters:
            self.filterComboBox.addItem(fil.name().upper())         #agrega todos los filtros al menu desplegable
        self.filterComboBox.currentIndexChanged.connect(self.showCurrentProperties)
        self.showCurrentProperties()
        self.done = False

    def showCurrentProperties(self):
        for x in self.dataentries:
            x.hide_all()
        for fil in self.filters:
            if fil.name().lower() == self.filterComboBox.currentText().lower():
                i = 0
                for key in fil.properties():
                    self.dataentries[i].show_all()
                    self.dataentries[i].set_property_title(key)
                    i += 1
                break

    def finished_selecting(self):
        for fil in self.filters:
            if fil.name().lower() == self.filterComboBox.currentText().lower():
                i = 0
                for key in fil.properties():
                    fil.properties[key] = self.dataentries[i].getUserInputValue()
                    i += 1
                if fil.validate():
                    self.hide()
                    self.mainWindow.update()
                    break
                else:
                    self.dataentries[i].error()

    # devuelve las properties del elemento seleccionado
    def get_data(self):
        ret = {}
        for fil in self.filters:
            if fil.name().lower() == self.filterComboBox.currentText().lower():
                ret = fil.properties()
                break
        return ret

    def get_selected_filter(self):
        ret = ""
        if self.done:
            for fil in self.filters:
                if fil.name().lower() == self.filterComboBox.currentText().lower():
                    ret = fil.name()
                    break
        return ret

class OutputDialog(AbstractDialog, Ui_Output):
    def __init__(self, all_outputs, main_window, *args, **kwargs):
        AbstractDialog.__init__(self, main_window, *args, **kwargs)
        self.okButton.clicked.connect(self.finished_selecting)
        self.dataentries.append(DataEntryCombo(self.comboProperty1, self.titleProperty1))
        self.dataentries.append(DataEntryCombo(self.comboProperty2, self.titleProperty2))
        self.dataentries.append(DataEntryCombo(self.comboProperty3, self.titleProperty3))
        self.dataentries.append(DataEntryCombo(self.comboProperty4, self.titleProperty4))
        for out in all_outputs:
            self.outputComboBox.addItem(out.name().upper())         #agrega todas las señales al menu desplegable
        self.outputs = all_outputs
        self.outputComboBox.currentIndexChanged.connect(self.showCurrentProperties)
        self.showCurrentProperties()

    def showCurrentProperties(self):
        for x in self.dataentries:
            x.hide_all()
        for out in self.outputs:
            if out.name().lower() == self.outputComboBox.currentText().lower():
                i = 0
                for key in out.properties():
                    self.dataentries[i].show_all()
                    self.dataentries[i].set_property_title(key)
                    i += 1

    def finished_selecting(self):
        for out in self.outputs:
            if out.name().lower() == self.signalComboBox.currentText().lower():
                i = 0
                for key in out.properties():
                    out.properties[key] = self.dataentries[i].getUserInputValue()
                    i += 1
                if out.validate():
                    self.hide()
                    self.mainWindow.update()
                    break
                else:
                    self.dataentries[i].error()

    #devuelve las properties del elemento seleccionado
    def get_data(self):
        ret = {}
        for out in self.outputs:
            if out.name().lower() == self.outputComboBox.currentText().lower():
                ret = out.properties()
                break
        return ret

    def get_selected_output(self):
        ret = ""
        if self.done:
            for out in self.outputs:
                if out.name().lower() == self.outputComboBox.currentText().lower():
                    ret = out.name()
                    break
        return ret


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    signals = [Signal("senodete"), Signal("escalon")]
    filters = [Filter("filtro1"), Filter("Filtro2")]
    outputs = [OutputConfig("chau")]
    back = BackEnd(signals, filters, outputs)
    window = MainWindow(back)
    window.show()
    sys.exit(app.exec_())
