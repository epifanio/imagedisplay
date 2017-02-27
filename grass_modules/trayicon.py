import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# code source: http://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application  - add answer PyQt5
#PyQt4 to PyQt5 version: http://stackoverflow.com/questions/20749819/pyqt5-failing-import-of-qtgui
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        self.exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)
        #QtCore.QObject.connect(exitAction, QtCore.SIGNAL('triggered()'), self.exit)
        self.exitAction.triggered.connect(self.exit)

    def exit(self):
      QtCore.QCoreApplication.exit()

def main(image):
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    on=r'/Users/epi/Desktop/map-marker-icon.png'# ADD PATH OF YOUR ICON HERE .png works
    main(on)