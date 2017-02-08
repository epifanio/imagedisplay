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




        self.p1.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p2.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p3.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p4.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p5.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p6.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p7.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p8.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p9.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))
        self.p10.setGeometry(QtCore.QRect(0, 0, self.fx, self.fy))

        self.p1.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p1.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p2.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p2.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p3.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p3.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p4.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p4.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p5.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p5.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p6.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p6.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p7.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p7.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p8.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p8.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p9.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p9.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.p10.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.p10.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.A1 = QPolygon([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.0), QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A2 = QPolygon([
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.25), QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.43, self.fy * 0.63), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25)])
        self.A3 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.57, self.fy * 0.63), QtCore.QPoint(self.fx * 0.75, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A4 = QPolygon([
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50), QtCore.QPoint(self.fx * 0.13, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.17, self.fy * 0.87), QtCore.QPoint(self.fx * 0.37, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.43, self.fy * 0.63)])
        self.A5 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.50), QtCore.QPoint(self.fx * 0.37, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.75)])
        self.A6 = QPolygon([
            QtCore.QPoint(self.fx * 0.57, self.fy * 0.63), QtCore.QPoint(self.fx * 0.63, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.83, self.fy * 0.87), QtCore.QPoint(self.fx * 0.87, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50)])
        self.A7 = QPolygon([
            QtCore.QPoint(self.fx * 0.13, self.fy * 0.75), QtCore.QPoint(self.fx * 0.0, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0)])
        self.A8 = QPolygon([
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.75), QtCore.QPoint(self.fx * 0.18, self.fy * 0.86),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0), QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.75)])
        self.A9 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.75), QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.75, self.fy * 1.0), QtCore.QPoint(self.fx * 0.83, self.fy * 0.87),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.75)])
        self.A10 = QPolygon([
            QtCore.QPoint(self.fx * 0.87, self.fy * 0.75), QtCore.QPoint(self.fx * 0.75, self.fy * 1.0),
            QtCore.QPoint(self.fx * 1.00, self.fy * 1.0)])

        self.region = QRegion(QRect(0, 0, self.fx, self.fy), QRegion.Rectangle)

        p1region = self.region.intersected(QRegion(self.A1))
        p2region = self.region.intersected(QRegion(self.A2))
        p3region = self.region.intersected(QRegion(self.A3))
        p4region = self.region.intersected(QRegion(self.A4))
        p5region = self.region.intersected(QRegion(self.A5))
        p6region = self.region.intersected(QRegion(self.A6))
        p7region = self.region.intersected(QRegion(self.A7))
        p8region = self.region.intersected(QRegion(self.A8))
        p9region = self.region.intersected(QRegion(self.A9))
        p10region = self.region.intersected(QRegion(self.A10))

        self.p1.setMask(p1region)
        self.p1.setStyleSheet("QPushButton { background-color: rgb(156, 101, 0) }"
                                "QPushButton:pressed { background-color: white }")

        self.p2.setMask(p2region)
        self.p2.setStyleSheet("QPushButton { background-color: rgb(255, 50, 0) }"
                                "QPushButton:pressed { background-color: white }")

        self.p3.setMask(p3region)
        self.p3.setStyleSheet("QPushButton { background-color: rgb(100, 155, 100) }"
                                "QPushButton:pressed { background-color: white }")

        self.p4.setMask(p4region)
        self.p4.setStyleSheet("QPushButton { background-color: rgb(0, 100, 0) }"
                                "QPushButton:pressed { background-color: white }")

        self.p5.setMask(p5region)
        self.p5.setStyleSheet("QPushButton { background-color: rgb(250, 0, 100) }"
                                "QPushButton:pressed { background-color: white }")

        self.p6.setMask(p6region)
        self.p6.setStyleSheet("QPushButton { background-color: rgb(155, 0, 100) }"
                                "QPushButton:pressed { background-color: white }")

        self.p7.setMask(p7region)
        self.p7.setStyleSheet("QPushButton { background-color: rgb(255, 255, 0) }"
                                "QPushButton:pressed { background-color: white }")

        self.p8.setMask(p8region)
        self.p8.setStyleSheet("QPushButton { background-color: rgb(0, 100, 255) }"
                                "QPushButton:pressed { background-color: white }")

        self.p9.setMask(p9region)
        self.p9.setStyleSheet("QPushButton { background-color: rgb(50, 0, 100) }"
                                "QPushButton:pressed { background-color: white }")

        self.p10.setMask(p10region)
        self.p10.setStyleSheet("QPushButton { background-color: rgb(255, 100, 100) }"
                                 "QPushButton:pressed { background-color: white }")

        self.p1.clicked.connect(self.p1print)
        self.p2.clicked.connect(self.p2print)
        self.p3.clicked.connect(self.p3print)
        self.p4.clicked.connect(self.p4print)
        self.p5.clicked.connect(self.p5print)
        self.p6.clicked.connect(self.p6print)
        self.p7.clicked.connect(self.p7print)
        self.p8.clicked.connect(self.p8print)
        self.p9.clicked.connect(self.p9print)
        self.p10.clicked.connect(self.p10print)


    def setValue(self, value):
        self.value = value


class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        self.label = QLabel("Marker description")
        self.txted = QLineEdit()
        self.lbled = QLabel("Enter position (eg: -33.89, 151.275)")
        self.pos = QLineEdit()
        self.group = QComboBox()
        self.group.addItems(["caves", "cities"])

        self.browser = QWebEngineView()
        #self.browser.load(QUrl('file:///Users/epi/gmap.html'))
        self.browser.load(QUrl('file:///Users/epi/basemap.html'))

        # html file available at:
        # https://gist.github.com/anonymous/4a745fa5b098a6afc2a84879858c83af
        print(dir(self.browser.page()))

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
        self.h3Box.addWidget(self.group)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h2Box)
        self.vbox.addLayout(self.h3Box)
        self.setLayout(self.vbox)

        self.addmarkerbutton.clicked.connect(self.addMarker)
        self.printsourcebutton.clicked.connect(self.getBounds)

        #self.printsourcebutton.clicked.connect(self.printsrc)


    def addMarker(self):
        # print(dir(self.pos))
        latlon = self.pos.text()
        print(latlon)
        # print(latlon)
        # self.browser.page().runJavaScript("addMarker(%s)" % latlon)
        self.browser.page().runJavaScript("L.marker([%s]).bindPopup('%s').addTo(%s)" % (latlon, self.txted.text(), self.group.currentText()))
        self.browser.page().runJavaScript("map.panTo([%s], 10)" % latlon)
        # setView / panTo


    # FROM JS to Python

    def getBounds(self):
        self.browser.page().runJavaScript("bounds = [map.getBounds().getSouthWest().lat, map.getBounds().getSouthWest().lng, map.getBounds().getNorthEast().lat, map.getBounds().getNorthEast().lng]" , print)


    def getZoom(self):
        pass

    def getCenter(self):
        pass


    # From Python to js
    def zoom_to(self):
        pass

    def addGeoJson(self):
        pass

    def addKML(self):
        pass

    def addImage(self):
        pass

    def addTiles(self):
        pass


    def printsrc(self):
        # import requests
        # sample_html = requests.get('http://stackoverflow.com/questions/17309288/importerror-no-module-named-requests').text
        # print(render(sample_html))
        # print(dir(self.browser.page()))
        # print(dir(self.browser))
        # print(self.browser.page().toHtml(self))
        # print(self.browser.page().url())
        # print((self.browser.page().toPlainText()))
        self.browser.page().toHtml(print)
        # print unicode(frame.toHtml()).encode('utf-8')




def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())