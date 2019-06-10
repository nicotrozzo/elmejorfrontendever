from frontend_ui import *
from input_ui import *
from filter_ui import *
from output_ui import *
from backend import *
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, backend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #setear todos los callbacks de botones
        self.inputWindow = InputDialog(self, backend.signals)        #agregar , backend.signals
        self.filterWindow = FilterDialog(self, backend.filters)      #agregar, backend.filters
        self.outputWindow = OutputDialog(self, backend.outputconfig)      #agregar, backend.outputconfig
        self.inputSelectButton.clicked.connect(self.clicked_input)
        self.filterSelectButton.clicked.connect(self.clicked_filter)
        self.outputConfigButton.clicked.connect(self.clicked_output)

    def clicked_input(self):
        self.inputWindow.show()

    def clicked_filter(self):
        self.filterWindow.show()

    def clicked_output(self):
        self.outputWindow.show()

    #éste metodo lo llaman los cuadros de diálogo cuando terminan, la idea es actualizar los line edits con la nueva informacion
    def update(self):
        print("ANDA EL UPDATE")


# clase base de los cuadros de dialogo de input, filter y output. Al apretarse el boton de Ok se ocultan y le avisan
# a la main window que hubo un cambio (algo asi como MVC)
class AbstractDialog(QtWidgets.QDialog):
    def __init__(self, main_window, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okButton.clicked.connect(self.finished_selecting)
        self.mainWindow = main_window
        self.selection =

    def finished_selecting(self):
        self.hide()
        self.mainWindow.update()

    def get_data(self):
        return self.

class InputDialog(AbstractDialog, Ui_Input):
    def __init__(self, all_signals, main_window, *args, **kwargs):
        AbstractDialog.__init__(self, main_window, *args, **kwargs)
        self.dataentries.append(DataEntry())

        #dataentry

        self.signals = all_signals
        for sig in all_signals:                 #cada sig es una señal distinta que se puede tener como input
            self.signalComboBox.addItem(sig.name())
            for key in sig.properties:
                self.



class FilterDialog(AbstractDialog, Ui_Filter):
    pass

class OutputDialog(AbstractDialog, Ui_Output):
    pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
