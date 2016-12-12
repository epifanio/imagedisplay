#!/usr/bin/env python

#import sys
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *

from PyQt5 import QtWidgets
from imagedisplay5_ui import Ui_MainWindow

class MainGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)