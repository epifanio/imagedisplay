#!/usr/local/bin/python36

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(widget)
        self.edit = QtWidgets.QLineEdit(self)
        self.web = QWebEngineView()
        self.web.load(QUrl('file:///Users/epi/index.html'))
        self.web.setMouseTracking(True)
        layout.addWidget(self.edit)
        layout.addWidget(self.web)
        self.setCentralWidget(widget)
        self.web.installEventFilter(self)





    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseMove and str(type(source))=="<class 'PyQt5.QtWidgets.QOpenGLWidget'>"):
            # QtCore.Qt.NoButton
            # QtCore.Qt.LeftButton
            # QtCore.Qt.RightButton
            if event.buttons() == QtCore.Qt.NoButton:
                pos = event.pos()
                self.edit.setText('no button: %d, y: %d' % (pos.x(), pos.y()))
                print(self.web.frameGeometry().width()-self.web.geometry().x(), self.web.frameGeometry().height()-self.web.geometry().y())
                print(self.web.frameGeometry().width(), self.web.frameGeometry().height())
                #print(self.web.frameGeometry()[2]-self.web.geometry().x(), self.web.frameGeometry()[3]-self.web.geometry().y())
            elif event.buttons() == QtCore.Qt.LeftButton:
                pos = event.pos()
                self.edit.setText('left button : %d, y: %d' % (pos.x(), pos.y()))
                #self.onmouseclick()
            elif event.buttons() == QtCore.Qt.RightButton:
                pos = event.pos()
                self.edit.setText('right button : %d, y: %d' % (pos.x(), pos.y()))
                #pass # do other stuff
        return QtWidgets.QMainWindow.eventFilter(self, source, event)


    def updatebounds(self):
        self.web.page().runJavaScript("[map.getBounds().getSouthWest().lat, \
                                            map.getBounds().getSouthWest().lng, \
                                            map.getBounds().getNorthEast().lat, \
                                            map.getBounds().getNorthEast().lng]",
                                                      self.getbounds)


    def onmouseclick(self):
        self.web.page().runJavaScript("map.on('click', onMapClick);", print)

    def getbounds(self, bounds):
        self.w.marker_description.setText(str(bounds))
        self.bounds = bounds
        self.w.statusbar.showMessage("LL-UR Boundary %s" % self.bounds)
        print(self.bounds)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.installEventFilter(win)
    sys.exit(app.exec_())