#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from imagedisplay5_ui import Ui_MainWindow


from PyQt5 import QtWidgets

    
class GuiWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
from gui3 import GuiWidget

import pickle
import os

class ImageDisplay(QObject):
    def init(self):
        self.imagepath = '/media/epi/backup1/imgs/'
        self.imagelist = pickle.load( open('imagelist.p', 'rb'))
        self.imageindex = 1
        self.ZoomStepValue=50
        self.w = GuiWidget()

        self.w.ImageIndexspinBox.setMaximum(len(self.imagelist))
        self.w.ImageIndexSlider.setMaximum(len(self.imagelist))

        self.w.fwd.clicked.connect(self.increaseimageindex)
        self.w.fwd.clicked.connect(self.addImage)

        self.w.rwd.clicked.connect(self.decreaseimageindex)
        self.w.rwd.clicked.connect(self.addImage)


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

        # Exit
        self.w.actionExit.triggered.connect(self.quitAll)


        self.w.show()




    def getimage(self):
        return self.imagelist[self.imageindex]


    def setImageIndexStepValue(self):
        self.w.ImageIndexspinBox.setSingleStep(self.w.ImageStepspinBox.value())
        self.w.ImageIndexSlider.setSingleStep(self.w.ImageStepspinBox.value())

    def setimageindex(self):
        self.w.ImageIndexSlider.value()

    def decreaseimageindex(self):
        self.imageindex=self.imageindex-self.w.ImageStepspinBox.value()

    def increaseimageindex(self):
        print(self.w.ImageStepspinBox.value())
        self.imageindex=self.imageindex+self.w.ImageStepspinBox.value()


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
        print(self.ZoomStepValue)

    def addImage(self):
        print(os.path.join(self.imagepath,self.imagelist[self.imageindex]))
        self.pixmap = QPixmap(os.path.join(self.imagepath,self.imagelist[self.imageindex]))
        width=self.pixmap.width()*(self.ZoomStepValue/100.)
        height=self.pixmap.height()*(self.ZoomStepValue/100.)
        self.pixmap = self.pixmap.scaled(width, height, Qt.KeepAspectRatio)
        self.w.image.setPixmap(self.pixmap)
        print(self.pixmap.width(),self.pixmap.height())
                
        
    def quitAll(self):
        print('Quitting')
        app.quit()

        
if __name__ == "__main__":
    import sys
    import time
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = ImageDisplay()
    p.init()
    sys.exit(app.exec_())
