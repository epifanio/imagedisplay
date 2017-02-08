#!/usr/bin/env python


from PyQt5 import QtWidgets
from htmap_ui import Ui_MainWindow

class HtMapGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)