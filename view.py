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


class main_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.players = OrderedDict()
        self.headers = ["Total", "Balance"]
        self.table_model = PlayerModel(self.players, self.headers)
        self.players_model = ListModel(self.players)
        self.tableView.setModel(self.table_model)
        self.playerBox.setModel(self.players_model)
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
        self.addButton.clicked.connect(self.addExpense_)
        self.actionQuit.triggered.connect(self.close)
        self.actionSave.triggered.connect(self.save)
        self.actionLoad.triggered.connect(self.load)

    def addExpense_(self):
        index = self.playerBox.currentIndex()
        try:
            amount = float(self.amountField.text())
        except ValueError:
            QtGui.QMessageBox.information(self, 'Warning', 'Please enter a number')
        self.players.values()[index].addExpense(amount)
        QtGui.QMessageBox.information('self', 'Success', 'Expense successfully added')


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
        index = self.tableView.currentIndex()
        print index.row
        self.table_model.removeRows(index)

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
            self.table_model.insertRows()
        self.averageCalculation()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()