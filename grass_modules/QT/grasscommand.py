#!/usr/local/bin/python36
import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import pandas as pd
from grassui import MainGui

# to run grass
GISDBASE = "/Users/epi/grassdata/"
MAPSET = "copy"
LOCATION_NAME = "project"


if sys.platform=='darwin':
    GISBASE ="/usr/local/grass-7.3.svn"
else:
    GISBASE ="/usr/local/grass-7.3.svn"


os.environ["GISBASE"] = GISBASE
sys.path.append(os.path.join(GISBASE, 'etc/python'))
os.environ["GISDBASE"] = GISDBASE
os.environ["MAPSET"] = MAPSET
os.environ["LOCATION_NAME"] = LOCATION_NAME

gisrc = 'MAPSET: %s\n' % os.environ["MAPSET"]
gisrc += 'GISDBASE: %s\n' % os.environ["GISDBASE"]
gisrc += 'LOCATION_NAME: %s\n' % os.environ["LOCATION_NAME"]
gisrc += 'GUI: text'

grass_gisrc = open('/tmp/gisrc', 'w')
grass_gisrc.write(gisrc)
grass_gisrc.close()
os.environ['GISRC'] = '/tmp/gisrc'

os.environ['PATH'] = '/usr/sbin:/bin/:/usr/bin:%s/bin:%s/scripts:/home/epi/.grass7/addons/bin:/home/epi/.grass7/addons/scripts:/usr/local/opt/gdal2/bin/:/Users/epi/.grass7/addons/bin:$PATH' % (GISBASE, GISBASE)

from grass.script import task as gtask

from parameters import GisOptionPrompt, GisOptionFlag, GisOptionString, GisOptionNum, GisOptionText, GisOptionMultiString, GisOptionFilePrompt

def gcommand(command):
    pd.options.mode.chained_assignment = None
    commandspecs = gtask.command_info(command)
    flags = []
    for i, v in enumerate(commandspecs['flags']):
        flags.append(pd.DataFrame.from_dict({0: v}, orient='index'))
    flags = pd.concat(flags).reset_index()
    flags.drop('index', 1, inplace=True)
    flags['guisection'].loc[(flags['guisection'] == '')] = 'Optional'

    params = []
    for i, v in enumerate(commandspecs['params']):
        params.append(pd.DataFrame.from_dict({0: v}, orient='index'))
    params = pd.concat(params).reset_index()
    params.drop('index', 1, inplace=True)

    params['guisection'].loc[
        (params['guisection'] == '') & (params['required'] == False)
    ] = 'Optional'
    params['guisection'].loc[
        (params['guisection'] == '') | (params['required'] == True)
    ] = 'Required'

    guisection = list(params['guisection'].unique()) + \
    list(flags['guisection'].unique())
    guisection = set(guisection)
    command_description = {}
    pr = {}
    fl = {}
    for i in guisection:
        pr[i] = params.loc[(params['guisection'] == i)].reset_index()
        fl[i] = flags.loc[(flags['guisection'] == i)].reset_index()
        del pr[i]['index']
        del fl[i]['index']
    command_description['description'] = commandspecs['description']
    command_description['keywords'] = commandspecs['keywords']
    command_description['usage'] = commandspecs['usage']
    command_description['parameters'] = pr
    command_description['flags'] = fl
    return command_description

