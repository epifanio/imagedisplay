#!/usr/local/bin/python36

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.form_widget)
        self.setCentralWidget(_widget)

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        self.label = QLabel("Name for marker")
        self.txted = QLineEdit()
        self.lbled = QLabel("Enter position (eg: -33.89, 151.275)")
        self.pos = QLineEdit()
        
        self.browser = QWebEngineView()
        self.browser.load(QUrl('file:///Users/epi/gmap.html'))
        # html file available at:
        # https://gist.github.com/anonymous/4a745fa5b098a6afc2a84879858c83af
        print(dir(self.browser.page().view()))

    def __layout(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.h2Box = QHBoxLayout()
        self.h3Box = QVBoxLayout()

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.txted)

        self.h2Box.addWidget(self.lbled)
        self.h2Box.addWidget(self.pos)
        
        self.addmarkerbutton = QPushButton()
        self.printsourcebutton = QPushButton()
        
        self.h3Box.addWidget(self.browser)
        self.h3Box.addWidget(self.addmarkerbutton)
        self.h3Box.addWidget(self.printsourcebutton)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h2Box)
        self.vbox.addLayout(self.h3Box)
        self.setLayout(self.vbox)
        
        self.addmarkerbutton.clicked.connect(self.addMarker)
        
        self.printsourcebutton.clicked.connect(self.printsrc)
        
        

    def addMarker(self):
        latlon = self.pos.text()
        self.browser.page().runJavaScript("addMarker(%s)" % latlon)
        
        
    def printsrc(self):
        self.browser.page().toHtml(print)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 