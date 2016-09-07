# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagedisplay5_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 605, 332))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Lon = QtWidgets.QLineEdit(self.groupBox)
        self.Lon.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Lon.setObjectName("Lon")
        self.gridLayout.addWidget(self.Lon, 1, 2, 1, 1)
        self.Pitchlabel = QtWidgets.QLabel(self.groupBox)
        self.Pitchlabel.setObjectName("Pitchlabel")
        self.gridLayout.addWidget(self.Pitchlabel, 5, 0, 1, 1)
        self.Headinglabel = QtWidgets.QLabel(self.groupBox)
        self.Headinglabel.setObjectName("Headinglabel")
        self.gridLayout.addWidget(self.Headinglabel, 6, 0, 1, 1)
        self.Latlabel = QtWidgets.QLabel(self.groupBox)
        self.Latlabel.setObjectName("Latlabel")
        self.gridLayout.addWidget(self.Latlabel, 2, 0, 1, 1)
        self.Depthlabel = QtWidgets.QLabel(self.groupBox)
        self.Depthlabel.setObjectName("Depthlabel")
        self.gridLayout.addWidget(self.Depthlabel, 3, 0, 1, 1)
        self.Depth = QtWidgets.QLineEdit(self.groupBox)
        self.Depth.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Depth.setObjectName("Depth")
        self.gridLayout.addWidget(self.Depth, 3, 2, 1, 1)
        self.Lonlabel = QtWidgets.QLabel(self.groupBox)
        self.Lonlabel.setObjectName("Lonlabel")
        self.gridLayout.addWidget(self.Lonlabel, 1, 0, 1, 1)
        self.Lat = QtWidgets.QLineEdit(self.groupBox)
        self.Lat.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Lat.setObjectName("Lat")
        self.gridLayout.addWidget(self.Lat, 2, 2, 1, 1)
        self.connectionlist = QtWidgets.QComboBox(self.groupBox)
        self.connectionlist.setObjectName("connectionlist")
        self.connectionlist.addItem("")
        self.connectionlist.setItemText(0, "")
        self.connectionlist.addItem("")
        self.connectionlist.addItem("")
        self.connectionlist.addItem("")
        self.connectionlist.addItem("")
        self.connectionlist.addItem("")
        self.connectionlist.addItem("")
        self.gridLayout.addWidget(self.connectionlist, 9, 2, 1, 1)
        self.Roll = QtWidgets.QLineEdit(self.groupBox)
        self.Roll.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Roll.setObjectName("Roll")
        self.gridLayout.addWidget(self.Roll, 4, 2, 1, 1)
        self.Pitch = QtWidgets.QLineEdit(self.groupBox)
        self.Pitch.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Pitch.setObjectName("Pitch")
        self.gridLayout.addWidget(self.Pitch, 5, 2, 1, 1)
        self.Heading = QtWidgets.QLineEdit(self.groupBox)
        self.Heading.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Heading.setObjectName("Heading")
        self.gridLayout.addWidget(self.Heading, 6, 2, 1, 1)
        self.Rolllabel = QtWidgets.QLabel(self.groupBox)
        self.Rolllabel.setObjectName("Rolllabel")
        self.gridLayout.addWidget(self.Rolllabel, 4, 0, 1, 1)
        self.setconnection = QtWidgets.QToolButton(self.groupBox)
        self.setconnection.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"     padding-right: 20px; /* make way for the popup button */\n"
