#!/usr/local/bin/python36
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWidgets

from htmapui import HtMapGui
from shepard_scA import ShepardA
from shepard_scB import ShepardB
from folk_scA import FolkA
from folk_scB import FolkB

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class VerticalLabel(QLabel):

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        painter = QPainter (self)
        painter.translate(0, self.height()-1)
        painter.rotate(-90)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QLabel.render(self, painter)
        painter.end()

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())


class MyLabel(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QtCore.Qt.black)
        painter.translate(20, 100)
        painter.rotate(-90)
        painter.drawText(0, 0, "hellos")
        painter.end()


class line(QWidget):
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.darkGray,3))
        painter.drawLine(self.p1,self.p2)
        painter.end()


class MapDisplay(QObject):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.modifiers = QApplication.keyboardModifiers()
        self.w = HtMapGui()
        self.w.webEngineView_map.installEventFilter(self)
        self.w.webEngineView_map.setObjectName("webEngineView_map")
        self.w.webEngineView_map.load(QUrl('file:///Users/epi/pyqtwebtest.html'))
        #self.w.actionAddmarker.triggered.connect(self.updatebounds)
        self.w.actionAddmarker.triggered.connect(self.showmarkernote)
        self.w.actionHtmlExport.triggered.connect(self.gethtml)
        #self.w.actionAddmarker.triggered.connect(self.addMarker)
        #self.w.addMarker.clicked.connect(self.updatebounds)
        #self.w.setMouseTracking(True)
        self.w.webEngineView_map.installEventFilter(self)
        self.w.markerBox.hide()
        self.w.latitude = QLineEdit()
        self.w.longitude = QLineEdit()
        self.w.latitude.setFixedWidth(140)
        self.w.longitude.setFixedWidth(140)
        #self.w.latitude.setMaximumSize(QtCore.QSize(140, 0))
        #self.w.longitude.setMaximumSize(QtCore.QSize(140, 0))
        self.w.statusbar.addPermanentWidget(self.w.latitude, stretch=0)
        self.w.statusbar.addPermanentWidget(self.w.longitude, stretch=0)
        self.mp = 1
        self.fontsize = 6
        self.sc = ShepardA(self.w.shepardframeA)
        self.fc = ShepardB(self.w.shepardframeB)

        self.fkA = FolkA(self.w.folkframeA)
        self.fkB = FolkB(self.w.folkframeB)

        self.w.increaseCS.clicked.connect(self.increaseCS)
        self.w.decreaseCS.clicked.connect(self.decreaseCS)
        self.w.show()

    def increaseCS(self):
        self.mp=1.1
        #self.fontsize=self.fontsize*self.mp
        #print(self.fontsize)
        self.sc.drawbuttons(self.mp)
        self.fc.drawbuttons(self.mp)
        self.fkA.drawbuttons(self.mp)
        self.fkB.drawbuttons(self.mp)


    def decreaseCS(self):
        self.mp=0.9
        #self.fontsize = self.fontsize*self.mp
        #print(self.fontsize)
        self.sc.drawbuttons(self.mp)
        self.fc.drawbuttons(self.mp)
        self.fkA.drawbuttons(self.mp)
        self.fkB.drawbuttons(self.mp)

    def showmarkernote(self):
        if self.w.actionAddmarker.isChecked():
            self.w.markerBox.show()
        else:
            self.w.markerBox.hide()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove and self.w.webEngineView_map.underMouse():
            #print('i am alive')
            # QtCore.Qt.NoButton
            # QtCore.Qt.LeftButton
            # QtCore.Qt.RightButton
            pos = event.pos()
            self.w.webEngineView_map.page().runJavaScript(
                "map.containerPointToLatLng(L.point(%s, %s))" % (pos.x(), pos.y()), self.getposition)

            #if event.buttons() == QtCore.Qt.LeftButton:
            #    pos = event.pos()
            #    print("mouse click")
            #    #self.edit.setText('no button: %d, y: %d' % (pos.x(), pos.y()))
            #    self.w.webEngineView_map.page().runJavaScript("[map.containerPointToLatLng(L.point(%s, %s))]" % (pos.x(), pos.y()), self.getposition)
            #elif event.buttons() == QtCore.Qt.LeftButton:
            #    pos = event.pos()
            #    self.w.webEngineView_map.page().runJavaScript("[map.containerPointToLatLng(L.point(%s, %s))]" % (pos.x(), pos.y()), self.getposition)
            #    #self.onmouseclick()
            #elif event.buttons() == QtCore.Qt.RightButton:
            #    pos = event.pos()
            #    self.w.webEngineView_map.page().runJavaScript("L.marker([%s,%s]).bindPopup('%s').addTo(%s)" % (
            #    self.w.latitude.text(), self.w.longitude.text(), str(self.w.marker_description.text()),
            #    self.w.marker_type.currentText()))

                #pass # do other stuff

        elif event.type() == QtCore.QEvent.MouseButtonPress and self.w.webEngineView_map.underMouse():
            if self.w.actionAddmarker.isChecked():
                print(str(self.w.marker_description.toPlainText()))
                cursor = self.w.marker_description.textCursor()
                print(cursor.selectionStart(), cursor.selectionEnd())
                text = str(self.w.marker_description.toPlainText()).replace('\n','<br>')
                self.w.webEngineView_map.page().runJavaScript("L.marker([%s,%s], {icon: greenIcon}).bindPopup('%s').addTo(%s)" % (self.position['lat'],
                                                                                                               self.position['lng'],
                                                                                                               text,
                                                                                                               self.w.marker_type.currentText()))
        # Handle SC graphic
        if event.type() == QtCore.QEvent.MouseButtonPress and source.objectName() == 'shepardsandgraphicsView':
            print(source.objectName())
            pos = event.pos()
            if event.buttons() == QtCore.Qt.LeftButton:
                print(float(pos.x())/source.size().width(), float(pos.y())/source.size().height())
                if self.sc.SC1.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC1.isSelected():
                        self.sc.SC1.setBrush(QBrush(Qt.red))
                        #self.sc.SC1.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC1.setSelected(True)

                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC1 already selected')

                elif self.sc.SC2.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC2.isSelected():
                        self.sc.SC2.setBrush(QBrush(Qt.red))
                        #self.sc.SC2.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC2.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC2 already selected')
                elif self.sc.SC3.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC3.isSelected():
                        self.sc.SC3.setBrush(QBrush(Qt.red))
                        #self.sc.SC3.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC3.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC3 already selected')
                elif self.sc.SC4.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC4.isSelected():
                        self.sc.SC4.setBrush(QBrush(Qt.red))
                        #self.sc.SC4.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC4.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC4 already selected')
                elif self.sc.SC5.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC5.isSelected():
                        self.sc.SC5.setBrush(QBrush(Qt.red))
                        #self.sc.SC5.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC5.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC5 already selected')
                elif self.sc.SC6.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC6.isSelected():
                        self.sc.SC6.setBrush(QBrush(Qt.red))
                        #self.sc.SC6.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC6.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC6 already selected')
                elif self.sc.SC7.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC7.isSelected():
                        self.sc.SC7.setBrush(QBrush(Qt.red))
                        #self.sc.SC7.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC7.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC7 already selected')
                elif self.sc.SC8.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC8.isSelected():
                        self.sc.SC8.setBrush(QBrush(Qt.red))
                        #self.sc.SC8.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC8.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC8 already selected')
                elif self.sc.SC9.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC9.isSelected():
                        self.sc.SC9.setBrush(QBrush(Qt.red))
                        #self.sc.SC9.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC9.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
                    else:
                        print('SC9 already selected')
                elif self.sc.SC10.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC10.isSelected():
                        self.sc.SC10.setBrush(QBrush(Qt.red))
                        #self.sc.SC10.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.sc.SC10.setSelected(True)

                        self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                        self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                        self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                        self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                        self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                        self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                        self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                    else:
                        print('SC10 already selected')

                else:
                    print('this is outside the triangles, set all to unselected')
                    self.sc.SC1.setSelected(False)
                    self.sc.SC2.setSelected(False)
                    self.sc.SC3.setSelected(False)
                    self.sc.SC4.setSelected(False)
                    self.sc.SC5.setSelected(False)
                    self.sc.SC6.setSelected(False)
                    self.sc.SC7.setSelected(False)
                    self.sc.SC8.setSelected(False)
                    self.sc.SC9.setSelected(False)
                    self.sc.SC10.setSelected(False)
                    self.sc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                    self.sc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                    self.sc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                    self.sc.SC4.setBrush(QBrush(QColor(0, 100, 0, 100)))
                    self.sc.SC5.setBrush(QBrush(QColor(250, 0, 100, 100)))
                    self.sc.SC6.setBrush(QBrush(QColor(155, 0, 100, 100)))
                    self.sc.SC7.setBrush(QBrush(QColor(255, 255, 0, 100)))
                    self.sc.SC8.setBrush(QBrush(QColor(0, 100, 255, 100)))
                    self.sc.SC9.setBrush(QBrush(QColor(50, 0, 100, 100)))
                    self.sc.SC10.setBrush(QBrush(QColor(255, 100, 100, 100)))
        if event.type() == QtCore.QEvent.MouseButtonPress and source.objectName() == 'shepardgravelgraphicsView':
            pos = event.pos()
            if event.buttons() == QtCore.Qt.LeftButton:
                print(float(pos.x())/source.size().width(), float(pos.y())/source.size().height())
                if self.fc.SC1.contains(QPointF(pos.x(), pos.y())):
                    if not self.sc.SC1.isSelected():
                        self.fc.SC1.setBrush(QBrush(Qt.red))
                        #self.sc.SC1.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fc.SC1.setSelected(True)

                        self.fc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                        self.fc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                    else:
                        print('FC1 already selected')

                elif self.fc.SC2.contains(QPointF(pos.x(), pos.y())):
                    if not self.fc.SC2.isSelected():
                        self.fc.SC2.setBrush(QBrush(Qt.red))
                        #self.sc.SC2.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fc.SC2.setSelected(True)

                        self.fc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.fc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))
                    else:
                        print('FC2 already selected')
                elif self.fc.SC3.contains(QPointF(pos.x(), pos.y())):
                    if not self.fc.SC3.isSelected():
                        self.fc.SC3.setBrush(QBrush(Qt.red))
                        #self.sc.SC3.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fc.SC3.setSelected(True)

                        self.fc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                        self.fc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                    else:
                        print('FC3 already selected')
                else:
                    print('this is outside the triangles, set all to unselected')
                    self.fc.SC1.setSelected(False)
                    self.fc.SC2.setSelected(False)
                    self.fc.SC3.setSelected(False)
                    self.fc.SC1.setBrush(QBrush(QColor(156, 101, 0, 100)))
                    self.fc.SC2.setBrush(QBrush(QColor(255, 50, 0, 100)))
                    self.fc.SC3.setBrush(QBrush(QColor(100, 155, 100, 100)))

        if event.type() == QtCore.QEvent.MouseButtonPress and source.objectName() == 'folkgravelgraphicsView':
            pos = event.pos()
            if event.buttons() == QtCore.Qt.LeftButton:
                print(float(pos.x())/source.size().width(), float(pos.y())/source.size().height())
                if self.fkA.SC1.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC1.isSelected():
                        self.fkA.SC1.setBrush(QBrush(Qt.red))
                        self.fkA.SC1.setSelected(True)

                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))



                    else:
                        print('FC1 already selected')

                elif self.fkA.SC2.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC2.isSelected():
                        self.fkA.SC2.setBrush(QBrush(Qt.red))
                        self.fkA.SC2.setSelected(True)

                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC2 already selected')
                elif self.fkA.SC3.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC3.isSelected():
                        self.fkA.SC3.setBrush(QBrush(Qt.red))
                        self.fkA.SC3.setSelected(True)

                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC3 already selected')
                elif self.fkA.SC4.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC4.isSelected():
                        self.fkA.SC4.setBrush(QBrush(Qt.red))
                        self.fkA.SC4.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC4 already selected')
                elif self.fkA.SC5.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC5.isSelected():
                        self.fkA.SC5.setBrush(QBrush(Qt.red))
                        #self.sc.SC5.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC5.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC5 already selected')
                elif self.fkA.SC6.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC6.isSelected():
                        self.fkA.SC6.setBrush(QBrush(Qt.red))
                        #self.sc.SC6.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC6.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC6 already selected')
                elif self.fkA.SC7.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC7.isSelected():
                        self.fkA.SC7.setBrush(QBrush(Qt.red))
                        #self.sc.SC7.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC7.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC7 already selected')
                elif self.fkA.SC8.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC8.isSelected():
                        self.fkA.SC8.setBrush(QBrush(Qt.red))
                        # self.sc.SC8.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC8.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC8 already selected')
                elif self.fkA.SC9.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC9.isSelected():
                        self.fkA.SC9.setBrush(QBrush(Qt.red))
                        # self.sc.SC9.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC9.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC9 already selected')
                elif self.fkA.SC10.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC10.isSelected():
                        self.fkA.SC10.setBrush(QBrush(Qt.red))
                        # self.sc.SC10.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC10.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC10 already selected')
                elif self.fkA.SC11.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC11.isSelected():
                        self.fkA.SC11.setBrush(QBrush(Qt.red))
                        # self.sc.SC11.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC11.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC11 already selected')
                elif self.fkA.SC12.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC12.isSelected():
                        self.fkA.SC12.setBrush(QBrush(Qt.red))
                        # self.sc.SC12.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC12.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC12 already selected')
                elif self.fkA.SC13.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC13.isSelected():
                        self.fkA.SC13.setBrush(QBrush(Qt.red))
                        # self.sc.SC13.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC13.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC13 already selected')
                elif self.fkA.SC14.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC14.isSelected():
                        self.fkA.SC14.setBrush(QBrush(Qt.red))
                        # self.sc.SC14.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC14.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC14 already selected')
                elif self.fkA.SC15.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkA.SC15.isSelected():
                        self.fkA.SC15.setBrush(QBrush(Qt.red))
                        # self.sc.SC15.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkA.SC15.setSelected(True)
                        self.fkA.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC15 already selected')
                else:
                    print('this is outside the triangles, set all to unselected')
                    self.fkA.SC1.setSelected(False)
                    self.fkA.SC2.setSelected(False)
                    self.fkA.SC3.setSelected(False)
                    self.fkA.SC4.setSelected(False)
                    self.fkA.SC5.setSelected(False)
                    self.fkA.SC6.setSelected(False)
                    self.fkA.SC7.setSelected(False)
                    self.fkA.SC8.setSelected(False)
                    self.fkA.SC9.setSelected(False)
                    self.fkA.SC10.setSelected(False)
                    self.fkA.SC11.setSelected(False)
                    self.fkA.SC12.setSelected(False)
                    self.fkA.SC13.setSelected(False)
                    self.fkA.SC14.setSelected(False)
                    self.fkA.SC15.setSelected(False)
                    self.fkA.SC1.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkA.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))

        if event.type() == QtCore.QEvent.MouseButtonPress and source.objectName() == 'folksandgraphicsView':
            pos = event.pos()
            if event.buttons() == QtCore.Qt.LeftButton:
                print(float(pos.x())/source.size().width(), float(pos.y())/source.size().height())
                if self.fkB.SC1.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC1.isSelected():
                        self.fkB.SC1.setBrush(QBrush(Qt.red))
                        self.fkB.SC1.setSelected(True)

                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))



                    else:
                        print('FC1 already selected')

                elif self.fkB.SC2.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC2.isSelected():
                        self.fkB.SC2.setBrush(QBrush(Qt.red))
                        self.fkB.SC2.setSelected(True)

                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC2 already selected')
                elif self.fkB.SC3.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC3.isSelected():
                        self.fkB.SC3.setBrush(QBrush(Qt.red))
                        self.fkB.SC3.setSelected(True)

                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC3 already selected')
                elif self.fkB.SC4.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC4.isSelected():
                        self.fkB.SC4.setBrush(QBrush(Qt.red))
                        self.fkB.SC4.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC4 already selected')
                elif self.fkB.SC5.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC5.isSelected():
                        self.fkB.SC5.setBrush(QBrush(Qt.red))
                        #self.sc.SC5.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC5.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC5 already selected')
                elif self.fkB.SC6.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC6.isSelected():
                        self.fkB.SC6.setBrush(QBrush(Qt.red))
                        #self.sc.SC6.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC6.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC6 already selected')
                elif self.fkB.SC7.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC7.isSelected():
                        self.fkB.SC7.setBrush(QBrush(Qt.red))
                        #self.sc.SC7.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC7.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC7 already selected')
                elif self.fkB.SC8.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC8.isSelected():
                        self.fkB.SC8.setBrush(QBrush(Qt.red))
                        # self.sc.SC8.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC8.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC8 already selected')
                elif self.fkB.SC9.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC9.isSelected():
                        self.fkB.SC9.setBrush(QBrush(Qt.red))
                        # self.sc.SC9.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC9.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC9 already selected')
                elif self.fkB.SC10.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC10.isSelected():
                        self.fkB.SC10.setBrush(QBrush(Qt.red))
                        # self.sc.SC10.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC10.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC10 already selected')
                elif self.fkB.SC11.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC11.isSelected():
                        self.fkB.SC11.setBrush(QBrush(Qt.red))
                        # self.sc.SC11.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC11.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC11 already selected')
                elif self.fkB.SC12.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC12.isSelected():
                        self.fkB.SC12.setBrush(QBrush(Qt.red))
                        # self.sc.SC12.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC12.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC12 already selected')
                elif self.fkB.SC13.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC13.isSelected():
                        self.fkB.SC13.setBrush(QBrush(Qt.red))
                        # self.sc.SC13.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC13.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC13 already selected')
                elif self.fkB.SC14.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC14.isSelected():
                        self.fkB.SC14.setBrush(QBrush(Qt.red))
                        # self.sc.SC14.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC14.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC14 already selected')
                elif self.fkB.SC15.contains(QPointF(pos.x(), pos.y())):
                    if not self.fkB.SC15.isSelected():
                        self.fkB.SC15.setBrush(QBrush(Qt.red))
                        # self.sc.SC15.setPen(QPen(QBrush(Qt.yellow), 3, Qt.SolidLine))
                        self.fkB.SC15.setSelected(True)
                        self.fkB.SC1.setBrush(QBrush(QColor(255, 0, 0, 100)))
                        self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                        self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    else:
                        print('FC15 already selected')
                else:
                    print('this is outside the triangles, set all to unselected')
                    self.fkB.SC1.setSelected(False)
                    self.fkB.SC2.setSelected(False)
                    self.fkB.SC3.setSelected(False)
                    self.fkB.SC4.setSelected(False)
                    self.fkB.SC5.setSelected(False)
                    self.fkB.SC6.setSelected(False)
                    self.fkB.SC7.setSelected(False)
                    self.fkB.SC8.setSelected(False)
                    self.fkB.SC9.setSelected(False)
                    self.fkB.SC10.setSelected(False)
                    self.fkB.SC11.setSelected(False)
                    self.fkB.SC12.setSelected(False)
                    self.fkB.SC13.setSelected(False)
                    self.fkB.SC14.setSelected(False)
                    self.fkB.SC15.setSelected(False)
                    self.fkB.SC1.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC2.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC3.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC4.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC5.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC6.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC7.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC8.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC9.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC10.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC11.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC12.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC13.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC14.setBrush(QBrush(QColor(255, 223, 155, 100)))
                    self.fkB.SC15.setBrush(QBrush(QColor(255, 223, 155, 100)))

        return QtWidgets.QMainWindow.eventFilter(self, source, event)

    def updateposition(self):
        self.w.webEngineView_map.page().runJavaScript("map.containerPointToLatLng(L.point(e.layerPoint.x, e.layerPoint.y))", self.getposition)

    def getposition(self, position):
        self.position = position
        try:
            #self.w.statusbar.showMessage("%s, %s" % (self.position['lat'], self.position['lng']))
            self.w.latitude.setText(str(self.position['lat']))
            self.w.longitude.setText(str(self.position['lng']))
        except:
            print("position not set yet")

    def updatebounds(self):
        self.w.webEngineView_map.page().runJavaScript("[map.getBounds().getSouthWest().lat, \
                                            map.getBounds().getSouthWest().lng, \
                                            map.getBounds().getNorthEast().lat, \
                                            map.getBounds().getNorthEast().lng]",
                                        self.getbounds)

    def getbounds(self, bounds):
        self.w.marker_description.setText(str(bounds))
        self.bounds = bounds
        self.w.statusbar.showMessage("LL-UR Boundary %s" % self.bounds)
        print(self.bounds)


    def gethtml(self):
        self.w.webEngineView_map.page().toHtml(self.printsrc)

    def printsrc(self, html):
        print(html)


    #def addMarker(self):
    #    self.w.webEngineView_map.page().runJavaScript("L.marker([%s,%s]).bindPopup('%s').addTo(%s)" % (self.w.latitude.text(), self.w.longitude.text(), str(self.w.marker_description.text()), self.w.marker_type.currentText()))
    #    print(self.w.marker_description.text())

    #def mouseMoveEvent(self, event):
    #    print('mouseMoveEvent: x=%d, y=%d' % (event.x(), event.y()))

        #self.w.webEngineView_map.page().runJavaScript("L.marker([%s, %s]).bindPopup('This is Littleton, CO.').addTo(cities)" % (self.w.MarkerLatSpinBox.value(), self.w.MarkerLonSpinBox.value()))
        #print(self.w.MarkerLatSpinBox.value())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = MapDisplay()
    p.__init__()
    app.installEventFilter(p)
    sys.exit(app.exec_())
