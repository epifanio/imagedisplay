# self.text = self.tr("Categories")

# --
# self.scene = QGraphicsScene()
# self.item1 = QGraphicsTextItem()
# self.item1.setPos(0, 0)
# self.item1.setPlainText("-----------------------")
# self.scene.addItem(self.item1)
# --

# item = scene.addSimpleText("Hello, world!", QFont("Times", 15))
# scene.addText(100, 50,  "Hello World!!")
# print(dir(item))
# item.setPos(0, 50)
# item.setBrush(QColor(0, 255, 0, 127))
# item = scene.addText("text", QFont('Arial Black', 15, QFont.Light))
# newLine = line(QtCore.QPoint(0, 0), QtCore.QPoint(50, 50))
# scene.addItem(newLine)

# --
# self.w.graphicsView.setScene(self.scene)
# --


# self.w.statusbar.setSizeGripEnabled(True)
# self.w.newclass.hide()
# self.w.addclass.hide()

# self.w.pushButton.setFixedHeight(200)
# self.w.pushButton.setFixedWidth(200)




# example assign menu to button
# self.w.menu = QMenu()
# self.menuItem1 = self.w.menu.addAction('Menu Item1')
# self.menuItem2 = self.w.menu.addAction('Menu Item2')
# self.w.p1.setMenu(self.w.menu)



# self.text = self.tr("Text Effects")
# self.number = 6
# self.font = QFont()

# self.w.frame.setMinimumSize(QtCore.QSize(self.fx, self.fy))
# self.w.frame.setMaximumSize(QtCore.QSize(self.fx, self.fy))

# self.w.frame_2.setMinimumSize(QtCore.QSize(self.fx, self.fy))
# self.w.frame_2.setMaximumSize(QtCore.QSize(self.fx, self.fy))

# self.w.graphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
# self.w.graphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))

"""
scene = QGraphicsScene()
scene.setSceneRect(0, 0, self.fx*self.mp, self.fy*self.mp)
self.w.graphicsView.setScene(scene)
#self.sc.graphicsView.setScene(scene)
item = scene.addText("PERCENT OF SAND")
font = QFont()
font.setPointSize(self.fx/20.)
item.setFont(font)
item.setTransform(QTransform().fromTranslate(2, 70), True)
item.update()
item.setTransform(QTransform().rotate(-63), True)
item.update()
#self.createScene()
"""

"""
self.p1 = QtWidgets.QPushButton(self.graphicsView)
self.p2 = QtWidgets.QPushButton(self.graphicsView)
self.p3 = QtWidgets.QPushButton(self.graphicsView)
self.p4 = QtWidgets.QPushButton(self.graphicsView)
self.p5 = QtWidgets.QPushButton(self.graphicsView)
self.p6 = QtWidgets.QPushButton(self.graphicsView)
self.p7 = QtWidgets.QPushButton(self.graphicsView)
self.p8 = QtWidgets.QPushButton(self.graphicsView)
self.p9 = QtWidgets.QPushButton(self.graphicsView)
self.p10 = QtWidgets.QPushButton(self.graphicsView)


self.L1 = QtWidgets.QLabel(self.graphicsView)
self.L1.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L2 = QtWidgets.QLabel(self.graphicsView)
self.L2.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L3 = QtWidgets.QLabel(self.graphicsView)
self.L3.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L4 = QtWidgets.QLabel(self.graphicsView)
self.L4.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L5 = QtWidgets.QLabel(self.graphicsView)
self.L5.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L6 = QtWidgets.QLabel(self.graphicsView)
self.L6.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L7 = QtWidgets.QLabel(self.graphicsView)
self.L7.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L8 = QtWidgets.QLabel(self.graphicsView)
self.L8.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L9 = QtWidgets.QLabel(self.graphicsView)
self.L9.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

self.L10 = QtWidgets.QLabel(self.graphicsView)
self.L10.setStyleSheet("background-color: rgba(0,0,0,0%)")
self.L10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.L10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

_translate = QCoreApplication.translate
self.p1.setToolTip(_translate("MainWindow", "P1"))
self.p2.setToolTip(_translate("MainWindow", "P2"))
self.p3.setToolTip(_translate("MainWindow", "P3"))
self.p4.setToolTip(_translate("MainWindow", "P4"))
self.p5.setToolTip(_translate("MainWindow", "P5"))
self.p6.setToolTip(_translate("MainWindow", "P6"))
self.p7.setToolTip(_translate("MainWindow", "P7"))
self.p8.setToolTip(_translate("MainWindow", "P8"))
self.p9.setToolTip(_translate("MainWindow", "P9"))
self.p10.setToolTip(_translate("MainWindow", "P10"))

self.L1.setText(_translate("MainWindow", "L1"))
self.L2.setText(_translate("MainWindow", "L2"))
self.L3.setText(_translate("MainWindow", "L3"))
self.L4.setText(_translate("MainWindow", "L4"))
self.L5.setText(_translate("MainWindow", "L5"))
self.L6.setText(_translate("MainWindow", "L6"))
self.L7.setText(_translate("MainWindow", "L7"))
self.L8.setText(_translate("MainWindow", "L8"))
self.L9.setText(_translate("MainWindow", "L9"))
self.L10.setText(_translate("MainWindow", "L10"))

self.L1.setParent(self.p1)
self.L2.setParent(self.p2)
self.L3.setParent(self.p3)
self.L4.setParent(self.p4)
self.L5.setParent(self.p5)
self.L6.setParent(self.p6)
self.L7.setParent(self.p7)
self.L8.setParent(self.p8)
self.L9.setParent(self.p9)
self.L10.setParent(self.p10)
"""

