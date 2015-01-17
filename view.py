__author__ = 'clementmondion'

from PyQt4 import QtCore, QtGui, uic
from collections import OrderedDict
from model import *
import sys

class main_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.players = OrderedDict()
        self.headers = ["Total", "Balance"]
        #self.average = ((self.players[i].__total/len(self.players.items())) for i in self.players.items())
        #print 'moyenne =', self.average
        #for i in info:
        #    headers.append(i[0])
        self.model = PlayerModel(self.players, self.headers)
        self.tableView.setModel(self.model)
        self.initButtons()


    def initButtons(self):
        self.plusButton.clicked.connect(self.addPlayer)
        self.actionQuit.triggered.connect(self.quit)
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)



    def save(self):
        print 'saving database'


    def load(self):
        print 'loading database'


    def addPlayer(self):
        name = raw_input('enter the name of the player')
        self.players[name] = Players(name)
        print players[name].name
        self.model.insertRows(name)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()
    B = Players('clem')
    print B.name