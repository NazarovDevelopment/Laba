import mainform as mf
from PyQt4 import QtCore, QtGui
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = mf.Ui_mainform()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()

    import LoadNiceFile
    data = LoadNiceFile.loadfile("si.lvm")

    window.ui.matplotlibwidget
    sys.exit(app.exec_())