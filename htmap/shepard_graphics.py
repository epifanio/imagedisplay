#!/usr/local/bin/python36
#import sys

from PyQt5 import QtCore
#from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
#from PyQt5 import QtWidgets


def generatepolygons(frameshape):
    fx, fy = frameshape
    SC1={}
    SC1['classlevel'] = 'SC1',
    SC1['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC1['brush'] = {'color': '156, 101, 0'},
    SC1['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.5, fy * 0.0),
        QtCore.QPoint(fx * 0.37, fy * 0.25),
        QtCore.QPoint(fx * 0.63, fy * 0.25)])

    SC2 = {}
    SC2['classlevel'] = 'SC2',
    SC2['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC2['brush'] = {'color': '156, 101, 0'},
    SC2['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.37, fy * 0.25),
        QtCore.QPoint(fx * 0.25, fy * 0.50),
        QtCore.QPoint(fx * 0.44, fy * 0.64),
        QtCore.QPoint(fx * 0.50, fy * 0.50),
        QtCore.QPoint(fx * 0.50, fy * 0.25)])

    SC3 = {}
    SC3['classlevel'] = 'SC3',
    SC3['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC3['brush'] = {'color': '100, 155, 100'},
    SC3['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.50, fy * 0.25),
        QtCore.QPoint(fx * 0.50, fy * 0.50),
        QtCore.QPoint(fx * 0.56, fy * 0.64),
        QtCore.QPoint(fx * 0.75, fy * 0.50),
        QtCore.QPoint(fx * 0.63, fy * 0.25)])

    SC4 = {}
    SC4['classlevel'] = 'SC4',
    SC4['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC4['brush'] = {'color': '0, 100, 0'},
    SC4['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.25, fy * 0.50),
        QtCore.QPoint(fx * 0.13, fy * 0.75),
        QtCore.QPoint(fx * 0.115, fy * 0.90),
        QtCore.QPoint(fx * 0.37, fy * 0.75),
        QtCore.QPoint(fx * 0.44, fy * 0.64)])

    SC5 = {}
    SC5['classlevel'] = 'SC5',
    SC5['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC5['brush'] = {'color': '250, 0, 100'},
    SC5['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.50, fy * 0.50),
        QtCore.QPoint(fx * 0.36, fy * 0.76),
        QtCore.QPoint(fx * 0.64, fy * 0.76)])

    SC6 = {}
    SC6['classlevel'] = 'SC6',
    SC6['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC6['brush'] = {'color': '155, 0, 100'},
    SC6['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.57, fy * 0.63),
        QtCore.QPoint(fx * 0.63, fy * 0.75),
        QtCore.QPoint(fx * 0.83, fy * 0.87),
        QtCore.QPoint(fx * 0.87, fy * 0.75),
        QtCore.QPoint(fx * 0.75, fy * 0.50)])

    SC7 = {}
    SC7['classlevel'] = 'SC7',
    SC7['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC7['brush'] = {'color': '255, 255, 0'},
    SC7['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.13, fy * 0.75),
        QtCore.QPoint(fx * 0.0, fy * 1.0),
        QtCore.QPoint(fx * 0.25, fy * 1.0)])

    SC8 = {}
    SC8['classlevel'] = 'SC8',
    SC8['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC8['brush'] = {'color': '0, 100, 255'},
    SC8['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.36, fy * 0.75),
        QtCore.QPoint(fx * 0.18, fy * 0.86),
        QtCore.QPoint(fx * 0.25, fy * 1.0),
        QtCore.QPoint(fx * 0.50, fy * 1.0),
        QtCore.QPoint(fx * 0.50, fy * 0.75)])

    SC9 = {}
    SC9['classlevel'] = 'SC9',
    SC9['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC9['brush'] = {'color': '50, 0, 100'},
    SC9['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.50, fy * 0.75),
        QtCore.QPoint(fx * 0.50, fy * 1.0),
        QtCore.QPoint(fx * 0.75, fy * 1.0),
        QtCore.QPoint(fx * 0.83, fy * 0.87),
        QtCore.QPoint(fx * 0.63, fy * 0.75)])

    SC10 = {}
    SC10['classlevel'] = 'SC10',
    SC10['pen'] = {'color': '255, 0, 0', 'width': 3},
    SC10['brush'] = {'color': '255, 100, 100'},
    SC10['polygon'] = QPolygonF([
        QtCore.QPoint(fx * 0.87, fy * 0.75),
        QtCore.QPoint(fx * 0.75, fy * 1.0),
        QtCore.QPoint(fx * 1.00, fy * 1.0)])

    SC = {
        'SC1': SC1,
        'SC2': SC2,
        'SC3': SC3,
        'SC4': SC4,
        'SC5': SC5,
        'SC6': SC6,
        'SC7': SC7,
        'SC8': SC8,
        'SC9': SC9,
        'SC10': SC10
    }
    return SC

SC = generatepolygons((100, 100))

print(SC)