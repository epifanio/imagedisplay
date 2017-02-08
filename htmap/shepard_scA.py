#!/usr/local/bin/python36
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np

class ShepardA(QWidget):
    def __init__(self, qframe):
        self.shepardframeA = qframe
        self.mp = 1
        self.fontsize = 6
        self.initUI()

    def initUI(self):
        self.shepardsandgraphicsView = QtWidgets.QGraphicsView(self.shepardframeA)
        self.shepardsandgraphicsView.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.shepardsandgraphicsView.setStyleSheet("background-color: rgba(0,0,0,0%)")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shepardsandgraphicsView.sizePolicy().hasHeightForWidth())

        self.shepardsandgraphicsView.setSizePolicy(sizePolicy)
        self.shepardsandgraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shepardsandgraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shepardsandgraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.shepardsandgraphicsView.setObjectName("shepardsandgraphicsView")

        font = QFont()
        font.setPointSize(8)

        self.fx, self.fy = self.shepardframeA.size().width(), self.shepardframeA.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.shepardsandgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardsandgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.drawbuttons(self.mp)

    def createScene(self):
        self.shepardframeA.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardframeA.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardsandgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardsandgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.fx, self.fy)

        #item.setTransform(QTransform().fromTranslate(0.02 * self.fx, 0.7 * self.fy), True)
        # draw borders
        #self.scene.addLine(QLineF(0, self.fy, self.fx/2., 0),
        #                   QPen(QBrush(Qt.red), 3, Qt.SolidLine))
        #self.scene.addLine(QLineF(self.fx/2., 0, self.fx, self.fx),
        #                   QPen(QBrush(Qt.red), 3, Qt.SolidLine))
        #
        # Add labels
        ylabel = self.scene.addSimpleText("Percent of Sand")
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
            QtCore.QPoint(self.fx * 0.375, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.625, self.fy * 0.25)])
        self.A2 = QPolygonF([
            QtCore.QPoint(self.fx * 0.375, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.42, self.fy * 0.59),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.42),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25)])
        self.A3 = QPolygonF([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.42),
            QtCore.QPoint(self.fx * 0.58, self.fy * 0.59),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.625, self.fy * 0.25)])
        self.A4 = QPolygonF([
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.125, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.19, self.fy * 0.88),
            QtCore.QPoint(self.fx * 0.33, self.fy * 0.78),
            QtCore.QPoint(self.fx * 0.42, self.fy * 0.59)])
        #self.A5 = QPolygonF([
        #    QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
        #    QtCore.QPoint(self.fx * 0.36, self.fy * 0.75),
        #    QtCore.QPoint(self.fx * 0.64, self.fy * 0.75)])
        self.A5 = QPolygonF([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.42),
            QtCore.QPoint(self.fx * 0.33, self.fy * 0.78),
            QtCore.QPoint(self.fx * 0.67, self.fy * 0.78)])
        self.A6 = QPolygonF([
            QtCore.QPoint(self.fx * 0.58, self.fy * 0.59),
            QtCore.QPoint(self.fx * 0.67, self.fy * 0.78),
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.88),
            QtCore.QPoint(self.fx * 0.875, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50)])
        self.A7 = QPolygonF([
            QtCore.QPoint(self.fx * 0.125, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.0, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0)])
        self.A8 = QPolygonF([
            QtCore.QPoint(self.fx * 0.33, self.fy * 0.78),
            QtCore.QPoint(self.fx * 0.19, self.fy * 0.88),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.78)])
        self.A9 = QPolygonF([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.78),
            QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.75, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.88),
            QtCore.QPoint(self.fx * 0.67, self.fy * 0.78)])
        self.A10 = QPolygonF([
            QtCore.QPoint(self.fx * 0.875, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 1.0),
            QtCore.QPoint(self.fx * 1.00, self.fy * 1.0)])

        self.SC1 = self.scene.addPolygon(self.A1,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(156, 101, 0, 100)))
        self.SC2 = self.scene.addPolygon(self.A2,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 50, 0, 100)))
        self.SC3 = self.scene.addPolygon(self.A3,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(100, 155, 100, 100)))
        self.SC4 = self.scene.addPolygon(self.A4,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(0, 100, 0, 100)))
        self.SC5 = self.scene.addPolygon(self.A5,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(250, 0, 100, 100)))
        self.SC6 = self.scene.addPolygon(self.A6,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(155, 0, 100, 100)))
        self.SC7 = self.scene.addPolygon(self.A7,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 255, 0, 100)))
        self.SC8 = self.scene.addPolygon(self.A8,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(0, 100, 255, 100)))
        self.SC9 = self.scene.addPolygon(self.A9,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(50, 0, 100, 100)))
        self.SC10 = self.scene.addPolygon(self.A10,
                                          QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                          QBrush(QColor(255, 100, 100, 100)))

        # draw ticks

        tick1 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick1.setTransform(QTransform().fromTranslate(self.A1.first().x(),
                                                      self.A1.first().y()+1), True)
        tick1.update()
        tick1.setTransform(QTransform().rotate(135), True)
        tick1.update()

        tick2 = self.scene.addLine(QLineF(0,0, self.fx/30., self.fy/30.),
                                              QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick2.setTransform(QTransform().fromTranslate(self.A2.first().x(),
                                                      self.A2.first().y()), True)
        tick2.update()
        tick2.setTransform(QTransform().rotate(162), True)
        tick2.update()

        tick3 = self.scene.addLine(QLineF(0,0, self.fx/30., self.fy/30.),
                                              QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick3.setTransform(QTransform().fromTranslate(self.A4.first().x(),
                                                      self.A4.first().y()), True)
        tick3.update()
        tick3.setTransform(QTransform().rotate(162), True)
        tick3.update()

        tick4 = self.scene.addLine(QLineF(0,0, self.fx/30., self.fy/30.),
                                              QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick4.setTransform(QTransform().fromTranslate(self.A7.first().x(),
                                                      self.A7.first().y()), True)
        tick4.update()
        tick4.setTransform(QTransform().rotate(162), True)
        tick4.update()

        tick5 = self.scene.addLine(QLineF(0, 0, self.fx/30., self.fy/30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick5.setTransform(QTransform().fromTranslate(1, self.fy-2), True)
        tick5.update()
        tick5.setTransform(QTransform().rotate(225), True)
        tick5.update()

        tick6 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick6.setTransform(QTransform().fromTranslate(self.A3.last().x(),
                                                      self.A3.last().y()), True)
        tick6.update()
        tick6.setTransform(QTransform().rotate(-70), True)
        tick6.update()

        tick7 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick7.setTransform(QTransform().fromTranslate(self.A6.last().x(), self.A6.last().y()), True)
        tick7.update()
        tick7.setTransform(QTransform().rotate(-70), True)
        tick7.update()

        tick8 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick8.setTransform(QTransform().fromTranslate(self.A10.first().x(), self.A10.first().y()), True)
        tick8.update()
        tick8.setTransform(QTransform().rotate(-70), True)
        tick8.update()

        tick9 = self.scene.addLine(QLineF(0, 0, self.fx / 30., self.fy / 30.),
                                   QPen(QBrush(Qt.darkGray), 2, Qt.DashLine))
        tick9.setTransform(QTransform().fromTranslate(self.A10.last().x()-1, self.A10.last().y()-2), True)
        tick9.update()
        tick9.setTransform(QTransform().rotate(-135), True)
        tick9.update()

        font = QFont()
        font.setPointSize(self.fx / 25.)

        L1 = self.scene.addSimpleText("Clay")
        L1.setTransform(QTransform().fromTranslate(self.fx * 0.45, self.fy * 0.12), True)
        L1.setFont(font)
        L1.setBrush(QColor(0, 0, 0, 160))

        L2 = self.scene.addSimpleText("Sandy \n Clay")
        L2.setTransform(QTransform().fromTranslate(self.fx * 0.35, self.fy * 0.35), True)
        L2.setFont(font)
        L2.setBrush(QColor(0, 0, 0, 160))

        L3 = self.scene.addSimpleText("Silty \n Clay")
        L3.setTransform(QTransform().fromTranslate(self.fx * 0.55, self.fy * 0.35), True)
        L3.setFont(font)
        L3.setBrush(QColor(0, 0, 0, 160))

        L4 = self.scene.addSimpleText("Clayey \n Sand")
        L4.setTransform(QTransform().fromTranslate(self.fx * 0.22, self.fy * 0.58), True)
        L4.setFont(font)
        L4.setBrush(QColor(0, 0, 0, 160))

        L5 = self.scene.addSimpleText("Sand \n Silt \n Clay")
        L5.setTransform(QTransform().fromTranslate(self.fx * 0.45, self.fy * 0.56), True)
        L5.setFont(font)
        L5.setBrush(QColor(0, 0, 0, 160))

        L6 = self.scene.addSimpleText("Clayey \n Silt")
        L6.setTransform(QTransform().fromTranslate(self.fx * 0.65, self.fy * 0.58), True)
        L6.setFont(font)
        L6.setBrush(QColor(0, 0, 0, 160))

        L7 = self.scene.addSimpleText("Sand")
        L7.setTransform(QTransform().fromTranslate(self.fx * 0.08, self.fy * 0.88), True)
        L7.setFont(font)
        L7.setBrush(QColor(0, 0, 0, 160))

        L8 = self.scene.addSimpleText("Silt \n Sand")
        L8.setTransform(QTransform().fromTranslate(self.fx * 0.32, self.fy * 0.83), True)
        L8.setFont(font)
        L8.setBrush(QColor(0, 0, 0, 160))

        L9 = self.scene.addSimpleText("Sandy \n Silt")
        L9.setTransform(QTransform().fromTranslate(self.fx * 0.58, self.fy * 0.83), True)
        L9.setFont(font)
        L9.setBrush(QColor(0, 0, 0, 160))

        L10 = self.scene.addSimpleText("Silt")
        L10.setTransform(QTransform().fromTranslate(self.fx * 0.84, self.fy * 0.88), True)
        L10.setFont(font)
        L10.setBrush(QColor(0, 0, 0, 160))

        L1.update()
        L2.update()
        L3.update()
        L4.update()
        L5.update()
        L6.update()
        L7.update()
        L8.update()
        L9.update()
        L10.update()

        self.shepardsandgraphicsView.setScene(self.scene)

    def drawbuttons(self, mp):
        self.mp = mp
        self.fx, self.fy = self.shepardframeA.size().width(), self.shepardframeA.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.shepardframeA.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.shepardframeA.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.createScene()

    def printer(self):
        print('meee')