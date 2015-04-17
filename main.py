from PyQt4 import uic, QtGui, QtCore

import sys


app = QtGui.QApplication(sys.argv)
window = uic.loadUi("mainform.ui")

window.show()
sys.exit(app.exec())