" }\n"
"\n"
" QToolButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QToolButton:checked {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 white, stop: 1 blue);\n"
" }\n"
"\n"
" /* the subcontrols below are used only in the MenuButtonPopup mode */\n"
" QToolButton::menu-button {\n"
"     border: 2px solid gray;\n"
"     border-top-right-radius: 6px;\n"
"     border-bottom-right-radius: 6px;\n"
"     /* 16px width + 4px for border = 20px allocated above */\n"
"     width: 16px;\n"
" }\n"
"\n"
" QToolButton::menu-arrow {\n"
"     image: url(downarrow.png);\n"
" }\n"
"\n"
" QToolButton::menu-arrow:open {\n"
"     top: 1px; left: 1px; /* shift it a bit */\n"
" }")
        self.setconnection.setObjectName("setconnection")
        self.gridLayout.addWidget(self.setconnection, 9, 0, 1, 1)
        self.timelabel = QtWidgets.QLabel(self.groupBox)
        self.timelabel.setObjectName("timelabel")
        self.gridLayout.addWidget(self.timelabel, 0, 0, 1, 1)
        self.Time = QtWidgets.QLineEdit(self.groupBox)
        self.Time.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.Time.setObjectName("Time")
        self.gridLayout.addWidget(self.Time, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ZoomStepSlider = QtWidgets.QSlider(self.centralwidget)
        self.ZoomStepSlider.setMaximum(100)
        self.ZoomStepSlider.setProperty("value", 50)
        self.ZoomStepSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ZoomStepSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ZoomStepSlider.setTickInterval(10)
        self.ZoomStepSlider.setObjectName("ZoomStepSlider")
        self.horizontalLayout_2.addWidget(self.ZoomStepSlider)
        self.ZoomStepspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ZoomStepspinBox.setObjectName("ZoomStepspinBox")
        self.horizontalLayout_2.addWidget(self.ZoomStepspinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.rwd = QtWidgets.QPushButton(self.centralwidget)
        self.rwd.setAutoRepeat(True)
        self.rwd.setObjectName("rwd")
        self.horizontalLayout_2.addWidget(self.rwd)
        self.ImageStepspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ImageStepspinBox.setMinimum(1)
        self.ImageStepspinBox.setMaximum(200)
        self.ImageStepspinBox.setObjectName("ImageStepspinBox")
        self.horizontalLayout_2.addWidget(self.ImageStepspinBox)
        self.fwd = QtWidgets.QPushButton(self.centralwidget)
        self.fwd.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fwd.setAutoRepeat(True)
        self.fwd.setAutoDefault(False)
        self.fwd.setObjectName("fwd")
        self.horizontalLayout_2.addWidget(self.fwd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 22))
        self.menubar.setObjectName("menubar")
        self.menuPreference = QtWidgets.QMenu(self.menubar)
        self.menuPreference.setObjectName("menuPreference")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionArduino = QtWidgets.QAction(MainWindow)
        self.actionArduino.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/processing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArduino.setIcon(icon)
        self.actionArduino.setObjectName("actionArduino")
        self.actionLcm = QtWidgets.QAction(MainWindow)
        self.actionLcm.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/defaultlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLcm.setIcon(icon1)
        self.actionLcm.setObjectName("actionLcm")
        self.actionTcp = QtWidgets.QAction(MainWindow)
        self.actionTcp.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/Ubuntu_connessione_Internet_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTcp.setIcon(icon2)
        self.actionTcp.setObjectName("actionTcp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName("actionExit")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreference.setIcon(icon4)
        self.actionPreference.setObjectName("actionPreference")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon5)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon6)
        self.actionPause.setObjectName("actionPause")
        self.actionRecord = QtWidgets.QAction(MainWindow)
        self.actionRecord.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRecord.setIcon(icon7)
        self.actionRecord.setObjectName("actionRecord")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/saveinfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon8)
        self.actionHelp.setObjectName("actionHelp")
        self.menuPreference.addAction(self.actionPreference)
        self.menuPreference.addAction(self.actionExit)
        self.menubar.addAction(self.menuPreference.menuAction())
        self.toolBar.addAction(self.actionTcp)
        self.toolBar.addAction(self.actionArduino)
        self.toolBar.addAction(self.actionLcm)
        self.toolBar_2.addAction(self.actionPreference)
        self.toolBar_2.addAction(self.actionExit)
        self.toolBar_2.addAction(self.actionHelp)
        self.toolBar_3.addAction(self.actionPlay)
        self.toolBar_3.addAction(self.actionPause)
        self.toolBar_3.addAction(self.actionRecord)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "MetaData"))
        self.Pitchlabel.setText(_translate("MainWindow", "Pitch"))
        self.Headinglabel.setText(_translate("MainWindow", "Heading"))
        self.Latlabel.setText(_translate("MainWindow", "Lat"))
        self.Depthlabel.setText(_translate("MainWindow", "Depth"))
        self.Lonlabel.setText(_translate("MainWindow", "Lon"))
        self.connectionlist.setItemText(1, _translate("MainWindow", "tcp"))
        self.connectionlist.setItemText(2, _translate("MainWindow", "pg"))
        self.connectionlist.setItemText(3, _translate("MainWindow", "lcm"))
        self.connectionlist.setItemText(4, _translate("MainWindow", "serial1"))
        self.connectionlist.setItemText(5, _translate("MainWindow", "searial2"))
        self.connectionlist.setItemText(6, _translate("MainWindow", "serial3"))
        self.Rolllabel.setText(_translate("MainWindow", "Roll"))
        self.setconnection.setText(_translate("MainWindow", "Set"))
        self.timelabel.setText(_translate("MainWindow", "Time"))
        self.rwd.setText(_translate("MainWindow", "<<<"))
        self.rwd.setShortcut(_translate("MainWindow", "Backspace"))
        self.fwd.setText(_translate("MainWindow", ">>>"))
        self.menuPreference.setTitle(_translate("MainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionArduino.setText(_translate("MainWindow", "arduino"))
        self.actionLcm.setText(_translate("MainWindow", "lcm"))
        self.actionTcp.setText(_translate("MainWindow", "tcp"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))
        self.actionPlay.setText(_translate("MainWindow", "play"))
        self.actionPause.setText(_translate("MainWindow", "pause"))
        self.actionRecord.setText(_translate("MainWindow", "record"))
        self.actionHelp.setText(_translate("MainWindow", "help"))

import resource5_rc
