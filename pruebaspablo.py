from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

app = QtWidgets.QApplication([])
dig = uic.loadUi("filter.ui")

validator = QDoubleValidator(0, 100, 2)
dig.editProperty1.setValidator(validator)

dig.editProperty1.hide()


dig.show()
app.exec()