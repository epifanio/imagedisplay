#!/usr/local/bin/python36
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np

class ShepardB(QWidget):
    def __init__(self, qframe):
        self.shepardframeB = qframe
        self.mp = 1
        self.fontsize = 6
        self.initUI()

    def initUI(self):
        self.shepardgravelgraphicsView = QtWidgets.QGraphicsView(self.shepardframeB)
        self.shepardgravelgraphicsView.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.shepardgravelgraphicsView.setStyleSheet("background-color: rgba(0,0,0,0%)")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shepardgravelgraphicsView.sizePolicy().hasHeightForWidth())

        self.shepardgravelgraphicsView.setSizePolicy(sizePolicy)
        self.shepardgravelgraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shepardgravelgraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shepardgravelgraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.shepardgravelgraphicsView.setObjectName("shepardgravelgraphicsView")

        font = QFont()
        font.setPointSize(8)

        self.fx, self.fy = self.shepardframeB.size().width(), self.shepardframeB.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.shepardgravelgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardgravelgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.drawbuttons(self.mp)


    def createScene(self):
        self.shepardframeB.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardframeB.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardgravelgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardgravelgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.fx, self.fy)

        ylabel = self.scene.addSimpleText("Percent of Gravel")
        font = QFont()
        font.setPointSize(self.fx / 20.)
        ylabel.setFont(font)
        ylabel.setBrush(QColor(255, 0, 0, 127))
        ylabel.setTransform(QTransform().fromTranslate(0.0 * self.fx, 0.6 * self.fy), True)
        ylabel.update()
        ylabel.setTransform(QTransform().rotate(-90), True)
        ylabel.update()

        # Add polygons
        self.A1 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.0),
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.42, self.fy * 0.59),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.42),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.625, self.fy * 0.25)])
        self.A2 = QPolygonF([
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.07, self.fy * 0.86),
            QtCore.QPoint(self.fx * 0.93, self.fy * 0.86),
            QtCore.QPoint(self.fx * 0.625, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.42),
            QtCore.QPoint(self.fx * 0.42, self.fy * 0.59)])
        self.A3 = QPolygonF([
            QtCore.QPoint(self.fx * 0.07, self.fy * 0.86),
            QtCore.QPoint(self.fx * 0.0, self.fy * 1),
            QtCore.QPoint(self.fx * 1, self.fy * 1),
            QtCore.QPoint(self.fx * 0.93, self.fy * 0.86)])


        self.SC1 = self.scene.addPolygon(self.A1,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(156, 101, 0, 100)))
        self.SC2 = self.scene.addPolygon(self.A2,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 50, 0, 100)))
        self.SC3 = self.scene.addPolygon(self.A3,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(100, 155, 100, 100)))

        # draw ticks

        #tick1 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
        #                           QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        #tick1.setTransform(QTransform().fromTranslate(self.A1.first().x(),
        #                                              self.A1.first().y()+1), True)
        #tick1.update()
        #tick1.setTransform(QTransform().rotate(135), True)
        #tick1.update()

        tick2 = self.scene.addLine(QLineF(0,0, self.fx/30., self.fy/30.),
                                              QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick2.setTransform(QTransform().fromTranslate(self.A2.first().x(),
                                                      self.A2.first().y()), True)
        tick2.update()
        tick2.setTransform(QTransform().rotate(162), True)
        tick2.update()


        font = QFont()
        font.setPointSize(self.fx / 25.)

        L1 = self.scene.addSimpleText("Gravel")
        L1.setTransform(QTransform().fromTranslate(self.fx * 0.44, self.fy * 0.18), True)
        L1.setFont(font)
        L1.setBrush(QColor(0, 0, 0, 160))

        L2 = self.scene.addSimpleText("Gravelly Sediment")
        L2.setTransform(QTransform().fromTranslate(self.fx * 0.35, self.fy * 0.7), True)
        L2.setFont(font)
        L2.setBrush(QColor(0, 0, 0, 160))

        L3 = self.scene.addSimpleText("Sand, Silt, and Clay (Gravel < 10%)")
        L3.setTransform(QTransform().fromTranslate(self.fx * 0.15, self.fy * 0.90), True)
        L3.setFont(font)
        L3.setBrush(QColor(0, 0, 0, 160))

        #L4 = self.scene.addSimpleText("Clayey \n Sand")
        #L4.setTransform(QTransform().fromTranslate(self.fx * 0.22, self.fy * 0.62), True)
        #L4.setFont(font)
        #L4.setBrush(QColor(0, 0, 0, 160))



        L1.update()
        L2.update()
        L3.update()

        #self.scene.addLine(QLineF(self.fx/2., 0, self.fx, self.fy),
        #                   QPen(QBrush(Qt.red), 3, Qt.SolidLine))

        self.shepardgravelgraphicsView.setScene(self.scene)

    def drawbuttons(self, mp):
        self.mp = mp
        self.fx, self.fy = self.shepardframeB.size().width(), self.shepardframeB.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.shepardframeB.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardframeB.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.createScene()

    def printer(self):
        print('meee')