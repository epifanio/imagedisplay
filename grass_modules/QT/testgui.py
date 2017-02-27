#!/usr/local/bin/python36
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtWidgets


from grassui import MainGui

class GisPrompt(QtWidgets.QWidget):
    def __init__(self, tab):      
        super(GisPrompt, self).__init__()
        self.tab = tab
        self.initUI()
        
    def initUI(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeviewbutton = QtWidgets.QPushButton(self.tab)
        self.treeviewbutton.setText("")
        self.treeviewbutton.setObjectName("treeviewbutton")
        self.gridLayout.addWidget(self.treeviewbutton, 0, 1, 1, 1)
        self.treeviewresults = QtWidgets.QLineEdit(self.tab)
        self.treeviewresults.setObjectName("treeviewresults")
        self.gridLayout.addWidget(self.treeviewresults, 0, 0, 1, 1)
        self.treeviewlabel = QtWidgets.QLabel(self.tab)
        self.treeviewlabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.treeviewlabel.setObjectName("treeviewlabel")
        self.gridLayout.addWidget(self.treeviewlabel, 0, 2, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.tab)
        self.treeView.hide()
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        #self.treeviewbutton.clicked.connect(self.showhidetree)
        self.treeviewbutton.clicked.connect(self.showhidetree)
        
    def showhidetree(self):
        print('connected')
        if self.treeView.isVisible():
            self.treeView.hide()
        else:
            self.treeView.show()
            self.treeView.setVisible(True)
        
        

class GrassCommand(QObject):
    def init(self):
        self.w = MainGui()
        self.w.treeView.hide()
        self.prompts = []
        
        gsec = ['tb1', 'tb2', 'tb3']
        for i in gsec:
            tab = QtWidgets.QWidget()
            tab.setObjectName(i)
            fileopen = GisPrompt(tab)
            #fileopen.treeviewbutton.clicked.connect(fileopen.showhidetree)
            #fileopen.treeviewbutton.clicked.connect(self.showhidetree)
            fileopen.setObjectName("fileopen_%s" % i)
            self.w.commandtab.addTab(tab, i)
            self.prompts.append(fileopen)
        self.w.show()
        
    def showhidetree(self):
        print('jjjj')

        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = GrassCommand()
    p.init()
    sys.exit(app.exec_())