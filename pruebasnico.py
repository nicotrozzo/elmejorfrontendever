from frontend_ui import *
from input_ui import *
from filter_ui import *
from output_ui import *
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #setear todos los callbacks de botones
        self.inputWindow = InputDialog(self)
        self.filterWindow = FilterDialog(self)
        self.outputWindow = OutputDialog(self)
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


class InputDialog(QtWidgets.QDialog, Ui_Input):
    def __init__(self, main_window, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okButton.clicked.connect(self.finished_selecting)
        self.mainWindow = main_window

    def finished_selecting(self):
        self.hide()
        self.mainWindow.update()

    def


class FilterDialog(QtWidgets.QDialog, Ui_Filter):
    def __init__(self, main_window, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okButton.clicked.connect(self.finished_selecting)
        self.mainWindow = main_window

    def finished_selecting(self):
        self.hide()
        self.mainWindow.update()


class OutputDialog(QtWidgets.QDialog, Ui_Output):
    def __init__(self, main_window, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okButton.clicked.connect(self.finished_selecting)
        self.mainWindow = main_window

    def finished_selecting(self):
        self.hide()
        self.mainWindow.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
