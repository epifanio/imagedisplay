import sys
import os
from PyQt5.QtWidgets import QApplication, \
                            QWidget, \
                            QComboBox, \
                            QToolButton, \
                            QTableWidget, \
                            QTableWidgetItem, \
                            QFormLayout, \
                            QLineEdit, \
                            QPushButton, \
                            QHBoxLayout,\
                            QAbstractItemView

from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtCore


class runcommands(QWidget):
    def __init__(self, parent=None):
        super(runcommands, self).__init__(parent)

        layout = QFormLayout()

        self.commandlist = QComboBox()
        self.param = QLineEdit()
        self.runit = QToolButton()
        self.runit.setText('run')
        self.runit.clicked.connect(self.runcommand)
        self.commandlist.addItems(['simplerun.py', 'simplerun2.py'])
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.model = QStandardItemModel()
        self.table.setHorizontalHeaderLabels(['Process', 'Parameter', 'STDOut', 'Status', 'Kill Switch'])
        self.clean = QToolButton()
        self.clean.setText('Clean')
        self.clean.clicked.connect(self.cleanprocess)
        self.rowcount = 0

        layout.addRow(self.commandlist)
        layout.addRow(self.param)
        #layout.addRow(self.runit)
        #layout.addRow(self.clean)

        layout.addRow(self.table)

        self.vl = QHBoxLayout()
        self.vl.addWidget(self.runit)
        self.vl.addWidget(self.clean)
        layout.addRow(self.vl)

        self.setLayout(layout)
        self.setWindowTitle("Run & Monitor")
        self.commandrunning=0
        self.mylistofprocesses=[]

    def cleanprocess(self):
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        indextoremove=[]
        for i, v in enumerate(self.mylistofprocesses):
            if v.state() == 0:
                indextoremove.append(i)
                self.table.selectRow(i)
                self.rowcount=self.rowcount-1
            else:
                print(v.pid())
        index_list = []
        for model_index in self.table.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.table.removeRow(index.row())

        self.mylistofprocesses = [i for j, i in enumerate(self.mylistofprocesses) if j not in indextoremove]
        self.table.setSelectionMode(QAbstractItemView.NoSelection)


    def runcommand(self):
        # add a record in the QTableWidget
        # updating its row number at each run
        self.rowcount = self.rowcount + 1
        self.table.setRowCount(self.rowcount)
        print(self.rowcount)

        # add column 0: command string
        self.c1 = QTableWidgetItem()
        self.c1.setText("%s" % os.path.join(os.getcwd(), self.commandlist.currentText()))
        self.table.setItem(self.rowcount - 1, 0, self.c1)

        # add column 1: parameter string
        self.c2 = QTableWidgetItem()
        self.c2.setText("%s" % self.param.text())
        self.table.setItem(self.rowcount - 1, 1, self.c2)

        # add column 2 to store the  Process StandardOutput
        stdout_item = QTableWidgetItem()
        self.table.setItem(self.rowcount - 1, 2, stdout_item)

        # add column 3: index to store the process status (0: Not Running, 1: Starting, 2: Running)
        status_item = QTableWidgetItem()
        self.table.setItem(self.rowcount - 1, 3, status_item)

        # add column 4: kill button to kill the relative process
        killbtn = QPushButton(self.table)
        killbtn.setText('Kill')
        self.table.setCellWidget(self.rowcount - 1, 4, killbtn)

        # Initiate a QProcess running a system command
        process = QtCore.QProcess()
        command = 'python3' + ' ' + os.getcwd() + '/' + self.commandlist.currentText() + ' ' + self.param.text()
        process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        # connect the stdout_item to the Process StandardOutput
        # it gets constantly update as the process emit std output
        process.readyReadStandardOutput.connect(lambda: stdout_item.setText(str(process.readAllStandardOutput().data().decode('utf-8'))))

        # start the process
        # here I can inject some envs likeL
        # os.environ['newvar']='newval'
        # and remove them at the end (i can generate temporary gisrc file)
        print(process.systemEnvironment())
        process.start(command)

        # connect the kill button to the process.kill method, to stop the process
        killbtn.clicked.connect(process.kill)
        killbtn.clicked.connect(lambda: killbtn.setText('Killed'))

        # Connect the process to the stateChanged method, to update its status
        status = {QtCore.QProcess.NotRunning: "Not Running",
                  QtCore.QProcess.Starting: "Starting",
                  QtCore.QProcess.Running: "Running"}
        process.stateChanged.connect(lambda state: status_item.setText(status[state]))
        process.stateChanged.connect(lambda state: killbtn.setText('Terminated') if status[state]=="Not Running" else killbtn.setText('Kill'))
        process.stateChanged.connect(lambda state: killbtn.setEnabled(False) if status[state]=="Not Running" else killbtn.setText('Kill'))
        self.mylistofprocesses.append(process)


def main():
    app = QApplication(sys.argv)
    ex = runcommands()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()