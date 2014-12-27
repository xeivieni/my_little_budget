#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):

        #exit action
        exitAction = QtGui.QAction(QtGui.QIcon('visu/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        #save action
        saveAction = QtGui.QAction(QtGui.QIcon('visu/save.png'), '&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save your database')
        saveAction.triggered.connect(self.save)

        #load action
        loadAction = QtGui.QAction(QtGui.QIcon('visu/load.png'), '&Load', self)
        loadAction.setShortcut('Ctrl+L')
        loadAction.setStatusTip('Load a data base')
        loadAction.triggered.connect(self.load)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(saveAction)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('1, 2, 3, FRIENDS')
        self.show()

    def save(self):
        print "lol"
    def load(self):
        print "save"

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()