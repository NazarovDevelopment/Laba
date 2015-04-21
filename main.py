import mainform as mf
from PyQt4 import QtCore, QtGui

import matplotlib.pyplot as plt
import matplotlib

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = mf.Ui_mainform()
        self.ui.matplotlibwidget.figure = plt.figure()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.DrawPlot)

    def DrawPlot(self):
        import LoadNiceFile
        MyData = LoadNiceFile.loadfile("si.lvm")

        ax = self.ui.matplotlibwidget.figure.add_subplot(111)
        ax.plot

        self.ui.matplotlibwidget.figure.draw()

        print(MyData[:, 1])


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()


    sys.exit(app.exec_())