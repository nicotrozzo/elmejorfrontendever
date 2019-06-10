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
        self.entrance = EntranceDialog()
        self.inputSelectButton.clicked.connect(self.clickedInput)
        self.filterSelectButton.clicked.connect(self.clickedFilter)
        self.outputConfigButton.clicked.connect(self.clickedOutput)

    def clickedInput(self):
        self.entrance.show()

    def clickedFilter(self):
        self.filter

class EntranceDialog(QtWidgets.QDialog, Ui_Input):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)


class FilterDialog(QtWidgets.QDialog, Ui_Filter):
    pass


class OutputDialog(QtWidgets.QDialog, Ui_Output):
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
