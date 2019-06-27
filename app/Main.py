# import the necessary packages
from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

import sys
from app.client.pyqt5.GUI_Detection import *
app = QApplication(sys.argv)
widget = GUI_Detection()
widget.setWindowFlags(widget.windowFlags() |
        QtCore.Qt.WindowMinimizeButtonHint |
        QtCore.Qt.WindowMaximizeButtonHint|
        QtCore.Qt.WindowSystemMenuHint)

widget.show()
sys.exit(app.exec_())