# Add polygons
print('adding polygons')
"""
SC = generatepolygons((self.fx, self.fy))
self.SC1 = self.scene.addPolygon(SC['SC1']['polygon'],
                                 SC['SC1']['pen'],
                                 SC['SC1']['brush'])

self.SC2 = self.scene.addPolygon(SC['SC2']['polygon'],
                                 SC['SC2']['pen'],
                                 SC['SC2']['brush'])

self.SC3 = self.scene.addPolygon(SC['SC3']['polygon'],
                                 SC['SC3']['pen'],
                                 SC['SC3']['brush'])

self.SC4 = self.scene.addPolygon(SC['SC4']['polygon'],
                                 SC['SC4']['pen'],
                                 SC['SC4']['brush'])

self.SC5 = self.scene.addPolygon(SC['SC5']['polygon'],
                                 SC['SC5']['pen'],
                                 SC['SC5']['brush'])

self.SC6 = self.scene.addPolygon(SC['SC6']['polygon'],
                                 SC['SC6']['pen'],
                                 SC['SC6']['brush'])

self.SC7 = self.scene.addPolygon(SC['SC7']['polygon'],
                                 SC['SC7']['pen'],
                                 SC['SC7']['brush'])

self.SC8 = self.scene.addPolygon(SC['SC8']['polygon'],
                                 SC['SC8']['pen'],
                                 SC['SC8']['brush'])

self.SC9 = self.scene.addPolygon(SC['SC9']['polygon'],
                                 SC['SC9']['pen'],
                                 SC['SC9']['brush'])

self.SC10 = self.scene.addPolygon(SC['SC10']['polygon'],
                                 SC['SC10']['pen'],
                                 SC['SC10']['brush'])

self.SC1.update()
self.graphicsView.setScene(self.scene)
"""


