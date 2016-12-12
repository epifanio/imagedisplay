# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/epi/PycharmProjects/imagedisplay/imagedisplay5_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 452, 349))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ZoomStepSlider = QtWidgets.QSlider(self.centralwidget)
        self.ZoomStepSlider.setMaximum(200)
        self.ZoomStepSlider.setProperty("value", 50)
        self.ZoomStepSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ZoomStepSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ZoomStepSlider.setTickInterval(10)
        self.ZoomStepSlider.setObjectName("ZoomStepSlider")
        self.horizontalLayout.addWidget(self.ZoomStepSlider)
        self.ZoomStepspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ZoomStepspinBox.setMaximum(200)
        self.ZoomStepspinBox.setProperty("value", 50)
        self.ZoomStepspinBox.setObjectName("ZoomStepspinBox")
        self.horizontalLayout.addWidget(self.ZoomStepspinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ImageIndexSlider = QtWidgets.QSlider(self.centralwidget)
        self.ImageIndexSlider.setProperty("value", 0)
        self.ImageIndexSlider.setSliderPosition(0)
        self.ImageIndexSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ImageIndexSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ImageIndexSlider.setTickInterval(500)
        self.ImageIndexSlider.setObjectName("ImageIndexSlider")
        self.horizontalLayout_2.addWidget(self.ImageIndexSlider)
        self.ImageIndexspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ImageIndexspinBox.setMinimum(0)
        self.ImageIndexspinBox.setProperty("value", 0)
        self.ImageIndexspinBox.setObjectName("ImageIndexspinBox")
        self.horizontalLayout_2.addWidget(self.ImageIndexspinBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ImageStepspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ImageStepspinBox.setMinimum(1)
        self.ImageStepspinBox.setMaximum(200)
        self.ImageStepspinBox.setObjectName("ImageStepspinBox")
        self.horizontalLayout_4.addWidget(self.ImageStepspinBox)
        self.rwd = QtWidgets.QPushButton(self.centralwidget)
        self.rwd.setAutoRepeat(True)
        self.rwd.setAutoRepeatDelay(500)
        self.rwd.setObjectName("rwd")
        self.horizontalLayout_4.addWidget(self.rwd)
        self.fwd = QtWidgets.QPushButton(self.centralwidget)
        self.fwd.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fwd.setAutoRepeat(True)
        self.fwd.setAutoRepeatDelay(500)
        self.fwd.setAutoDefault(False)
        self.fwd.setObjectName("fwd")
        self.horizontalLayout_4.addWidget(self.fwd)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_5.addWidget(self.label_29)
        self.rangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.rangeSlider.setMaximum(1000000)
        self.rangeSlider.setProperty("value", 0)
        self.rangeSlider.setSliderPosition(0)
        self.rangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rangeSlider.setObjectName("rangeSlider")
        self.horizontalLayout_5.addWidget(self.rangeSlider)
        self.rangeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rangeSpinBox.setMaximum(1000000)
        self.rangeSpinBox.setProperty("value", 0)
        self.rangeSpinBox.setObjectName("rangeSpinBox")
        self.horizontalLayout_5.addWidget(self.rangeSpinBox)
        self.zoomto = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/600px-Brosen_windrose.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomto.setIcon(icon)
        self.zoomto.setCheckable(True)
        self.zoomto.setObjectName("zoomto")
        self.horizontalLayout_5.addWidget(self.zoomto)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 22))
        self.menubar.setObjectName("menubar")
        self.menuPreference = QtWidgets.QMenu(self.menubar)
        self.menuPreference.setObjectName("menuPreference")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuProcessing = QtWidgets.QMenu(self.menubar)
        self.menuProcessing.setObjectName("menuProcessing")
        self.menuConveter = QtWidgets.QMenu(self.menuProcessing)
        self.menuConveter.setObjectName("menuConveter")
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
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.metadata = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.metadata.setMaximumSize(QtCore.QSize(360, 16777215))
        self.metadata.setObjectName("metadata")
        self.HBC = QtWidgets.QWidget()
        self.HBC.setObjectName("HBC")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.HBC)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.HBC)
        self.scrollArea_3.setMaximumSize(QtCore.QSize(330, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 314, 633))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        self.dateTimeEdit.setStyleSheet("border: 1px solid gray;\n"
"background: rgb(231, 231, 231);\n"
"border-radius: 5px;\n"
"padding: 0 8px;")
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_5.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.imagenorth = QtWidgets.QLineEdit(self.groupBox_3)
        self.imagenorth.setMaximumSize(QtCore.QSize(167, 16777215))
        self.imagenorth.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.imagenorth.setObjectName("imagenorth")
        self.gridLayout_5.addWidget(self.imagenorth, 3, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)
        self.Rolllabel = QtWidgets.QLabel(self.groupBox_3)
        self.Rolllabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Rolllabel.setObjectName("Rolllabel")
        self.gridLayout_5.addWidget(self.Rolllabel, 5, 0, 1, 1)
        self.altimeter = QtWidgets.QLineEdit(self.groupBox_3)
        self.altimeter.setMaximumSize(QtCore.QSize(80, 16777215))
        self.altimeter.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.altimeter.setObjectName("altimeter")
        self.gridLayout_5.addWidget(self.altimeter, 6, 1, 1, 1)
        self.waterdepth = QtWidgets.QLineEdit(self.groupBox_3)
        self.waterdepth.setMaximumSize(QtCore.QSize(80, 16777215))
        self.waterdepth.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.waterdepth.setObjectName("waterdepth")
        self.gridLayout_5.addWidget(self.waterdepth, 5, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 8, 0, 1, 1)
        self.Depthlabel = QtWidgets.QLabel(self.groupBox_3)
        self.Depthlabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Depthlabel.setObjectName("Depthlabel")
        self.gridLayout_5.addWidget(self.Depthlabel, 4, 0, 1, 1)
        self.O2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.O2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.O2.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.O2.setObjectName("O2")
        self.gridLayout_5.addWidget(self.O2, 9, 1, 1, 1)
        self.turbidity = QtWidgets.QLineEdit(self.groupBox_3)
        self.turbidity.setMaximumSize(QtCore.QSize(80, 16777215))
        self.turbidity.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.turbidity.setObjectName("turbidity")
        self.gridLayout_5.addWidget(self.turbidity, 12, 1, 1, 1)
        self.Pitchlabel = QtWidgets.QLabel(self.groupBox_3)
        self.Pitchlabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Pitchlabel.setObjectName("Pitchlabel")
        self.gridLayout_5.addWidget(self.Pitchlabel, 6, 0, 1, 1)
        self.chlorophyll = QtWidgets.QLineEdit(self.groupBox_3)
        self.chlorophyll.setMaximumSize(QtCore.QSize(80, 16777215))
        self.chlorophyll.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.chlorophyll.setObjectName("chlorophyll")
        self.gridLayout_5.addWidget(self.chlorophyll, 11, 1, 1, 1)
        self.linklabel = QtWidgets.QLabel(self.groupBox_3)
        self.linklabel.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"background: rgb(231, 231, 231);")
        self.linklabel.setTextFormat(QtCore.Qt.RichText)
        self.linklabel.setOpenExternalLinks(True)
        self.linklabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.linklabel.setObjectName("linklabel")
        self.gridLayout_5.addWidget(self.linklabel, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 11, 0, 1, 1)
        self.imageeast = QtWidgets.QLineEdit(self.groupBox_3)
        self.imageeast.setMaximumSize(QtCore.QSize(167, 16777215))
        self.imageeast.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.imageeast.setObjectName("imageeast")
        self.gridLayout_5.addWidget(self.imageeast, 2, 1, 1, 1)
        self.CDOM = QtWidgets.QLineEdit(self.groupBox_3)
        self.CDOM.setMaximumSize(QtCore.QSize(80, 16777215))
        self.CDOM.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.CDOM.setObjectName("CDOM")
        self.gridLayout_5.addWidget(self.CDOM, 10, 1, 1, 1)
        self.Latlabel = QtWidgets.QLabel(self.groupBox_3)
        self.Latlabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Latlabel.setObjectName("Latlabel")
        self.gridLayout_5.addWidget(self.Latlabel, 3, 0, 1, 1)
        self.temperature = QtWidgets.QLineEdit(self.groupBox_3)
        self.temperature.setMaximumSize(QtCore.QSize(80, 16777215))
        self.temperature.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.temperature.setObjectName("temperature")
        self.gridLayout_5.addWidget(self.temperature, 8, 1, 1, 1)
        self.hbcdepth = QtWidgets.QLineEdit(self.groupBox_3)
        self.hbcdepth.setMaximumSize(QtCore.QSize(80, 16777215))
        self.hbcdepth.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.hbcdepth.setObjectName("hbcdepth")
        self.gridLayout_5.addWidget(self.hbcdepth, 4, 1, 1, 1)
        self.timelabel = QtWidgets.QLabel(self.groupBox_3)
        self.timelabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.timelabel.setObjectName("timelabel")
        self.gridLayout_5.addWidget(self.timelabel, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 12, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 10, 0, 1, 1)
        self.Lonlabel = QtWidgets.QLabel(self.groupBox_3)
        self.Lonlabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Lonlabel.setObjectName("Lonlabel")
        self.gridLayout_5.addWidget(self.Lonlabel, 2, 0, 1, 1)
        self.salinity = QtWidgets.QLineEdit(self.groupBox_3)
        self.salinity.setMaximumSize(QtCore.QSize(80, 16777215))
        self.salinity.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.salinity.setObjectName("salinity")
        self.gridLayout_5.addWidget(self.salinity, 7, 1, 1, 1)
        self.Headinglabel = QtWidgets.QLabel(self.groupBox_3)
        self.Headinglabel.setMaximumSize(QtCore.QSize(90, 16777215))
        self.Headinglabel.setObjectName("Headinglabel")
        self.gridLayout_5.addWidget(self.Headinglabel, 7, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.addWidget(self.scrollArea_3)
        self.metadata.addTab(self.HBC, "")
        self.MBED = QtWidgets.QWidget()
        self.MBED.setObjectName("MBED")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.MBED)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.MBED)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 312, 633))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 11, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 10, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 8, 0, 1, 1)
        self.pingtime = QtWidgets.QLineEdit(self.groupBox)
        self.pingtime.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pingtime.setObjectName("pingtime")
        self.gridLayout_3.addWidget(self.pingtime, 0, 1, 1, 1)
        self.pingnumber = QtWidgets.QLineEdit(self.groupBox)
        self.pingnumber.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pingnumber.setObjectName("pingnumber")
        self.gridLayout_3.addWidget(self.pingnumber, 1, 1, 1, 1)
        self.beamnumber = QtWidgets.QLineEdit(self.groupBox)
        self.beamnumber.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.beamnumber.setObjectName("beamnumber")
        self.gridLayout_3.addWidget(self.beamnumber, 2, 1, 1, 1)
        self.pingeasting = QtWidgets.QLineEdit(self.groupBox)
        self.pingeasting.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pingeasting.setObjectName("pingeasting")
        self.gridLayout_3.addWidget(self.pingeasting, 3, 1, 1, 1)
        self.pingnorthing = QtWidgets.QLineEdit(self.groupBox)
        self.pingnorthing.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pingnorthing.setObjectName("pingnorthing")
        self.gridLayout_3.addWidget(self.pingnorthing, 4, 1, 1, 1)
        self.pingdepth = QtWidgets.QLineEdit(self.groupBox)
        self.pingdepth.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pingdepth.setObjectName("pingdepth")
        self.gridLayout_3.addWidget(self.pingdepth, 5, 1, 1, 1)
        self.pinglongitude = QtWidgets.QLineEdit(self.groupBox)
        self.pinglongitude.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pinglongitude.setObjectName("pinglongitude")
        self.gridLayout_3.addWidget(self.pinglongitude, 6, 1, 1, 1)
        self.pinglatitude = QtWidgets.QLineEdit(self.groupBox)
        self.pinglatitude.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.pinglatitude.setObjectName("pinglatitude")
        self.gridLayout_3.addWidget(self.pinglatitude, 7, 1, 1, 1)
        self.trueangle = QtWidgets.QLineEdit(self.groupBox)
        self.trueangle.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.trueangle.setObjectName("trueangle")
        self.gridLayout_3.addWidget(self.trueangle, 8, 1, 1, 1)
        self.backscatter = QtWidgets.QLineEdit(self.groupBox)
        self.backscatter.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.backscatter.setObjectName("backscatter")
        self.gridLayout_3.addWidget(self.backscatter, 9, 1, 1, 1)
        self.correctedbackscatter = QtWidgets.QLineEdit(self.groupBox)
        self.correctedbackscatter.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.correctedbackscatter.setObjectName("correctedbackscatter")
        self.gridLayout_3.addWidget(self.correctedbackscatter, 10, 1, 1, 1)
        self.datetime = QtWidgets.QLineEdit(self.groupBox)
        self.datetime.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.datetime.setObjectName("datetime")
        self.gridLayout_3.addWidget(self.datetime, 11, 1, 1, 1)
        self.line = QtWidgets.QLineEdit(self.groupBox)
        self.line.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }")
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 12, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout_12.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.addWidget(self.scrollArea_4)
        self.metadata.addTab(self.MBED, "")
        self.Notes = QtWidgets.QWidget()
        self.Notes.setObjectName("Notes")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Notes)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.Notes)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 312, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fixpeble = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fixpeble.setObjectName("fixpeble")
        self.gridLayout_2.addWidget(self.fixpeble, 8, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 6, 1, 1, 1)
        self.GravelSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.GravelSlider.setMaximum(100)
        self.GravelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GravelSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.GravelSlider.setObjectName("GravelSlider")
        self.gridLayout_2.addWidget(self.GravelSlider, 7, 2, 1, 1)
        self.SandSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.SandSlider.setMaximum(100)
        self.SandSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SandSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.SandSlider.setObjectName("SandSlider")
        self.gridLayout_2.addWidget(self.SandSlider, 6, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 8, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 1, 1, 1)
        self.subdtatecomponent = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.subdtatecomponent.setStyleSheet("QToolButton { /* all types of tool button */\n"
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
        self.subdtatecomponent.setObjectName("subdtatecomponent")
        self.gridLayout_2.addWidget(self.subdtatecomponent, 2, 1, 1, 1)
        self.geoformcomponent = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.geoformcomponent.setStyleSheet("QToolButton { /* all types of tool button */\n"
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
        self.geoformcomponent.setObjectName("geoformcomponent")
        self.gridLayout_2.addWidget(self.geoformcomponent, 1, 1, 1, 1)
        self.notes = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.notes.setObjectName("notes")
        self.gridLayout_2.addWidget(self.notes, 9, 1, 1, 4)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 5, 1, 1, 1)
        self.fixclay = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fixclay.setObjectName("fixclay")
        self.gridLayout_2.addWidget(self.fixclay, 5, 4, 1, 1)
        self.ClaySlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.ClaySlider.setMaximum(100)
        self.ClaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.ClaySlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ClaySlider.setObjectName("ClaySlider")
        self.gridLayout_2.addWidget(self.ClaySlider, 5, 2, 1, 1)
        self.MudSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.MudSlider.setMaximum(100)
        self.MudSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MudSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.MudSlider.setTickInterval(10)
        self.MudSlider.setObjectName("MudSlider")
        self.gridLayout_2.addWidget(self.MudSlider, 3, 2, 1, 1)
        self.substratelist = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.substratelist.setObjectName("substratelist")
        self.substratelist.addItem("")
        self.substratelist.setItemText(0, "")
        self.substratelist.addItem("")
        self.substratelist.addItem("")
        self.substratelist.addItem("")
        self.substratelist.addItem("")
        self.substratelist.addItem("")
        self.substratelist.addItem("")
        self.gridLayout_2.addWidget(self.substratelist, 2, 2, 1, 3)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 7, 1, 1, 1)
        self.fixmud = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fixmud.setObjectName("fixmud")
        self.gridLayout_2.addWidget(self.fixmud, 3, 4, 1, 1)
        self.geoformlist = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.geoformlist.setObjectName("geoformlist")
        self.geoformlist.addItem("")
        self.geoformlist.setItemText(0, "")
        self.geoformlist.addItem("")
        self.geoformlist.addItem("")
        self.geoformlist.addItem("")
        self.geoformlist.addItem("")
        self.geoformlist.addItem("")
        self.geoformlist.addItem("")
        self.gridLayout_2.addWidget(self.geoformlist, 1, 2, 1, 3)
        self.PebleSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PebleSlider.setMaximum(100)
        self.PebleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PebleSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.PebleSlider.setObjectName("PebleSlider")
        self.gridLayout_2.addWidget(self.PebleSlider, 8, 2, 1, 1)
        self.fixgravel = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fixgravel.setObjectName("fixgravel")
        self.gridLayout_2.addWidget(self.fixgravel, 7, 4, 1, 1)
        self.fixsand = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.fixsand.setObjectName("fixsand")
        self.gridLayout_2.addWidget(self.fixsand, 6, 4, 1, 1)
        self.mud = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mud.sizePolicy().hasHeightForWidth())
        self.mud.setSizePolicy(sizePolicy)
        self.mud.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mud.setObjectName("mud")
        self.gridLayout_2.addWidget(self.mud, 3, 3, 1, 1)
        self.clay = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clay.sizePolicy().hasHeightForWidth())
        self.clay.setSizePolicy(sizePolicy)
        self.clay.setMaximumSize(QtCore.QSize(30, 16777215))
        self.clay.setObjectName("clay")
        self.gridLayout_2.addWidget(self.clay, 5, 3, 1, 1)
        self.sand = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sand.sizePolicy().hasHeightForWidth())
        self.sand.setSizePolicy(sizePolicy)
        self.sand.setMaximumSize(QtCore.QSize(30, 16777215))
        self.sand.setObjectName("sand")
        self.gridLayout_2.addWidget(self.sand, 6, 3, 1, 1)
        self.gravel = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gravel.sizePolicy().hasHeightForWidth())
        self.gravel.setSizePolicy(sizePolicy)
        self.gravel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.gravel.setObjectName("gravel")
        self.gridLayout_2.addWidget(self.gravel, 7, 3, 1, 1)
        self.peble = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peble.sizePolicy().hasHeightForWidth())
        self.peble.setSizePolicy(sizePolicy)
        self.peble.setMaximumSize(QtCore.QSize(30, 16777215))
        self.peble.setObjectName("peble")
        self.gridLayout_2.addWidget(self.peble, 8, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.submit = QtWidgets.QPushButton(self.Notes)
        self.submit.setObjectName("submit")
        self.verticalLayout_8.addWidget(self.submit)
        self.metadata.addTab(self.Notes, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gtvector_type = QtWidgets.QComboBox(self.groupBox_2)
        self.gtvector_type.setObjectName("gtvector_type")
        self.gtvector_type.addItem("")
        self.gtvector_type.addItem("")
        self.gtvector_type.addItem("")
        self.gridLayout_4.addWidget(self.gtvector_type, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_30.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_8.addWidget(self.label_30)
        self.frontbuffer = QtWidgets.QSpinBox(self.groupBox_2)
        self.frontbuffer.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frontbuffer.setObjectName("frontbuffer")
        self.horizontalLayout_8.addWidget(self.frontbuffer)
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_31.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_8.addWidget(self.label_31)
        self.rearbuffer = QtWidgets.QSpinBox(self.groupBox_2)
        self.rearbuffer.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rearbuffer.setObjectName("rearbuffer")
        self.horizontalLayout_8.addWidget(self.rearbuffer)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        self.query = QtWidgets.QPushButton(self.groupBox_2)
        self.query.setObjectName("query")
        self.gridLayout_4.addWidget(self.query, 6, 1, 1, 1)
        self.bufferwidth = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.bufferwidth.setObjectName("bufferwidth")
        self.gridLayout_4.addWidget(self.bufferwidth, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gtvector = QtWidgets.QLineEdit(self.groupBox_2)
        self.gtvector.setObjectName("gtvector")
        self.horizontalLayout_9.addWidget(self.gtvector)
        self.gtvector_select = QtWidgets.QToolButton(self.groupBox_2)
        self.gtvector_select.setObjectName("gtvector_select")
        self.horizontalLayout_9.addWidget(self.gtvector_select)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)
        self.syncGE = QtWidgets.QCheckBox(self.groupBox_2)
        self.syncGE.setObjectName("syncGE")
        self.gridLayout_4.addWidget(self.syncGE, 6, 0, 1, 1)
        self.append_geometry = QtWidgets.QPushButton(self.groupBox_2)
        self.append_geometry.setObjectName("append_geometry")
        self.gridLayout_4.addWidget(self.append_geometry, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 4, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.verticalLayout_13.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 409, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.metadata.addTab(self.tab, "")
        self.verticalLayout_9.addWidget(self.metadata)
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionArduino = QtWidgets.QAction(MainWindow)
        self.actionArduino.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/processing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArduino.setIcon(icon1)
        self.actionArduino.setObjectName("actionArduino")
        self.actionLcm = QtWidgets.QAction(MainWindow)
        self.actionLcm.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/defaultlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLcm.setIcon(icon2)
        self.actionLcm.setObjectName("actionLcm")
        self.actionTcp = QtWidgets.QAction(MainWindow)
        self.actionTcp.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/Ubuntu_connessione_Internet_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTcp.setIcon(icon3)
        self.actionTcp.setObjectName("actionTcp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreference.setIcon(icon5)
        self.actionPreference.setObjectName("actionPreference")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon6)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon7)
        self.actionPause.setObjectName("actionPause")
        self.actionRecord = QtWidgets.QAction(MainWindow)
        self.actionRecord.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRecord.setIcon(icon8)
        self.actionRecord.setObjectName("actionRecord")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/saveinfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon9)
        self.actionHelp.setObjectName("actionHelp")
        self.actionImageDirectory = QtWidgets.QAction(MainWindow)
        self.actionImageDirectory.setObjectName("actionImageDirectory")
        self.actionASCII_Converter = QtWidgets.QAction(MainWindow)
        self.actionASCII_Converter.setObjectName("actionASCII_Converter")
        self.actionASCII2Feather = QtWidgets.QAction(MainWindow)
        self.actionASCII2Feather.setObjectName("actionASCII2Feather")
        self.actionSelect_Image_Metadata = QtWidgets.QAction(MainWindow)
        self.actionSelect_Image_Metadata.setObjectName("actionSelect_Image_Metadata")
        self.menuPreference.addAction(self.actionPreference)
        self.menuPreference.addAction(self.actionExit)
        self.menuFile.addAction(self.actionImageDirectory)
        self.menuFile.addAction(self.actionSelect_Image_Metadata)
        self.menuConveter.addAction(self.actionASCII2Feather)
        self.menuProcessing.addAction(self.menuConveter.menuAction())
        self.menubar.addAction(self.menuPreference.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.toolBar.addAction(self.actionTcp)
        self.toolBar.addAction(self.actionArduino)
        self.toolBar.addAction(self.actionLcm)
        self.toolBar_2.addAction(self.actionPreference)
        self.toolBar_2.addAction(self.actionHelp)
        self.toolBar_3.addAction(self.actionPlay)
        self.toolBar_3.addAction(self.actionPause)
        self.toolBar_3.addAction(self.actionRecord)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.metadata.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image.setText(_translate("MainWindow", "Load Images"))
        self.label.setText(_translate("MainWindow", "Zoom"))
        self.label_2.setText(_translate("MainWindow", "Image switch"))
        self.rwd.setText(_translate("MainWindow", "<<<"))
        self.rwd.setShortcut(_translate("MainWindow", "Left"))
        self.fwd.setText(_translate("MainWindow", ">>>"))
        self.fwd.setShortcut(_translate("MainWindow", "Right"))
        self.label_29.setText(_translate("MainWindow", "Range"))
        self.zoomto.setText(_translate("MainWindow", "..."))
        self.menuPreference.setTitle(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuProcessing.setTitle(_translate("MainWindow", "Processing"))
        self.menuConveter.setTitle(_translate("MainWindow", "Conveter"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Image Metadata"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yy h:mm:ss:zzz AP"))
        self.imagenorth.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "Image Name"))
        self.Rolllabel.setText(_translate("MainWindow", "Water Depth"))
        self.altimeter.setText(_translate("MainWindow", "0"))
        self.waterdepth.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "O2"))
        self.label_3.setText(_translate("MainWindow", "Temperature"))
        self.Depthlabel.setText(_translate("MainWindow", "Vehicle Depth"))
        self.O2.setText(_translate("MainWindow", "0"))
        self.turbidity.setText(_translate("MainWindow", "0"))
        self.Pitchlabel.setText(_translate("MainWindow", "Altimeter"))
        self.chlorophyll.setText(_translate("MainWindow", "0"))
        self.linklabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"http://www.google.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Image</span></a></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Chlorophyll"))
        self.imageeast.setText(_translate("MainWindow", "0"))
        self.CDOM.setText(_translate("MainWindow", "0"))
        self.Latlabel.setText(_translate("MainWindow", "North"))
        self.temperature.setText(_translate("MainWindow", "0"))
        self.hbcdepth.setText(_translate("MainWindow", "0"))
        self.timelabel.setText(_translate("MainWindow", "Time"))
        self.label_26.setText(_translate("MainWindow", "Turbidity"))
        self.label_24.setText(_translate("MainWindow", "CDOM"))
        self.Lonlabel.setText(_translate("MainWindow", "East"))
        self.salinity.setText(_translate("MainWindow", "0"))
        self.Headinglabel.setText(_translate("MainWindow", "Salinity"))
        self.metadata.setTabText(self.metadata.indexOf(self.HBC), _translate("MainWindow", "HBC"))
        self.groupBox.setTitle(_translate("MainWindow", "MBES"))
        self.label_15.setText(_translate("MainWindow", "Datetime"))
        self.label_5.setText(_translate("MainWindow", "Ping Number"))
        self.label_4.setText(_translate("MainWindow", "Ping Time"))
        self.label_13.setText(_translate("MainWindow", "Corrected Backcatter Value"))
        self.label_7.setText(_translate("MainWindow", "Easting"))
        self.label_9.setText(_translate("MainWindow", "Depth"))
        self.label_11.setText(_translate("MainWindow", "Latitude"))
        self.label_16.setText(_translate("MainWindow", "Line"))
        self.label_8.setText(_translate("MainWindow", "Northing"))
        self.label_6.setText(_translate("MainWindow", "Beam Number"))
        self.label_12.setText(_translate("MainWindow", "Backscatter Value"))
        self.label_10.setText(_translate("MainWindow", "Longitude"))
        self.label_14.setText(_translate("MainWindow", "True Angle"))
        self.metadata.setTabText(self.metadata.indexOf(self.MBED), _translate("MainWindow", "MBES"))
        self.fixpeble.setText(_translate("MainWindow", "fix"))
        self.label_19.setText(_translate("MainWindow", "Sand"))
        self.label_21.setText(_translate("MainWindow", "Peble"))
        self.label_17.setText(_translate("MainWindow", "Mud"))
        self.subdtatecomponent.setText(_translate("MainWindow", "SC"))
        self.geoformcomponent.setText(_translate("MainWindow", "GC"))
        self.label_18.setText(_translate("MainWindow", "Clay"))
        self.fixclay.setText(_translate("MainWindow", "fix"))
        self.substratelist.setItemText(1, _translate("MainWindow", "1"))
        self.substratelist.setItemText(2, _translate("MainWindow", "2"))
        self.substratelist.setItemText(3, _translate("MainWindow", "3"))
        self.substratelist.setItemText(4, _translate("MainWindow", "4"))
        self.substratelist.setItemText(5, _translate("MainWindow", "5"))
        self.substratelist.setItemText(6, _translate("MainWindow", "6"))
        self.label_20.setText(_translate("MainWindow", "Gravel"))
        self.fixmud.setText(_translate("MainWindow", "fix"))
        self.geoformlist.setItemText(1, _translate("MainWindow", "1"))
        self.geoformlist.setItemText(2, _translate("MainWindow", "2"))
        self.geoformlist.setItemText(3, _translate("MainWindow", "3"))
        self.geoformlist.setItemText(4, _translate("MainWindow", "4"))
        self.geoformlist.setItemText(5, _translate("MainWindow", "5"))
        self.geoformlist.setItemText(6, _translate("MainWindow", "6"))
        self.fixgravel.setText(_translate("MainWindow", "fix"))
        self.fixsand.setText(_translate("MainWindow", "fix"))
        self.submit.setText(_translate("MainWindow", "Tag"))
        self.metadata.setTabText(self.metadata.indexOf(self.Notes), _translate("MainWindow", "Notes"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Line Buffer"))
        self.gtvector_type.setItemText(0, _translate("MainWindow", "SHP"))
        self.gtvector_type.setItemText(1, _translate("MainWindow", "GeoJson"))
        self.gtvector_type.setItemText(2, _translate("MainWindow", "KML"))
        self.label_30.setText(_translate("MainWindow", "+"))
        self.label_31.setText(_translate("MainWindow", "-"))
        self.query.setText(_translate("MainWindow", "Save"))
        self.label_28.setText(_translate("MainWindow", "Length (# img)"))
        self.label_27.setText(_translate("MainWindow", "Width (m)"))
        self.gtvector_select.setText(_translate("MainWindow", "..."))
        self.syncGE.setText(_translate("MainWindow", "GE"))
        self.append_geometry.setText(_translate("MainWindow", "Append Geometry"))
        self.metadata.setTabText(self.metadata.indexOf(self.tab), _translate("MainWindow", "GT"))
        self.actionArduino.setText(_translate("MainWindow", "arduino"))
        self.actionLcm.setText(_translate("MainWindow", "lcm"))
        self.actionTcp.setText(_translate("MainWindow", "tcp"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))
        self.actionPlay.setText(_translate("MainWindow", "play"))
        self.actionPause.setText(_translate("MainWindow", "pause"))
        self.actionRecord.setText(_translate("MainWindow", "record"))
        self.actionHelp.setText(_translate("MainWindow", "help"))
        self.actionImageDirectory.setText(_translate("MainWindow", "Select Image Directory"))
        self.actionASCII_Converter.setText(_translate("MainWindow", "ASCII Converter"))
        self.actionASCII2Feather.setText(_translate("MainWindow", "ASCII to Feather"))
        self.actionSelect_Image_Metadata.setText(_translate("MainWindow", "Select Image Metadata"))

import resource5_rc