class GrassCommand(QObject):
    def init(self):
        self.w = MainGui()
        #
        self.prompts = []
        self.datasurcesprompts = []
        self.filesprompts = []
        self.gflags = []
        self.goptionsstring = []
        self.goptionsmultistring = []
        self.goptionsnum = []
        self.goptionstext = []
        #
        self.parameters=[]
        self.datasurceprompt = []
        self.fileprompt = []
        self.flags=[]
        self.stringoption = []
        self.multistringoption = []
        self.numoption = []
        self.textoption = []
        #
        self.commandname = 'r.in.gdal'
        #
        self.message = ''
        gsec = gcommand(self.commandname)
        commandspecs = gtask.command_info(self.commandname)
        self.w.commanddescription.setText(commandspecs['description'])
        self.w.commanddescription.setWordWrap(True)
        keywords = ', '.join(gsec['keywords'])
        title = str(self.commandname) + " [" + keywords + ']'
        #title = str(self.commandname)+" "+str(gsec['keywords'])
        self.w.setWindowTitle(title)
        for i in gsec['parameters'].keys():
            tab = QtWidgets.QScrollArea()
            tab.setWidget(QtWidgets.QWidget())
            fl = QtWidgets.QVBoxLayout(tab.widget())
            tab.setWidgetResizable(True)
            tab.setObjectName(i)
            self.w.commandtab.addTab(tab, i)
            for j in gsec['flags'][i].index.values:
                flag = gsec['flags'][i].iloc[j]
                gflag = GisOptionFlag(fl, self.flags, flag)
                self.gflags.append(gflag)
            for j in gsec['parameters'][i].index.values:
                command = gsec['parameters'][i].iloc[j]
                if command['gisprompt']: # and command['age'] == 'old':
                    if command['prompt'] in ['raster', 'raster_3d', 'vector', 'label', 'region', 'group', 'all']:
                        print(command['prompt'])
                        fileopen = GisOptionPrompt(fl, self.parameters, command)
                        fileopen.setObjectName("fileopen_%s" % i)
                        self.prompts.append(fileopen)

                # TODO: handle here the datasource prompt
                #
                #    if command['gisprompt'] and command['prompt'] == 'datasource':
                #        fileopen = GisOptionDataSourcePrompt(fl, self.datasurceprompt, command)
                #        fileopen.setObjectName("fileopen_%s" % i)
                #        self.datasurcesprompts.append(fileopen)


                # TODO: handle here the file prompt
                #
                    if command['gisprompt'] and command['prompt'] == 'file':
                        fileopen = GisOptionFilePrompt(fl, self.fileprompt, command)
                        fileopen.setObjectName("fileopen_%s" % i)
                        self.filesprompts.append(fileopen)

            #for j in gsec['parameters'][i].index.values:
            #    command = gsec['parameters'][i].iloc[j]
                if command['type'] == 'string' and command['values'] != [] and not command['multiple']:
                    opt = GisOptionString(fl, self.stringoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsstring.append(opt)
            # TODO: handle multicheckbox here
                if command['type'] == 'string' and command['values'] != [] and command['multiple']:
                    opt = GisOptionMultiString(fl, self.multistringoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsmultistring.append(opt)

            #for j in gsec['parameters'][i].index.values:
            #    command = gsec['parameters'][i].iloc[j]
                if command['type'] == 'integer' or command['type'] == 'float' and not command['multiple']:
                    opt = GisOptionNum(fl, self.numoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsnum.append(opt)
                if command['type'] == 'integer' or command['type'] == 'float' and command['multiple']:
                    opt = GisOptionText(fl, self.textoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionstext.append(opt)
            spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            fl.addItem(spacerItem4)
        doclink = os.path.join(GISBASE, 'docs/html', self.commandname)
        self.w.manualpage.load(QUrl('file://%s.html' % doclink))
        #self.w.runcommand.clicked.connect(self.getParam)
        self.w.copycommand.clicked.connect(self.messagecopy)
        self.w.closecommand.clicked.connect(self.w.close)


        for i in self.gflags:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsstring:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsmultistring:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionstext:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsnum:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.prompts:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.filesprompts:
            i.valueUpdated.connect(self.handleValueUpdated)

        self.status = {}
        self.status['flags'] = []
        for i in range(self.w.commandtab.count()):
            #print(i, self.w.commandtab.widget(i).objectName())
            if self.w.commandtab.widget(i).objectName() == 'Required':
                self.w.commandtab.tabBar().moveTab(i, 0)
            if self.w.commandtab.widget(i).objectName() == 'CommandOutput':
                self.w.commandtab.tabBar().moveTab(i, self.w.commandtab.count() - 2)
            if self.w.commandtab.widget(i).objectName() == 'Manual':
                self.w.commandtab.tabBar().moveTab(i, self.w.commandtab.count() - 1)
        print(self.w.commandtab.count())
        self.w.commandtab.setCurrentIndex(0)
        self.w.show()


    def handleValueUpdated(self, value):
        if len(value.split('=')) > 1:
            self.status[value.split('=')[0]] = value.split('=')[1]
        if len(value.split(':')) > 1:
            if value.split(':')[1] != 'None':
                self.status['flags'].append(value.split(':')[1])
            else:
                self.status['flags'] = [i for i in self.status['flags'] if value.split(':')[0] not in i]
        paramstatus = ' '.join(['{}={}'.format(k, v) for k, v in self.status.items() if k != 'flags'])
        flagstatus = ' '.join(self.status['flags'])
        self.message = self.commandname+' '+paramstatus+' '+flagstatus
        self.w.statusbar.showMessage(self.message)
        QtWidgets.QApplication.processEvents()

    def messagecopy(self):
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.message, mode=cb.Clipboard)
        #print(self.w.commandtab.widget(0).objectName())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = GrassCommand()
    p.init()
    sys.exit(app.exec_())