def drawbuttons2(self, mp):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    self.mp = mp
    self.fx, self.fy = self.frame.size().width(), self.frame.size().height()
    self.fx = self.mp * self.fx
    self.fy = self.mp * self.fy
    self.frame.setMinimumSize(QtCore.QSize(self.fx, self.fy))
    self.frame.setMaximumSize(QtCore.QSize(self.fx, self.fy))

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

    self.L1.setGeometry(QtCore.QRect(self.fx * 0.48, self.fy * 0.12, self.mp * 50, self.mp * 50))
    self.L2.setGeometry(QtCore.QRect(self.fx * 0.38, self.fy * 0.40, self.mp * 50, self.mp * 50))
    self.L3.setGeometry(QtCore.QRect(self.fx * 0.58, self.fy * 0.40, self.mp * 50, self.mp * 50))
    self.L4.setGeometry(QtCore.QRect(self.fx * 0.25, self.fy * 0.65, self.mp * 50, self.mp * 50))
    self.L5.setGeometry(QtCore.QRect(self.fx * 0.48, self.fy * 0.62, self.mp * 50, self.mp * 50))
    self.L6.setGeometry(QtCore.QRect(self.fx * 0.68, self.fy * 0.65, self.mp * 50, self.mp * 50))
    self.L7.setGeometry(QtCore.QRect(self.fx * 0.10, self.fy * 0.88, self.mp * 50, self.mp * 50))
    self.L8.setGeometry(QtCore.QRect(self.fx * 0.32, self.fy * 0.88, self.mp * 50, self.mp * 50))
    self.L9.setGeometry(QtCore.QRect(self.fx * 0.58, self.fy * 0.88, self.mp * 50, self.mp * 50))
    self.L10.setGeometry(QtCore.QRect(self.fx * 0.84, self.fy * 0.88, self.mp * 50, self.mp * 50))

    font = QFont()
    font.setPointSize(self.fontsize)

    self.L1.setFont(font)
    self.L2.setFont(font)
    self.L3.setFont(font)
    self.L4.setFont(font)
    self.L5.setFont(font)
    self.L6.setFont(font)
    self.L7.setFont(font)
    self.L8.setFont(font)
    self.L9.setFont(font)
    self.L10.setFont(font)

    self.A1 = QPolygon([
        QtCore.QPoint(self.fx * 0.5, self.fy * 0.0), QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
        QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
    self.A2 = QPolygon([
        QtCore.QPoint(self.fx * 0.37, self.fy * 0.25), QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
        QtCore.QPoint(self.fx * 0.44, self.fy * 0.64), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
        QtCore.QPoint(self.fx * 0.50, self.fy * 0.25)])
    self.A3 = QPolygon([
        QtCore.QPoint(self.fx * 0.50, self.fy * 0.25), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
        QtCore.QPoint(self.fx * 0.56, self.fy * 0.64), QtCore.QPoint(self.fx * 0.75, self.fy * 0.50),
        QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
    self.A4 = QPolygon([
        QtCore.QPoint(self.fx * 0.25, self.fy * 0.50), QtCore.QPoint(self.fx * 0.13, self.fy * 0.75),
        QtCore.QPoint(self.fx * 0.115, self.fy * 0.90), QtCore.QPoint(self.fx * 0.37, self.fy * 0.75),
        QtCore.QPoint(self.fx * 0.44, self.fy * 0.64)])
    self.A5 = QPolygon([
        QtCore.QPoint(self.fx * 0.50, self.fy * 0.50), QtCore.QPoint(self.fx * 0.36, self.fy * 0.76),
        QtCore.QPoint(self.fx * 0.64, self.fy * 0.76)])
    self.A6 = QPolygon([
        QtCore.QPoint(self.fx * 0.57, self.fy * 0.63), QtCore.QPoint(self.fx * 0.63, self.fy * 0.75),
        QtCore.QPoint(self.fx * 0.83, self.fy * 0.87), QtCore.QPoint(self.fx * 0.87, self.fy * 0.75),
        QtCore.QPoint(self.fx * 0.75, self.fy * 0.50)])
    self.A7 = QPolygon([
        QtCore.QPoint(self.fx * 0.13, self.fy * 0.75), QtCore.QPoint(self.fx * 0.0, self.fy * 1.0),
        QtCore.QPoint(self.fx * 0.25, self.fy * 1.0)])
    self.A8 = QPolygon([
        QtCore.QPoint(self.fx * 0.36, self.fy * 0.75), QtCore.QPoint(self.fx * 0.18, self.fy * 0.86),
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
                          "QPushButton:pressed { background-color: red }")

    self.p2.setMask(p2region)
    self.p2.setStyleSheet("QPushButton { background-color: rgb(255, 50, 0) }"
                          "QPushButton:pressed { background-color: red }")

    self.p3.setMask(p3region)
    self.p3.setStyleSheet("QPushButton { background-color: rgb(100, 155, 100) }"
                          "QPushButton:pressed { background-color: red }")

    self.p4.setMask(p4region)
    self.p4.setStyleSheet("QPushButton { background-color: rgb(0, 100, 0) }"
                          "QPushButton:pressed { background-color: red }")

    self.p5.setMask(p5region)
    self.p5.setStyleSheet("QPushButton { background-color: rgb(250, 0, 100) }"
                          "QPushButton:pressed { background-color: red }")

    self.p6.setMask(p6region)
    self.p6.setStyleSheet("QPushButton { background-color: rgb(155, 0, 100) }"
                          "QPushButton:pressed { background-color: red }")

    self.p7.setMask(p7region)
    self.p7.setStyleSheet("QPushButton { background-color: rgb(255, 255, 0) }"
                          "QPushButton:pressed { background-color: red }")

    self.p8.setMask(p8region)
    self.p8.setStyleSheet("QPushButton { background-color: rgb(0, 100, 255) }"
                          "QPushButton:pressed { background-color: red }")

    self.p9.setMask(p9region)
    self.p9.setStyleSheet("QPushButton { background-color: rgb(50, 0, 100) }"
                          "QPushButton:pressed { background-color: red }")

    self.p10.setMask(p10region)
    self.p10.setStyleSheet("QPushButton { background-color: rgb(255, 100, 100) }"
                           "QPushButton:pressed { background-color: red }")
    self.createScene()


def createScene2(self):
    self.frame.setMinimumSize(QtCore.QSize(self.fx, self.fy))
    self.frame.setMaximumSize(QtCore.QSize(self.fx, self.fy))
    self.graphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
    self.graphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
    self.scene = QGraphicsScene()
    self.scene.setSceneRect(0, 0, self.fx, self.fy)
    # draw borders
    self.scene.addLine(QLineF(0, self.fy, self.fx / 2., 0), QPen(QBrush(Qt.red), 3, Qt.SolidLine))
    self.scene.addLine(QLineF(self.fx / 2., 0, self.fx, self.fx), QPen(QBrush(Qt.red), 3, Qt.SolidLine))
    #
    self.graphicsView.setScene(self.scene)
    # Add text labels
    item = self.scene.addText("PERCENT OF SAND")
    font = QFont()
    font.setPointSize(self.fx / 20.)
    item.setFont(font)
    item.setTransform(QTransform().fromTranslate(0.02 * self.fx, 0.7 * self.fy), True)
    item.update()
    item.setTransform(QTransform().rotate(-63), True)
    item.update()
    # Add polygons
    self.A1F = QPolygonF([
        QtCore.QPoint(self.fx * 0.4, self.fy * 0.01),
        QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
        QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
    self.item2 = self.scene.addPolygon(self.A1F, QPen(QBrush(Qt.red), 3, Qt.SolidLine), QBrush(Qt.darkBlue))
    # self.item2.setFlag(QGraphicsItem.ItemIsSelectable)
    # self.item2.setFlag(QGraphicsItem.ItemIsMovable)
    self.item2.update()



class Shepard1(QWidget):
    def __init__(self, qframe):
        self.frame = qframe
        self.mp = 1
        self.fontsize = 6
        self.initUI()


    def initUI(self):
        self.graphicsView = QtWidgets.QGraphicsView(self.shepardframe)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.graphicsView.setObjectName("graphicsView")


        self.p1 = QtWidgets.QPushButton(self.graphicsView)
        self.p1.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.p1.setMinimumSize(QtCore.QSize(100, 100))
        self.p1.setMaximumSize(QtCore.QSize(100, 100))
        self.p1.setText("")
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(self.graphicsView)
        self.p2.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2.sizePolicy().hasHeightForWidth())
        self.p2.setSizePolicy(sizePolicy)
        self.p2.setMinimumSize(QtCore.QSize(100, 100))
        self.p2.setMaximumSize(QtCore.QSize(100, 100))
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(self.graphicsView)
        self.p3.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3.sizePolicy().hasHeightForWidth())
        self.p3.setSizePolicy(sizePolicy)
        self.p3.setMinimumSize(QtCore.QSize(100, 100))
        self.p3.setMaximumSize(QtCore.QSize(100, 100))
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QPushButton(self.graphicsView)
        self.p4.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p4.sizePolicy().hasHeightForWidth())
        self.p4.setSizePolicy(sizePolicy)
        self.p4.setMinimumSize(QtCore.QSize(100, 100))
        self.p4.setMaximumSize(QtCore.QSize(100, 100))
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(self.graphicsView)
        self.p5.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p5.sizePolicy().hasHeightForWidth())
        self.p5.setSizePolicy(sizePolicy)
        self.p5.setMinimumSize(QtCore.QSize(100, 100))
        self.p5.setMaximumSize(QtCore.QSize(100, 100))
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QPushButton(self.graphicsView)
        self.p6.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p6.sizePolicy().hasHeightForWidth())
        self.p6.setSizePolicy(sizePolicy)
        self.p6.setMinimumSize(QtCore.QSize(100, 100))
        self.p6.setMaximumSize(QtCore.QSize(100, 100))
        self.p6.setText("")
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QPushButton(self.graphicsView)
        self.p7.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p7.sizePolicy().hasHeightForWidth())
        self.p7.setSizePolicy(sizePolicy)
        self.p7.setMinimumSize(QtCore.QSize(100, 100))
        self.p7.setMaximumSize(QtCore.QSize(100, 100))
        self.p7.setText("")
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QPushButton(self.graphicsView)
        self.p8.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p8.sizePolicy().hasHeightForWidth())
        self.p8.setSizePolicy(sizePolicy)
        self.p8.setMinimumSize(QtCore.QSize(100, 100))
        self.p8.setMaximumSize(QtCore.QSize(100, 100))
        self.p8.setText("")
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QPushButton(self.graphicsView)
        self.p9.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p9.sizePolicy().hasHeightForWidth())
        self.p9.setSizePolicy(sizePolicy)
        self.p9.setMinimumSize(QtCore.QSize(100, 100))
        self.p9.setMaximumSize(QtCore.QSize(100, 100))
        self.p9.setText("")
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QPushButton(self.graphicsView)
        self.p10.setGeometry(QtCore.QRect(0, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p10.sizePolicy().hasHeightForWidth())
        self.p10.setSizePolicy(sizePolicy)
        self.p10.setMinimumSize(QtCore.QSize(100, 100))
        self.p10.setMaximumSize(QtCore.QSize(100, 100))
        self.p10.setText("")
        self.p10.setObjectName("p10")
        self.L1 = QtWidgets.QLabel(self.graphicsView)
        self.L1.setGeometry(QtCore.QRect(48, 12, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L1.setFont(font)
        self.L1.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L1.setMouseTracking(True)
        self.L1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L1.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L1.setObjectName("L1")
        self.L2 = QtWidgets.QLabel(self.graphicsView)
        self.L2.setGeometry(QtCore.QRect(38, 40, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L2.setFont(font)
        self.L2.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L2.setMouseTracking(True)
        self.L2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L2.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L2.setObjectName("L2")
        self.L3 = QtWidgets.QLabel(self.graphicsView)
        self.L3.setGeometry(QtCore.QRect(58, 40, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L3.setFont(font)
        self.L3.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L3.setMouseTracking(True)
        self.L3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L3.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L3.setObjectName("L3")
        self.L4 = QtWidgets.QLabel(self.graphicsView)
        self.L4.setGeometry(QtCore.QRect(25, 65, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L4.setFont(font)
        self.L4.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L4.setMouseTracking(True)
        self.L4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L4.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L4.setObjectName("L4")
        self.L5 = QtWidgets.QLabel(self.graphicsView)
        self.L5.setGeometry(QtCore.QRect(48, 62, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L5.setFont(font)
        self.L5.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L5.setMouseTracking(True)
        self.L5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L5.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L5.setObjectName("L5")
        self.L6 = QtWidgets.QLabel(self.graphicsView)
        self.L6.setGeometry(QtCore.QRect(68, 65, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L6.setFont(font)
        self.L6.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L6.setMouseTracking(True)
        self.L6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L6.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L6.setObjectName("L6")
        self.L7 = QtWidgets.QLabel(self.graphicsView)
        self.L7.setGeometry(QtCore.QRect(10, 88, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L7.setFont(font)
        self.L7.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L7.setMouseTracking(True)
        self.L7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L7.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L7.setObjectName("L7")
        self.L8 = QtWidgets.QLabel(self.graphicsView)
        self.L8.setGeometry(QtCore.QRect(32, 88, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L8.setFont(font)
        self.L8.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L8.setMouseTracking(True)
        self.L8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L8.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L8.setObjectName("L8")
        self.L9 = QtWidgets.QLabel(self.graphicsView)
        self.L9.setGeometry(QtCore.QRect(58, 88, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L9.setFont(font)
        self.L9.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L9.setMouseTracking(True)
        self.L9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L9.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L9.setObjectName("L9")
        self.L10 = QtWidgets.QLabel(self.graphicsView)
        self.L10.setGeometry(QtCore.QRect(84, 88, 50, 50))
        font = QFont()
        font.setPointSize(8)
        self.L10.setFont(font)
        self.L10.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.L10.setMouseTracking(True)
        self.L10.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.L10.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.L10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.L10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.L10.setObjectName("L10")
        _translate = QCoreApplication.translate
        self.p1.setToolTip(_translate("MainWindow", "P1"))
        self.p2.setToolTip(_translate("MainWindow", "P2"))
        self.p3.setToolTip(_translate("MainWindow", "P3"))
        self.p4.setToolTip(_translate("MainWindow", "P4"))
        self.p10.setToolTip(_translate("MainWindow", "P10"))
        self.L1.setText(_translate("MainWindow", "L1"))
        self.L2.setText(_translate("MainWindow", "L2"))
        self.L3.setText(_translate("MainWindow", "L3"))
        self.L4.setText(_translate("MainWindow", "L4"))
        self.L5.setText(_translate("MainWindow", "L5"))
        self.L6.setText(_translate("MainWindow", "L6"))
        self.L7.setText(_translate("MainWindow", "L7"))
        self.L8.setText(_translate("MainWindow", "L8"))
        self.L9.setText(_translate("MainWindow", "L9"))
        self.L10.setText(_translate("MainWindow", "L10"))

        self.L1.setParent(self.p1)
        self.L2.setParent(self.p2)
        self.L3.setParent(self.p3)
        self.L4.setParent(self.p4)
        self.L5.setParent(self.p5)
        self.L6.setParent(self.p6)
        self.L7.setParent(self.p7)
        self.L8.setParent(self.p8)
        self.L9.setParent(self.p9)
        self.L10.setParent(self.p10)

        self.fx, self.fy = self.frame.size().width(), self.frame.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.graphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.graphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))

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
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.0),
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A2 = QPolygon([
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.44, self.fy * 0.64),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25)])
        self.A3 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.56, self.fy * 0.64),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A4 = QPolygon([
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.13, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.17, self.fy * 0.87),
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.44, self.fy * 0.64)])
        self.A5 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.36, self.fy * 0.76),
            QtCore.QPoint(self.fx * 0.64, self.fy * 0.76)])
        self.A6 = QPolygon([
            QtCore.QPoint(self.fx * 0.57, self.fy * 0.63),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.83, self.fy * 0.87),
            QtCore.QPoint(self.fx * 0.87, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50)])
        self.A7 = QPolygon([
            QtCore.QPoint(self.fx * 0.13, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.0, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0)])
        self.A8 = QPolygon([
            QtCore.QPoint(self.fx * 0.36, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.18, self.fy * 0.86),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.75)])
        self.A9 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.50, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.75, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.83, self.fy * 0.87),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.75)])
        self.A10 = QPolygon([
            QtCore.QPoint(self.fx * 0.87, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 1.0),
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

        self.E1 = QPolygon([
            QtCore.QPoint(self.fx * 0, self.fy * 0),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0),
            QtCore.QPoint(self.fx * 1, self.fy * 0),
            QtCore.QPoint(self.fx * 1, self.fy * 1),
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.01),
            QtCore.QPoint(self.fx * 0, self.fy * 1)])


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

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.fx * self.mp, self.fy * self.mp)
        self.graphicsView.setScene(scene)
        item = scene.addText("PERCENT OF SAND")
        font = QFont()
        font.setPointSize(self.fx / 20.)
        item.setFont(font)
        item.setTransform(QTransform().fromTranslate(2, 70), True)
        item.update()
        item.setTransform(QTransform().rotate(-63), True)
        item.update()

    def createScene(self):
        self.frame.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.frame.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        self.graphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.graphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.fx, self.fy)
        self.graphicsView.setScene(scene)
        item = scene.addText("PERCENT OF SAND")
        font = QFont()
        font.setPointSize(self.fx / 20.)
        item.setFont(font)
        item.setTransform(QTransform().fromTranslate(0.02 * self.fx, 0.7 * self.fy), True)
        item.update()
        item.setTransform(QTransform().rotate(-63), True)
        item.update()


    def changeSize(self, mp):
        self.mp = mp
        self.fx, self.fy = self.frame.size().width(), self.frame.size().height()
        self.fx = self.mp * self.fx
        self.fy = self.mp * self.fy
        self.frame.setMinimumSize(QtCore.QSize(self.fx, self.fy))
        self.frame.setMaximumSize(QtCore.QSize(self.fx, self.fy))

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

        self.L1.setGeometry(QtCore.QRect(self.fx * 0.48, self.fy * 0.12, self.mp*50, self.mp*50))
        self.L2.setGeometry(QtCore.QRect(self.fx * 0.38, self.fy * 0.40, self.mp*50, self.mp*50))
        self.L3.setGeometry(QtCore.QRect(self.fx * 0.58, self.fy * 0.40, self.mp*50, self.mp*50))
        self.L4.setGeometry(QtCore.QRect(self.fx * 0.25, self.fy * 0.65, self.mp*50, self.mp*50))
        self.L5.setGeometry(QtCore.QRect(self.fx * 0.48, self.fy * 0.62, self.mp*50, self.mp*50))
        self.L6.setGeometry(QtCore.QRect(self.fx * 0.68, self.fy * 0.65, self.mp*50, self.mp*50))
        self.L7.setGeometry(QtCore.QRect(self.fx * 0.10, self.fy * 0.88, self.mp*50, self.mp*50))
        self.L8.setGeometry(QtCore.QRect(self.fx * 0.32, self.fy * 0.88, self.mp*50, self.mp*50))
        self.L9.setGeometry(QtCore.QRect(self.fx * 0.58, self.fy * 0.88, self.mp*50, self.mp*50))
        self.L10.setGeometry(QtCore.QRect(self.fx * 0.84, self.fy * 0.88, self.mp*50, self.mp*50))

        font = QFont()
        font.setPointSize(self.fontsize)
        self.L1.setFont(font)
        self.L2.setFont(font)
        self.L3.setFont(font)
        self.L4.setFont(font)
        self.L5.setFont(font)
        self.L6.setFont(font)
        self.L7.setFont(font)
        self.L8.setFont(font)
        self.L9.setFont(font)
        self.L10.setFont(font)

        self.A1 = QPolygon([
            QtCore.QPoint(self.fx * 0.5, self.fy * 0.01), QtCore.QPoint(self.fx * 0.37, self.fy * 0.25),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A2 = QPolygon([
            QtCore.QPoint(self.fx * 0.37, self.fy * 0.25), QtCore.QPoint(self.fx * 0.25, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.44, self.fy * 0.64), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25)])
        self.A3 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.25), QtCore.QPoint(self.fx * 0.50, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.56, self.fy * 0.64), QtCore.QPoint(self.fx * 0.75, self.fy * 0.50),
            QtCore.QPoint(self.fx * 0.63, self.fy * 0.25)])
        self.A4 = QPolygon([
            QtCore.QPoint(self.fx * 0.25, self.fy * 0.50), QtCore.QPoint(self.fx * 0.13, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.115, self.fy * 0.90), QtCore.QPoint(self.fx * 0.37, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.44, self.fy * 0.64)])
        self.A5 = QPolygon([
            QtCore.QPoint(self.fx * 0.50, self.fy * 0.50), QtCore.QPoint(self.fx * 0.36, self.fy * 0.76),
            QtCore.QPoint(self.fx * 0.64, self.fy * 0.76)])
        self.A6 = QPolygon([
            QtCore.QPoint(self.fx * 0.57, self.fy * 0.63), QtCore.QPoint(self.fx * 0.63, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.83, self.fy * 0.87), QtCore.QPoint(self.fx * 0.87, self.fy * 0.75),
            QtCore.QPoint(self.fx * 0.75, self.fy * 0.50)])
        self.A7 = QPolygon([
            QtCore.QPoint(self.fx * 0.13, self.fy * 0.75), QtCore.QPoint(self.fx * 0.0, self.fy * 1.0),
            QtCore.QPoint(self.fx * 0.25, self.fy * 1.0)])
        self.A8 = QPolygon([
            QtCore.QPoint(self.fx * 0.36, self.fy * 0.75), QtCore.QPoint(self.fx * 0.18, self.fy * 0.86),
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
        self.createScene()


# self.fx, self.fy = self.w.shepardframe.size().width(), self.w.shepardframe.size().height()
# self.fx = self.mp * self.fx
# self.fy = self.mp * self.fy


"""
self.sc.p1.clicked.connect(self.p1print)
self.sc.p2.clicked.connect(self.p2print)
self.sc.p3.clicked.connect(self.p3print)
self.sc.p4.clicked.connect(self.p4print)
self.sc.p5.clicked.connect(self.p5print)
self.sc.p6.clicked.connect(self.p6print)
self.sc.p7.clicked.connect(self.p7print)
self.sc.p8.clicked.connect(self.p8print)
self.sc.p9.clicked.connect(self.p9print)
self.sc.p10.clicked.connect(self.p10print)
"""


def L1click(self):
    print('p1')
    # self.w.p1.setStyleSheet(
    #        """QLineEdit { background-color: green; color: white }""")
    # if self.w.p1.clicked:
    #    print('cccc')
    # self.w.p1.setStyleSheet(
    #    """QLineEdit { background-color: green; color: white }""")


def p1print(self):
    print('p1')


def p2print(self):
    print('p2')


def p3print(self):
    print('p3')


def p4print(self):
    print('p4')


def p5print(self):
    print('p5')


def p6print(self):
    print('p6')


def p7print(self):
    print('p7')


def p8print(self):
    print('p8')


def p9print(self):
    print('p9')


def p10print(self):
    print('p10')


def createscene3(self):
    self.shepardframeA.setMinimumSize(QtCore.QSize(self.fx, self.fy))
    self.shepardframeA.setMaximumSize(QtCore.QSize(self.fx, self.fy))
    self.shepardsandgraphicsView.setMinimumSize(QtCore.QSize(self.fx, self.fy))
    self.shepardsandgraphicsView.setMaximumSize(QtCore.QSize(self.fx, self.fy))
    self.scene = QGraphicsScene()
    self.scene.setSceneRect(0, 0, self.fx, self.fy)

    # Add labels
    item = self.scene.addText("PERCENT OF SAND")
    font = QFont()
    font.setPointSize(self.fx / 20.)
    item.setFont(font)
    item.setTransform(QTransform().fromTranslate(0.02 * self.fx, 0.7 * self.fy), True)
    item.update()
    item.setTransform(QTransform().rotate(-63), True)
    item.update()