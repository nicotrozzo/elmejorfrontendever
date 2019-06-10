import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QLineEdit, QLabel, QComboBox

from filter_ui import Ui_Filter
from frontend_ui import Ui_MainWindow
from input_ui import Ui_Input


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # setear todos los callbacks de botones
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


class DataEntry():
    def __init__(self, line_edit, label):
        self.propertyTitle = label
        self.propertyLineEdit = line_edit
        self.userInputValue = None
        self.onlyNumbers = True
        self.set_only_numbers(self.onlyNumbers)
        self.hide_all()

    def hide_all(self):
        self.propertyLineEdit.hide()
        self.propertyTitle.hide()

    def show_all(self):
        self.propertyLineEdit.show()
        self.propertyTitle.show()

    def update_user_input_value(self):
        self.userInputValue = self.propertyLineEdit.text()

    def get_user_input_value(self):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    dig = uic.loadUi("filter.ui")

    parameters1 = DataEntry(dig.editProperty1, dig.titleProperty1)
    parameters1.set_property_title("Primer cero")

    parameters2 = DataEntry(dig.editProperty2, dig.titleProperty2)
    parameters2.set_property_title("Segundo cero")

    parameters3 = DataEntry(dig.editProperty3, dig.titleProperty3)
    parameters3.hide_all()

    dig.show()
    app.exec()
