# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/epi/PycharmProjects/imagedisplay/converter_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Converter(object):
    def setupUi(self, Converter):
        Converter.setObjectName("Converter")
        Converter.resize(396, 763)
        Converter.setAutoFillBackground(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Converter)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.asciiconverter = QtWidgets.QGroupBox(Converter)
        self.asciiconverter.setObjectName("asciiconverter")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.asciiconverter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.asciiconverter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ASCII = QtWidgets.QLineEdit(self.asciiconverter)
        self.ASCII.setObjectName("ASCII")
        self.gridLayout.addWidget(self.ASCII, 0, 1, 1, 1)
        self.feather = QtWidgets.QLineEdit(self.asciiconverter)
        self.feather.setObjectName("feather")
        self.gridLayout.addWidget(self.feather, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.asciiconverter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.getASCII = QtWidgets.QToolButton(self.asciiconverter)
        self.getASCII.setObjectName("getASCII")
        self.gridLayout.addWidget(self.getASCII, 0, 2, 1, 1)
        self.setFeather = QtWidgets.QToolButton(self.asciiconverter)
        self.setFeather.setObjectName("setFeather")
        self.gridLayout.addWidget(self.setFeather, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buildgeometrycheckbox = QtWidgets.QCheckBox(self.asciiconverter)
        self.buildgeometrycheckbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buildgeometrycheckbox.setObjectName("buildgeometrycheckbox")
        self.horizontalLayout.addWidget(self.buildgeometrycheckbox)
        self.buildtimecheckbox = QtWidgets.QCheckBox(self.asciiconverter)
        self.buildtimecheckbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buildtimecheckbox.setObjectName("buildtimecheckbox")
        self.horizontalLayout.addWidget(self.buildtimecheckbox)
        self.advancedsettings = QtWidgets.QCheckBox(self.asciiconverter)
        self.advancedsettings.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.advancedsettings.setAutoFillBackground(False)
        self.advancedsettings.setObjectName("advancedsettings")
        self.horizontalLayout.addWidget(self.advancedsettings)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.time_unit_label = QtWidgets.QLabel(self.asciiconverter)
        self.time_unit_label.setObjectName("time_unit_label")
        self.gridLayout_3.addWidget(self.time_unit_label, 3, 0, 1, 1)
        self.x_geom_label = QtWidgets.QLabel(self.asciiconverter)
        self.x_geom_label.setMaximumSize(QtCore.QSize(16, 16777215))
        self.x_geom_label.setObjectName("x_geom_label")
        self.gridLayout_3.addWidget(self.x_geom_label, 0, 0, 1, 1)
        self.y_geom_label = QtWidgets.QLabel(self.asciiconverter)
        self.y_geom_label.setMaximumSize(QtCore.QSize(16, 16777215))
        self.y_geom_label.setObjectName("y_geom_label")
        self.gridLayout_3.addWidget(self.y_geom_label, 1, 0, 1, 1)
        self.x_geom = QtWidgets.QLineEdit(self.asciiconverter)
        self.x_geom.setMaximumSize(QtCore.QSize(167, 167))
        self.x_geom.setObjectName("x_geom")
        self.gridLayout_3.addWidget(self.x_geom, 0, 1, 1, 1)
        self.y_geom = QtWidgets.QLineEdit(self.asciiconverter)
        self.y_geom.setMaximumSize(QtCore.QSize(167, 167))
        self.y_geom.setObjectName("y_geom")
        self.gridLayout_3.addWidget(self.y_geom, 1, 1, 1, 1)
        self.ping_time = QtWidgets.QLineEdit(self.asciiconverter)
        self.ping_time.setMaximumSize(QtCore.QSize(167, 167))
        self.ping_time.setObjectName("ping_time")
        self.gridLayout_3.addWidget(self.ping_time, 2, 1, 1, 1)
        self.ping_time_label = QtWidgets.QLabel(self.asciiconverter)
        self.ping_time_label.setObjectName("ping_time_label")
        self.gridLayout_3.addWidget(self.ping_time_label, 2, 0, 1, 1)
        self.time_delta_label = QtWidgets.QLabel(self.asciiconverter)
        self.time_delta_label.setObjectName("time_delta_label")
        self.gridLayout_3.addWidget(self.time_delta_label, 4, 0, 1, 1)
        self.time_unit = QtWidgets.QLineEdit(self.asciiconverter)
        self.time_unit.setMaximumSize(QtCore.QSize(167, 167))
        self.time_unit.setObjectName("time_unit")
        self.gridLayout_3.addWidget(self.time_unit, 3, 1, 1, 1)
        self.time_delta = QtWidgets.QLineEdit(self.asciiconverter)
        self.time_delta.setMaximumSize(QtCore.QSize(167, 167))
        self.time_delta.setObjectName("time_delta")
        self.gridLayout_3.addWidget(self.time_delta, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.asciiconverter)
        self.advancedparsing = QtWidgets.QGroupBox(Converter)
        self.advancedparsing.setObjectName("advancedparsing")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.advancedparsing)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.advancedparsing)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.advancedparsing)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.names = QtWidgets.QLineEdit(self.advancedparsing)
        self.names.setObjectName("names")
        self.gridLayout_2.addWidget(self.names, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.advancedparsing)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.skip_rows = QtWidgets.QSpinBox(self.advancedparsing)
        self.skip_rows.setProperty("value", 16)
        self.skip_rows.setObjectName("skip_rows")
        self.gridLayout_2.addWidget(self.skip_rows, 0, 1, 1, 1)
        self.separator = QtWidgets.QLineEdit(self.advancedparsing)
        self.separator.setObjectName("separator")
        self.gridLayout_2.addWidget(self.separator, 2, 1, 1, 1)
        self.preview = QtWidgets.QTextEdit(self.advancedparsing)
        self.preview.setObjectName("preview")
        self.gridLayout_2.addWidget(self.preview, 6, 0, 1, 2)
        self.asciihead = QtWidgets.QTextEdit(self.advancedparsing)
        self.asciihead.setObjectName("asciihead")
        self.gridLayout_2.addWidget(self.asciihead, 5, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shoraw = QtWidgets.QRadioButton(self.advancedparsing)
        self.shoraw.setObjectName("shoraw")
        self.horizontalLayout_2.addWidget(self.shoraw)
        self.showparsed = QtWidgets.QRadioButton(self.advancedparsing)
        self.showparsed.setObjectName("showparsed")
        self.horizontalLayout_2.addWidget(self.showparsed)
        self.reset_parser = QtWidgets.QToolButton(self.advancedparsing)
        self.reset_parser.setText("")
        self.reset_parser.setObjectName("reset_parser")
        self.horizontalLayout_2.addWidget(self.reset_parser)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.advancedparsing)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.delimiterWS = QtWidgets.QComboBox(self.advancedparsing)
        self.delimiterWS.setObjectName("delimiterWS")
        self.delimiterWS.addItem("")
        self.delimiterWS.addItem("")
        self.gridLayout_2.addWidget(self.delimiterWS, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.advancedparsing)
        spacerItem = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.convert = QtWidgets.QPushButton(Converter)
        self.convert.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.convert.setFont(font)
        self.convert.setObjectName("convert")
        self.verticalLayout_3.addWidget(self.convert)
        self.progressBar = QtWidgets.QProgressBar(Converter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)

        self.retranslateUi(Converter)
        QtCore.QMetaObject.connectSlotsByName(Converter)

    def retranslateUi(self, Converter):
        _translate = QtCore.QCoreApplication.translate
        Converter.setWindowTitle(_translate("Converter", "Converter"))
        self.asciiconverter.setTitle(_translate("Converter", "ASCII->Feather"))
        self.label_2.setText(_translate("Converter", "Output"))
        self.label.setText(_translate("Converter", "Input"))
        self.getASCII.setText(_translate("Converter", "..."))
        self.setFeather.setText(_translate("Converter", "..."))
        self.buildgeometrycheckbox.setText(_translate("Converter", "Build Geometry "))
        self.buildtimecheckbox.setText(_translate("Converter", "Build Datetime"))
        self.advancedsettings.setText(_translate("Converter", "Advanced"))
        self.time_unit_label.setText(_translate("Converter", "Unit"))
        self.x_geom_label.setText(_translate("Converter", "X"))
        self.y_geom_label.setText(_translate("Converter", "Y"))
        self.x_geom.setText(_translate("Converter", "Easting"))
        self.y_geom.setText(_translate("Converter", "Northing"))
        self.ping_time.setText(_translate("Converter", "Ping Time"))
        self.ping_time_label.setText(_translate("Converter", "T"))
        self.time_delta_label.setText(_translate("Converter", "Delta T"))
        self.time_unit.setText(_translate("Converter", "s"))
        self.time_delta.setText(_translate("Converter", "16"))
        self.advancedparsing.setTitle(_translate("Converter", "Advanced Parsing"))
        self.label_4.setText(_translate("Converter", "Column Names"))
        self.label_3.setText(_translate("Converter", "Skip rows"))
        self.names.setText(_translate("Converter", "Ping Time, Ping Number, Beam Number, Easting, Northing, Depth, Longitude, Latitude, Backscatter Value, Corrected Backscatter Value, True Angle"))
        self.label_5.setText(_translate("Converter", "Separator"))
        self.shoraw.setText(_translate("Converter", "Raw"))
        self.showparsed.setText(_translate("Converter", "Parsed"))
        self.label_6.setText(_translate("Converter", "Delimiter White Space"))
        self.delimiterWS.setItemText(0, _translate("Converter", "True"))
        self.delimiterWS.setItemText(1, _translate("Converter", "False"))
        self.convert.setText(_translate("Converter", "Convert"))

