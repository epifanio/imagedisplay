#!/usr/bin/env python


import os
from PyQt5 import QtWidgets, QtGui
from converter_ui import Ui_Converter

from multiprocessing import Process, Queue
from glob import glob
import pandas as pd
import numpy as np
import feather



class Converter(QtWidgets.QDialog, Ui_Converter):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.getASCII.clicked.connect(self.getASCIIDir)
        self.setFeather.clicked.connect(self.setFeatherFile)
        self.convert.clicked.connect(self.execute)
        self.reset_parser.clicked.connect(self.resetparser)
        self.advancedparsing.hide()
        self.geom = False
        self.data_time = False
        self.advancedsettings.stateChanged.connect(self.hideshowadvancedparsing)
        self.buildgeometrycheckbox.stateChanged.connect(self.buildgeometry)
        self.buildtimecheckbox.stateChanged.connect(self.buildtime)
        self.x_geom_label.hide()
        self.y_geom_label.hide()
        self.x_geom.hide()
        self.y_geom.hide()
        self.ping_time.hide()
        self.time_unit.hide()
        self.time_delta.hide()
        self.ping_time_label.hide()
        self.time_unit_label.hide()
        self.time_delta_label.hide()
        self.dirname = ''
        self.featherName = None
        self.preview.hide()


    def buildgeometry(self):
        self.x_geom_label.show()
        self.y_geom_label.show()
        self.x_geom.show()
        self.y_geom.show()
        if self.buildgeometrycheckbox.isChecked():
            self.geom = True
        else:
            self.geom = False
            self.x_geom_label.hide()
            self.y_geom_label.hide()
            self.x_geom.hide()
            self.y_geom.hide()



    def buildtime(self):
        if self.buildtimecheckbox.isChecked():
            self.ping_time.show()
            self.time_unit.show()
            self.time_delta.show()
            self.ping_time_label.show()
            self.time_unit_label.show()
            self.time_delta_label.show()
            self.data_time = True
        else:
            self.ping_time.hide()
            self.time_unit.hide()
            self.time_delta.hide()
            self.ping_time_label.hide()
            self.time_unit_label.hide()
            self.time_delta_label.hide()
            self.data_time = False

    def hideshowadvancedparsing(self):
        if self.advancedsettings.isChecked():
            self.advancedparsing.show()
        else:
            self.advancedparsing.hide()

    def resetparser(self):
        self.ping_time.setText('')
        self.time_unit.setText('')
        self.time_delta.setText('')
        self.x_geom.setText('')
        self.y_geom.setText('')
        self.skip_rows.setValue('')
        self.names.setText('')
        self.delimiterWS.setCurrentIndex(0)



    def execute(self):
        if not os.path.isdir(self.dirname):
            print("you need to set the input directory")
        elif self.featherName is None :
            print("you need to set the output feather file")
            from itertools import islice
            with open("/Users/epi/SHARED/SHARED/ASCII/170_001_0000_ascii_ara_beam_detail.txt") as myfile:
                head = list(islice(myfile, 20))
            for w in head:
                self.asciihead.append(w.replace('\n', ''))
        else:
            print(os.listdir(self.dirname))
            self.doit()

    def doit(self):
        lista = []
        self.queue = Queue()
        procs = [Process(target=self.slave1, args=(self.queue, i, self.geom, self.data_time)) for i in glob('%s/*' % self.dirname)]
        for proc in procs:
            proc.start()
        finished = 0

        while finished < len(glob('%s/*' % self.dirname)):
            # item = queue.get()
            lista.append(self.queue.get())
            finished = finished + 1
            left = len(glob('%s/*' % self.dirname)) - finished
            print('running ... %s file left' % left)
            print(finished)
            self.progressBar.setValue(finished)
            QtGui.QGuiApplication.processEvents()
        print('merging dataframes')
        acoustic = pd.concat(lista)
        print(acoustic.shape)
        self.progressBar.setValue(finished+1)
        print('writing dataframes to feather')
        feather.write_dataframe(acoustic, self.featherName[0])
        self.progressBar.setValue(finished + 2)
        print('done')
        df = feather.read_dataframe(self.featherName[0])
        #print(df.shape)
        print(df.columns)

    def getASCIIDir(self):
        self.dirname = QtWidgets.QFileDialog.getExistingDirectory()
        self.asciilist = os.listdir(self.dirname)
        self.ASCII.setText(self.dirname)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(len(glob('%s/*' % self.dirname))+2)
        print(self.asciilist)


    def setFeatherFile(self):
        self.featherName = QtWidgets.QFileDialog.getSaveFileName()
        self.feather.setText(self.featherName[0])
        print(self.featherName[0])



    def worker1(self, filename, geom, data_time):
        key = filename.split('/')[-1].split('.')[0][:-22]
        #names = ['Ping Time',
        #       'Ping Number',
        #       'Beam Number',
        #       'Easting',
        #       'Northing',
        #       'Depth',
        #       'Longitude',
        #       'Latitude',
        #       'Backscatter Value',
        #       'Corrected Backscatter Value',
        #       'True Angle']
        names = [x.strip(' ') for x in self.names.text().split(',')]
        #names = self.names.text().strip().split(',')
        print(names)
        df = pd.read_csv(filename,
                    skiprows=self.skip_rows.value(),
                    names=names,
                    delim_whitespace=True)
        if geom:
            df['Geom']=self.makegeom(df=df, x=self.x_geom.text(), y=self.y_geom.text())
        if data_time:
            df = df.assign(datetime=pd.to_datetime(df[self.ping_time.text()],
                                                   unit=self.time_unit.text()) - pd.Timedelta(self.time_delta.text(),
                                                                            unit=self.time_unit.text()),
                           line=key)
        return df

    def makegeom(self, df, x, y):
        geom = np.core.defchararray.add(
            np.core.defchararray.add(
                np.core.defchararray.add(
                    'Point(',
                    df[x].values.astype(str)),
                ' '),
            np.core.defchararray.add(
                df[y].values.astype(str),
                ')')
        )
        return geom

    def slave1(self, queue, filename, geom, data_time):
        print(filename)
        #val = worker1(filename)
        self.queue.put(self.worker1(filename, self.geom, self.data_time))