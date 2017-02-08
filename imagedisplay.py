#!/usr/local/bin/python36
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from imagedisplay5_ui import Ui_MainWindow
from PyQt5 import QtWidgets

import pandas as pd
from mainui import MainGui
from converter import Converter

import pickle
import os
from pyproj import Proj
import socket
import datetime as dt

from osgeo import ogr
from osgeo import osr
import json

#from ipyleaflet import (
#    Map,
#    Marker,
#    TileLayer, ImageOverlay,
#    Polyline, Polygon, Rectangle, Circle, CircleMarker,
#    GeoJSON,
#    DrawControl
#)

from htmap.htmapapp import MapDisplay

class ImageDisplay(QObject):
    def init(self):

        self.host='10.211.55.3'
        #self.host = '192.168.8.58'
        self.pport='8000'
        self.range=0
        self.w = MainGui()
        self.converter = Converter()
        self.myProj = Proj("+proj=utm +no_defs +zone=19 +a=6378137 +rf=298.257223563 +towgs84=0.000,0.000,0.000 +to_meter=1")

        #self.imagepath = '/media/epi/backup1/imgs/'
        #self.imagelist = pickle.load(open('imagelist.p', 'rb'))

        self.metadatafile = None
        self.imagelist = None
        #self.imagelist = []
        #self.imagelist = glob.glob('*.jpg')

        #self.hbcdta = pd.HDFStore('GB_selection_log_735768.h5')
        #self.hbcdtatot = pd.read_csv('GB_selection_log_735768.csv', index_col=0)
        #self.hbcdta = self.hbcdtatot.loc[self.hbcdtatot['Imagename'].isin((i.replace('.jpg', '') for i in self.imagelist))]
        #self.hbcdta = []
        self.imageindex = 1
        self.ZoomStepValue = 50
        self.dirname=''

        self.w.actionImageDirectory.triggered.connect(self.getImageDir)
        self.w.actionSelect_Image_Metadata.triggered.connect(self.getImageMetadataFile)
        self.w.actionASCII2Feather.triggered.connect(self.ascii2feather)

        self.w.gtvector_select.clicked.connect(self.setGTVectorFile)

        #self.w.ImageIndexspinBox.setMaximum(len(self.imagelist)-1)
        #self.w.ImageIndexSlider.setMaximum(len(self.imagelist)-1)

        self.w.fwd.clicked.connect(self.increaseimageindex)
        self.w.fwd.clicked.connect(self.addImage)

        self.w.rwd.clicked.connect(self.decreaseimageindex)
        self.w.rwd.clicked.connect(self.addImage)

        self.w.zoomto.clicked.connect(self.zoomto)

        self.w.query.clicked.connect(self.linearbuffer)



        # ZOOM
        self.w.ZoomStepSlider.valueChanged.connect(self.setValueZoomStepspinBox)
        
        self.w.ZoomStepSlider.valueChanged.connect(self.printFunction)
        
        self.w.ZoomStepspinBox.valueChanged.connect(self.setValueZoomStepSlider)
        
        self.w.ZoomStepspinBox.valueChanged.connect(self.printFunction)
        
        self.w.ZoomStepSlider.valueChanged.connect(self.setValue)
        
        self.w.ZoomStepspinBox.valueChanged.connect(self.setValue)

        # Image Index
        self.w.ImageIndexSlider.valueChanged.connect(self.setValueImageIndexspinBox)

        self.w.ImageIndexSlider.valueChanged.connect(self.printFunction)

        self.w.ImageIndexspinBox.valueChanged.connect(self.setValueImageIndexSlider)

        self.w.ImageStepspinBox.valueChanged.connect(self.setImageIndexStepValue)


        # zoomto and range
        # Image Index
        self.w.rangeSlider.valueChanged.connect(self.setValuerangeSpinBox)
        self.w.rangeSpinBox.valueChanged.connect(self.setValuerangeSlider)

        #self.w.rangeSlider.valueChanged.connect(self.setValueRange)

        # substrate annotation
        self.w.fixclay.setEnabled(False)
        self.w.fixsand.setEnabled(False)
        self.w.fixgravel.setEnabled(False)
        self.w.fixpeble.setEnabled(False)

        self.w.MudSlider.valueChanged.connect(self.setValueMud)

        self.w.ClaySlider.valueChanged.connect(self.setValueClay)

        self.w.SandSlider.valueChanged.connect(self.setValueSand)

        self.w.GravelSlider.valueChanged.connect(self.setValueGravel)

        self.w.PebleSlider.valueChanged.connect(self.setValuePeble)

        self.w.fixmud.stateChanged.connect(self.setValueMud)
        self.w.fixclay.stateChanged.connect(self.setValueClay)
        self.w.fixsand.stateChanged.connect(self.setValueSand)
        self.w.fixgravel.stateChanged.connect(self.setValueGravel)


        # Exit
        self.w.actionExit.triggered.connect(self.quitAll)


        #print(self.hbcdta.columns)
        self.w.statusbar.showMessage("System Status | Normal")
        self.w.show()


    def ascii2feather(self):
        self.converter.show()

    def setValuerangeSpinBox(self, r):
        self.range = int(r)
        self.w.rangeSpinBox.setSingleStep(1)
        self.w.rangeSpinBox.setValue(self.range)

    def setValuerangeSlider(self, r):
        self.range = int(r)
        self.w.rangeSlider.setSingleStep(1)
        self.w.rangeSlider.setValue(self.range)

    def getImageDir(self):
        self.dirname = QtWidgets.QFileDialog.getExistingDirectory()
        if self.dirname:
            self.imagelist = os.listdir(self.dirname)
            self.w.ImageIndexspinBox.setMaximum(len(self.imagelist) - 1)
            self.w.ImageIndexSlider.setMaximum(len(self.imagelist) - 1)
        #print(self.imagelist)

    def getImageMetadataFile(self):
        self.metadatafile = QtWidgets.QFileDialog.getSaveFileName()
        if self.metadatafile:
            self.hbcdtatot = pd.read_csv(self.metadatafile[0], index_col=0)
            self.hbcdtatot.index = pd.to_datetime(self.hbcdtatot.index)
            self.hbcdta = self.hbcdtatot.loc[
                self.hbcdtatot['Imagename'].isin((i.replace('.jpg', '') for i in self.imagelist))]
        #print(self.hbcdta)

    def setGTVectorFile(self):
        self.GTVectorFile = QtWidgets.QFileDialog.getSaveFileName()
        print('something')
        print(self.w.gtvector_type.currentText())
        if self.GTVectorFile:
            print(self.GTVectorFile)
            self.w.gtvector.setText(self.GTVectorFile[0]+'.'+self.w.gtvector_type.currentText().lower())


    def getimage(self):
        return self.imagelist[self.imageindex]

    def setImageIndexStepValue(self):
        self.w.ImageIndexspinBox.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexSlider.setSingleStep(self.w.ImageStepspinBox.value())

    def setimageindex(self):
        self.w.ImageIndexSlider.value()

    def decreaseimageindex(self):
        self.imageindex=self.imageindex-self.w.ImageStepspinBox.value()
        self.w.ImageIndexSlider.setValue(self.imageindex)

    def increaseimageindex(self):
        #print(self.w.ImageStepspinBox.value())
        self.imageindex = self.imageindex+self.w.ImageStepspinBox.value()
        self.w.ImageIndexSlider.setValue(self.imageindex)
        #self.w.ImageStepspinBox.setValue(self.imageindex)

    def setValueImageIndexspinBox(self, z):
        self.imageindex = int(z)
        self.w.ImageIndexspinBox.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexspinBox.setValue(self.imageindex)

    def setValueImageIndexSlider(self, z):
        self.imageindex = int(z)
        self.w.ImageIndexSlider.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexSlider.setValue(self.imageindex)

    def setValueZoomStepspinBox(self, z):
        self.ZoomStepValue = int(z)
        #self.w.ZoomStepspinBox.setRange(1, 100)
        self.w.ZoomStepspinBox.setSingleStep(1)
        self.w.ZoomStepspinBox.setValue(self.ZoomStepValue)

    def setValueZoomStepSlider(self, z):
        self.ZoomStepValue = int(z)
        self.w.ZoomStepSlider.setMinimum(1)
        #self.w.ZoomStepSlider.setMaximum(100)
        self.w.ZoomStepSlider.setValue(self.ZoomStepValue)

    def setValue(self, v):
        self.Value = v

    def printFunction(self):
        self.addImage()
        if self.w.zoomto.isChecked():
            #print('i am checked')
            self.zoomto()
        print(self.ZoomStepValue)

    def addImage(self):
        if self.metadatafile and self.imagelist is not None:
            print('ok')
            print(os.path.join(self.dirname, self.imagelist[self.imageindex]))
            #print(self.imagelist[self.imageindex][:-4])
            #print(self.hbcdta[self.hbcdta['Imagename']==self.imagelist[self.imageindex][:-4]])
            print('imageindex', self.imageindex)
            record = self.hbcdta[self.hbcdta['Imagename'] == self.imagelist[self.imageindex][:-4]]
            # use values[0] with a check for non empty list or reep the string replacemtnet ?
            if len(record) >= 1:
                # self.w.imagename.setText(str(record['Imagename'].values[0]))
                #self.w.imagetime.setText(str(record['Imagename'].index[0]))
                self.w.imageeast.setText(str(record['xutm'].values[0]))
                self.w.imagenorth.setText(str(record['yutm'].values[0]))
                self.w.hbcdepth.setText(str(record['V_Depth'].values[0]))
                self.w.waterdepth.setText(str(record['Water_Depth'].values[0]))
                self.w.altimeter.setText(str(record['Altimeter'].values[0]))
                self.w.salinity.setText(str(record['Salinity'].values[0]))
                self.w.temperature.setText(str(record['Temp'].values[0]))
                self.w.O2.setText(str(record['O2'].values[0]))
                self.w.CDOM.setText(str(record['Cdom'].values[0]))
                self.w.chlorophyll.setText(str(record['Chlorophyll'].values[0]))
                self.w.turbidity.setText(str(record['Turb'].values[0]))
                # test QtDateTime
                self.w.dateTimeEdit.setDateTime(record.index[0])

                self.w.statusbar.showMessage("Image %s" % record.index[0])
                self.w.linklabel.setText("<a href=\"file://%s\">%s</a>" % (os.path.join(self.dirname, self.imagelist[self.imageindex]), str(record['Imagename'].values[0])))
                self.w.linklabel.setOpenExternalLinks(True)



            self.pixmap = QPixmap(os.path.join(self.dirname, self.imagelist[self.imageindex]))
            width=self.pixmap.width()*(self.ZoomStepValue/100.)
            height=self.pixmap.height()*(self.ZoomStepValue/100.)
            self.pixmap = self.pixmap.scaled(width, height, Qt.KeepAspectRatio)
            self.w.image.setPixmap(self.pixmap)
            #print(dir(self.w.image))
            print('height', self.w.image.height())
            print('width', self.w.image.width())
            print('heightMM', self.w.image.height())
            print('widthMM', self.w.image.widthMM())
            #print(self.pixmap.width(), self.pixmap.height())
        else:
            print('both image path and metadata need to be set')
            print(' --- ')

    def setValueMud(self, mud):
        self.mudvalue = int(mud)
        self.w.mud.setText(str(self.mudvalue))
        if self.w.fixmud.isChecked()==True:
            self.w.fixclay.setEnabled(True)
            self.w.ClaySlider.setRange(0, 100-int(self.mudvalue))
        else:
            self.w.fixclay.setEnabled(False)

    def setValueClay(self, clay):
        self.clayvalue = int(clay)
        self.w.clay.setText(str(self.clayvalue))
        if self.w.fixclay.isChecked()==True:
            self.w.fixsand.setEnabled(True)
            self.w.SandSlider.setRange(0, 100 - (int(self.mudvalue)+int(self.clayvalue)))
        else:
            self.w.fixsand.setEnabled(False)

    def setValueSand(self, sand):
        self.sandvalue = int(sand)
        self.w.sand.setText(str(self.sandvalue))
        if self.w.fixsand.isChecked()==True:
            self.w.fixgravel.setEnabled(True)
            self.w.GravelSlider.setRange(0, 100 - (int(self.mudvalue)+int(self.clayvalue)+int(self.sandvalue)))
        else:
            self.w.fixgravel.setEnabled(False)

    def setValueGravel(self, gravel):
        self.gravelvalue = int(gravel)
        self.w.gravel.setText(str(self.gravelvalue))
        if self.w.fixgravel.isChecked()==True:
            self.w.fixpeble.setEnabled(True)
            self.w.PebleSlider.setRange(0, 100 - (int(self.mudvalue)+int(self.clayvalue)+int(self.sandvalue)+int(self.gravelvalue)))
        else:
            self.w.fixpeble.setEnabled(False)

    def setValuePeble(self, peble):
        self.peblevalue = int(peble)
        self.w.peble.setText(str(self.peblevalue))

    #self.myProj = Proj("+proj=utm +no_defs +zone=19 +a=6378137 +rf=298.257223563 +towgs84=0.000,0.000,0.000 +to_meter=1")
    #lon, lat = myProj(east, north, inverse=True)

    def zoomto(self):
        #self.w.statusbar.showMessage("System Status | Connecting to planet  ... 10s timeout")
        distance=1000
        east=self.w.imageeast.text()
        north=self.w.imagenorth.text()
        distance=self.range
        #range=self.w.rangeSlider.value()
        print(east)
        print(north)
        #self.myProj = Proj("+proj=utm +no_defs +zone=19 +a=6378137 +rf=298.257223563 +towgs84=0.000,0.000,0.000 +to_meter=1")
        lon, lat = self.myProj(east, north, inverse=True)
        ossim_zoom_xml = '<Set target=":navigator" vref="wgs84"><Camera><longitude>%s</longitude><latitude>%s</latitude><altitude>%s</altitude><heading>0</heading><pitch>0</pitch><roll>0</roll><altitudeMode>absolute</altitudeMode><range>%s</range></Camera></Set>' % (
        lon, lat, distance, distance)
        try:
            ossimposition = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ossimposition.settimeout(10)
            ossimposition.connect((self.host, int(self.pport)))
            ossimposition.settimeout(None)
            ossimposition.send(bytes(ossim_zoom_xml, "UTf-8"))
            ossimposition.close()
        except socket.timeout:
            print('No connection')
            #self.w.statusbar.showMessage("System Status | Connection failed")
        print(ossim_zoom_xml)
        #self.w.statusbar.showMessage("System Status | Normal")

    def quitAll(self):
        print('Quitting')
        app.quit()

    def linearbuffer(self):
        if self.metadatafile is not None:
            if self.w.ImageIndexspinBox.value()-self.w.rearbuffer.value() < 0:
                print('decrease rear buffer')
            if self.w.ImageIndexspinBox.value()+self.w.frontbuffer.value() > self.hbcdta.shape[0]:
                print('decrease front buffer')
            ##print(self.imagelist[self.imageindex])
            ##print(self.w.ImageIndexspinBox.value())
            ##print(self.hbcdta.shape)
            ##print(self.hbcdta.iloc[self.w.ImageIndexspinBox.value()])
            ##print(self.hbcdta.iloc[self.w.ImageIndexspinBox.value()])
            #east = self.w.imageeast.text()
            #north = self.w.imagenorth.text()
            #print(self.hbcdta.iloc[self.w.ImageIndexspinBox.value()-self.w.rearbuffer.value():self.w.ImageIndexspinBox.value()+self.w.frontbuffer.value()])
            #print(self.hbcdta[["yutm", "xutm"]].iloc[self.w.ImageIndexspinBox.value()-self.w.rearbuffer.value():self.w.ImageIndexspinBox.value()+self.w.frontbuffer.value()])
            pp = self.hbcdta[["yutm", "xutm"]].iloc[self.w.ImageIndexspinBox.value()-self.w.rearbuffer.value():self.w.ImageIndexspinBox.value()+self.w.frontbuffer.value()].values
            line = ogr.Geometry(ogr.wkbLineString)
            #print(pp)

            source = osr.SpatialReference()
            source.ImportFromEPSG(32619)
            target = osr.SpatialReference()
            target.ImportFromEPSG(4326)
            transform = osr.CoordinateTransformation(source, target)

            for i in pp:
                #lon, lat = self.myProj(i[1], i[0], inverse=True)
                line.AddPoint(i[1], i[0])
                #line.AddPoint(lon, lat)

            buffer=self.w.bufferwidth.value()
            bufferDistance = buffer
            poly = line.Buffer(bufferDistance)
            line.Transform(transform)
            poly.Transform(transform)
            d = json.loads(line.ExportToJson())
            #print(json.dumps(d))
            d = json.loads(poly.ExportToJson())
            #print(json.dumps(d))
            #p = GeoJSON(data=d)
            #print(p)
            #print(poly)
            d = poly.ExportToKML()
            kml = open('test.kml', 'w')
            kml.write("""<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Placemark><name>The Pentagon</name>""")
            kml.write(d)
            kml.write("""</Placemark ></kml >""")
            kml.close()
            if self.w.syncGE.isChecked():
                os.system("open -a Google\ Earth\ Pro test.kml")
            print(d)
        else:
            print('yuo need to load image metadata first')

    def buffergeom(self, points):
        line = ogr.Geometry(ogr.wkbLineString)
        line.AddPoint(myl[0][0], myl[0][-1])
        line.AddPoint(myl[-1][0], myl[-1][-1])
        bufferDistance = 0.00000000005
        poly = line.Buffer(bufferDistance)
        d = json.loads(line.ExportToJson())
        g = GeoJSON(data=d)
        d = json.loads(poly.ExportToJson())
        p = GeoJSON(data=d)
        print(p)
        print(d)


if __name__ == "__main__":
    import sys
    #import time
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = ImageDisplay()
    p.init()
    sys.exit(app.exec_())


'''
left = df[(df['Easting']>=e-5) &
          (df['Easting']<=e+5) &
          (df['Northing']>=n-5) &
          (df['Northing']<=n+5) &
          (df['True Angle']>=-70) &
          (df['True Angle']<=-10)]

right = df[(df['Easting']>=e-5) &
           (df['Easting']<=e+5) &
           (df['Northing']>=n-5) &
           (df['Northing']<=n+5) &
           (df['True Angle']<=70) &
           (df['True Angle']>=10)]
'''
