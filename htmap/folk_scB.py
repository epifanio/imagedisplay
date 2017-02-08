#!/usr/local/bin/python36
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np

class FolkB(QWidget):
    def __init__(self, qframe):
        self.folkframeB = qframe
        self.mp = 1
        self.fontsize = 6
        self.initUI()

    def initUI(self):
        self.folksandgraphicsView = QtWidgets.QGraphicsView(self.folkframeB)
        self.folksandgraphicsView.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.folksandgraphicsView.setStyleSheet("background-color: rgba(0,0,0,0%)")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folksandgraphicsView.sizePolicy().hasHeightForWidth())

        self.folksandgraphicsView.setSizePolicy(sizePolicy)
        self.folksandgraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.folksandgraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.folksandgraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.folksandgraphicsView.setObjectName("folksandgraphicsView")

        font = QFont()
        font.setPointSize(8)

        self.fx, self.fy = self.folkframeB.size().width(), self.folkframeB.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.folksandgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.folksandgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))

        self.drawbuttons(self.mp)


    def createScene(self):
        self.folkframeB.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.folkframeB.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.folksandgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.folksandgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.fx, self.fy)

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
        #self.A0 = QPolygonF([
        #    QtCore.QPoint(self.fx * 0.5, self.fy * 0.0),
        #    QtCore.QPoint(self.fx * 0, self.fy * 1),
        #    QtCore.QPoint(self.fx * 1, self.fy * 1)])
        self.A1 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.0),
            QtCore.QPoint(self.fx * 0.4, self.fy * 0.2),
            QtCore.QPoint(self.fx * 0.6, self.fy * 0.2)])
        self.A2 = QPolygonF([
            QtCore.QPoint(self.fx * 0.4, self.fy * 0.2),
            QtCore.QPoint(self.fx * 0.2, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.2)])
        self.A3 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.2),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.735, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.58, self.fy * 0.2)])
        self.A4 = QPolygonF([
            QtCore.QPoint(self.fx * 0.58, self.fy * 0.2),
            QtCore.QPoint(self.fx * 0.735, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.8, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.6, self.fy * 0.2)])
        self.A5 = QPolygonF([
            QtCore.QPoint(self.fx * 0.2, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.1, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.6)])
        self.A6 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.735, self.fy * 0.6)])
        self.A7 = QPolygonF([
            QtCore.QPoint(self.fx * 0.735, self.fy * 0.6),
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.9, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.8, self.fy * 0.6)])
        self.A8 = QPolygonF([
            QtCore.QPoint(self.fx * 0.1, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.05, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.15, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.19, self.fy * 0.8)])
        self.A9 = QPolygonF([
            QtCore.QPoint(self.fx * 0.19, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.15, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.8)])
        self.A10 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.85, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.8)])
        self.A11 = QPolygonF([
            QtCore.QPoint(self.fx * 0.81, self.fy * 0.8),
            QtCore.QPoint(self.fx * 0.85, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.95, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.9, self.fy * 0.8)])
        self.A12 = QPolygonF([
            QtCore.QPoint(self.fx * 0.05, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.0, self.fy * 1),
            QtCore.QPoint(self.fx * 0.12, self.fy * 1),
            QtCore.QPoint(self.fx * 0.15, self.fy * 0.90)])
        self.A13 = QPolygonF([
            QtCore.QPoint(self.fx * 0.15, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.12, self.fy * 1),
            QtCore.QPoint(self.fx * 0.5, self.fy * 1),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.90)])
        self.A14 = QPolygonF([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.5, self.fy * 1),
            QtCore.QPoint(self.fx * 0.89, self.fy * 1),
            QtCore.QPoint(self.fx * 0.85, self.fy * 0.90)])
        self.A15 = QPolygonF([
            QtCore.QPoint(self.fx * 0.85, self.fy * 0.90),
            QtCore.QPoint(self.fx * 0.89, self.fy * 1),
            QtCore.QPoint(self.fx * 1, self.fy * 1),
            QtCore.QPoint(self.fx * 0.95, self.fy * 0.90)])


        #self.SC0 = self.scene.addPolygon(self.A0,
        #                                 QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
        #                                 QBrush(QColor(100, 155, 200, 100)))

        self.SC1 = self.scene.addPolygon(self.A1,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 0, 0, 100)))

        self.SC2 = self.scene.addPolygon(self.A2,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC3 = self.scene.addPolygon(self.A3,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))

        self.SC4 = self.scene.addPolygon(self.A4,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))

        self.SC5 = self.scene.addPolygon(self.A5,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC6 = self.scene.addPolygon(self.A6,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC7 = self.scene.addPolygon(self.A7,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC8 = self.scene.addPolygon(self.A8,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC9 = self.scene.addPolygon(self.A9,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC10 = self.scene.addPolygon(self.A10,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC11 = self.scene.addPolygon(self.A11,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC12 = self.scene.addPolygon(self.A12,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC13 = self.scene.addPolygon(self.A13,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC14 = self.scene.addPolygon(self.A14,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
        self.SC15 = self.scene.addPolygon(self.A15,
                                         QPen(QBrush(Qt.darkGray), 3, Qt.SolidLine),
                                         QBrush(QColor(255, 223, 155, 100)))
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

        #self.scene.addLine(QLineF(self.fx/2., 0, self.fx/9., self.fy),
        #                   QPen(QBrush(Qt.red), 3, Qt.SolidLine))

        self.folksandgraphicsView.setScene(self.scene)

    def drawbuttons(self, mp):
        self.mp = mp
        self.fx, self.fy = self.folkframeB.size().width(), self.folkframeB.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.folkframeB.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.folkframeB.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.createScene()

    def printer(self):
        print('meee')