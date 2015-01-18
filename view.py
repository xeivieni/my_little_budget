#!/usr/bin/python
#-*- coding: <utf-8> -*-
__author__ = 'clementmondion'


from PyQt4 import QtCore, QtGui, uic
from collections import OrderedDict
from model import *
import sys

RED   = QtGui.QColor(255,0,0)
GREEN = QtGui.QColor(0,255,0)
BLUE  = QtGui.QColor(0,0,255)
YELLOW = QtGui.QColor("#FFFF00")


class main_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.players = OrderedDict()
        self.headers = ["Total", "Balance"]
        self.currency = QtCore.QStringList()
        self.currency << "Euro" << "Dollar" << "Pounds"
        #self.average = ((self.players[i].__total/len(self.players.items())) for i in self.players.items())
        #print 'moyenne =', self.average
        #for i in info:
        #    headers.append(i[0])
        print self.players.keys()
        self.tablemodel = PlayerModel(self.players, self.headers)
        self.currencymodel = ListModel(self.currency)
        self.playersmodel = ListModel(self.players.keys())
        self.tableView.setModel(self.tablemodel)
        self.currencyBox.setModel(self.currencymodel)
        self.playerBox.setModel(self.playersmodel)
        self.initButtons()

    def averageCalculation(self):
        total = 0
        for i in self.players.keys():
            total += self.players[i].total
        Players.average = total/len(self.players.items())
        for i in self.players.keys():
            self.players[i].balanceCalculation()

    def initButtons(self):
        self.plusButton.clicked.connect(self.addPlayer)
        self.minusButton.clicked.connect(self.delPlayer)
        self.actionQuit.triggered.connect(self.close)
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)


    def save(self):
        path = QtGui.QFileDialog.getSaveFileName(self, "Save Database",
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
            player_name = elements[0].strip("'")
            player_amount = elements[1]
            if player_name not in self.players.keys():
                self.addPlayer(player_name, True)
                self.players[player_name].addExpense(player_amount)

            else :
                QtGui.QMessageBox.information(self, 'Warning', '%s has been found in actual database and loaded\
                                              database\nRenaming in %s' %(player_name,
                                                                          player_name+"1"))
                self.addPlayer(player_name+"1", True)
                self.players[player_name+"1"].addExpense(player_amount)
        self.averageCalculation()


    def delPlayer(self):
        print 'index ? ',self.tablemodel.rowCount(QtCore.QModelIndex())
        self.tablemodel.removeRows(0)

    def addPlayer(self, text = '', ok = ''):
        if text is False and ok is not True:
            text, ok = QtGui.QInputDialog.getText(self, 'Add a new player',
                                                  'Enter your name:')
            while text in self.players.keys():
                text, ok = QtGui.QInputDialog.getText(self, 'Add error : name already taken',
                                                  'Please choose another name:')
        if ok :
            name = str(text)
            self.players[name] = Players(name)
            self.tablemodel.insertRows()
        self.averageCalculation()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()