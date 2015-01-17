__author__ = 'clementmondion'

from PyQt4 import QtGui, QtCore, uic
import sys


class PlayerModel(QtCore.QAbstractTableModel):

    def __init__(self, infos = {}, headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__infos = infos
        self.__headers = headers


    def rowCount(self, parent):
        return len(self.__infos.keys())


    def columnCount(self, parent):
        return len(self.__infos.values())


    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def data(self, index, role):

        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return self.__infos[row].total
            elif column == 1:
                return self.__infos[row].balance



        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return "Name: " + self.__infos[row][column]

        if role == QtCore.Qt.DisplayRole:

            row = index.row()
            column = index.column()
            value = self.__infos[row][column]

            return value


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:

            row = index.row()
            column = index.column()
            self.__infos[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False


    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:

                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
            else:
                return QtCore.QString("%1").arg(section)

    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
    def insertRows(self, position = 0,rows=1, parent = QtCore.QModelIndex()):
        position = len(self.__infos.keys())
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):

            defaultValues = [QtCore.QString("Not implemented") for i in range(self.columnCount(None))]
            self.__infos[position].append(position, defaultValues)

        self.endInsertRows()

        return True


    def insertColumns(self, position, columns, parent = QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)

        rowCount = len(self.__infos)

        for i in range(columns):
            for j in range(rowCount):
                self.__infos[j].insert(position, QtCore.QString("Not implemented"))

        self.endInsertColumns()

        return True



class Players():
    def __init__(self, name):
        self.__name = name
        self.__total = 0
        self.__balance = 0
        print 'name is :', self.__name

    def addExpense(self, amount):
        self.__total += float(amount)
        print "new total for %s = %s " %(self.name, self.total)
        self.balance()


    def balance(self):
        self.__balance = self.__total - 1


