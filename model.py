__author__ = 'clementmondion'

from PyQt4 import QtGui, QtCore, uic
import sys


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, headers, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.items = headers
        print self.items

    def rowCount(self, parent):
        return len(self.items)

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            return self.items.values()[row].name


class PlayerModel(QtCore.QAbstractTableModel):

    def __init__(self, infos = {}, headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.infos = infos
        self.headers = headers


    def rowCount(self, parent):
        return len(self.infos.keys())


    def columnCount(self, parent):
        return 2


    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def data(self, index, role):

        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return self.infos.values()[row].total

            elif column == 1:
                return self.infos.values()[row].balanceCalculation()

        if role == QtCore.Qt.DisplayRole:

            row = index.row()
            column = index.column()
            if column == 0:
                return self.infos.values()[row].total

            elif column == 1:
                return self.infos.values()[row].balanceCalculation()


    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:

                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"
            else:
                return self.infos.values()[section].name


    def insertRows(self, position = 0, rows=1, parent = QtCore.QModelIndex()):
        position = len(self.infos.keys())
        self.beginInsertRows(parent, position, position + rows - 1)

        self.endInsertRows()

        return True


    def removeRows(self,  position, rows = 1, parent =  QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position)
        self.endRemoveRows()
        return True


    def insertColumns(self, position, columns, parent = QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)

        rowCount = len(self.infos)

        for i in range(columns):
            for j in range(rowCount):
                self.infos[j].insert(position, QtCore.QString("Not implemented"))

        self.endInsertColumns()

        return True



class Players():
    average = 0
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.balance = 0

    def addExpense(self, amount):
        self.total += float(amount)
        self.balanceCalculation()

    def balanceCalculation(self):
        self.balance = self.total - Players.average
        return self.balance
