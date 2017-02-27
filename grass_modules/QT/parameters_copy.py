#!/usr/local/bin/python36
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtWidgets

# to run grass
GISDBASE = "/Users/epi/grassdata/"
MAPSET = "copy"
LOCATION_NAME = "project"

if sys.platform == 'darwin':
    GISBASE = "/usr/local/grass-7.3.svn"
else:
    GISBASE = "/usr/local/grass-7.3.svn"

os.environ["GISBASE"] = GISBASE
sys.path.append(os.path.join(GISBASE, 'etc/python'))

os.environ["GISDBASE"] = GISDBASE
os.environ["MAPSET"] = MAPSET
os.environ["LOCATION_NAME"] = LOCATION_NAME

gisrc = 'MAPSET: %s\n' % os.environ["MAPSET"]
gisrc += 'GISDBASE: %s\n' % os.environ["GISDBASE"]
gisrc += 'LOCATION_NAME: %s\n' % os.environ["LOCATION_NAME"]
gisrc += 'GUI: text'

grass_gisrc = open('/tmp/gisrc', 'w')
grass_gisrc.write(gisrc)
grass_gisrc.close()
os.environ['GISRC'] = '/tmp/gisrc'

os.environ[
    'PATH'] = '/usr/sbin:/bin/:/usr/bin:%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (
GISBASE, GISBASE)

from grass.script import task as gtask
from grass import script


class GisPrompt(QtWidgets.QWidget):
    def __init__(self, tab, parameterlist, command):
        super(GisPrompt, self).__init__()
        self.tab = tab
        self.parameterlist = parameterlist
        self.command = command
        self.initUI()

    def initUI(self):
        # TODO: I need to add label name and descriptions for this prompt
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # Label
        self.commandlabel = QtWidgets.QLabel(self.tab)
        self.commandlabel.setObjectName("label")
        self.gridLayout.addWidget(self.commandlabel, 0, 0, 1, 1)
        if self.command['label'] != '':
            self.commandlabel.setText(self.command['label'])
        else:
            self.commandlabel.setText(self.command['description'])
        # treeviewlabel
        self.treeviewlabel = QtWidgets.QLabel(self.tab)
        self.treeviewlabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.treeviewlabel.setObjectName("treeviewlabel")
        self.gridLayout.addWidget(self.treeviewlabel, 0, 1, 1, 1)
        self.treeviewlabel.setText('(' + self.command['name'] + '=' + self.command['type'] + ')')
        # treeviewresults
        self.treeviewresults = QtWidgets.QLineEdit(self.tab)
        self.treeviewresults.setObjectName("treeviewresults")
        self.gridLayout.addWidget(self.treeviewresults, 1, 0, 1, 1)
        # treeview button
        self.treeviewbutton = QtWidgets.QPushButton(self.tab)
        self.treeviewbutton.setText("")
        self.treeviewbutton.setObjectName("treeviewbutton")
        self.gridLayout.addWidget(self.treeviewbutton, 1, 1, 1, 1)
        # treeview
        self.treeView = QtWidgets.QTreeView(self.tab)
        self.treeView.setModel(self.get_model(self.command['prompt']))
        if self.command['multiple']:
            print('this should be false')
            self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        else:
            self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setEditTriggers(self.treeView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionBehavior(self.treeView.SelectRows)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.clicked.connect(self.selectitems)
        self.treeView.hide()
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 3, 0, 1, 1)
        #
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.treeviewbutton.clicked.connect(self.showhidetree)

    def showhidetree(self):
        if self.treeView.isVisible():
            self.treeView.hide()
        else:
            self.treeView.show()

    def list2model(self, lista):
        model = QStandardItemModel()
        model.setParent(self)
        for listitem in lista:
            parent_item = QStandardItem(str(listitem))
            parent_item.setSelectable(True)
            model.appendRow(parent_item)
        return model
        # mapsets = [i.decode() for i in script.mapsets(search_path=True)]

    def get_model(self, gtype):
        """
        creates the core of a tree based model to input into widget
        :param gtask: part of gtask for this widget
        :return: tree model
        """
        mapsets = [i.decode() for i in script.mapsets(search_path=True)]
        model = QStandardItemModel()
        # model.__init__(parent=None)
        model.setParent(self)
        for mapset in mapsets:
            parent_item = QStandardItem('Mapset: ' + str(mapset))
            parent_item.setSelectable(False)
            lista = script.core.list_pairs(gtype)
            # print
            for map in lista:
                if mapset in map:
                    # print(map)
                    parent_item.appendRow(QStandardItem
                                          ('%s@%s' % (map[0], map[1])))
            model.appendRow(parent_item)

        return model

    def selectitems(self):
        indexes = [i.model().itemFromIndex(i).text() for i in self.treeView.selectedIndexes()]
        maplist = ', '.join(indexes)
        self.treeviewresults.setText(maplist)
        self.parameterlist.append(maplist)
