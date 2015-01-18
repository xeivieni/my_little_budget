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
        self.actionQuit.triggered.connect(self.close)
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)



    def save(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Save Database",
                                                '/Users/clementmondion/Documents/personal_projects/my_little_budget/src/',
                                                 "TEXT (*.txt)")
        my_file = open(path, 'w')
        for key in self.players.keys():
            my_file.write(key + ":" + str(self.players[key].total) + "\n")
        my_file.close()



    def load(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Open Database",
                                                '/Users/clementmondion/Documents/personal_projects/my_little_budget/src/',
                                                 "TEXT (*.txt)")
        my_file = open(path, 'r')
        for line in my_file.readlines():
            elements = line.split(":")
            self.addPlayer(elements[0].strip("'"))


    def addPlayer(self, text = ''):
        if text is False:
            text, ok = QtGui.QInputDialog.getText(self, 'Add a new player',
                                                  'Enter your name:')
            while text in self.players.keys():
                text, ok = QtGui.QInputDialog.getText(self, 'Add error : name already taken',
                                                  'Please choose another name:')
        name = str(text)
        self.players[name] = Players(name)
        self.model.insertRows(name)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()