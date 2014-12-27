import sys
from PyQt4 import QtCore, QtGui, uic
import functions



class main_window(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # load MAIN user interface

        uic.loadUi("dialog.ui", self)
        self.setWindowTitle('1, 2, 3 Friends')

        #load popup for text entry
        self.text_popup = QtGui.QDialog(self)
        uic.loadUi(("text_popup.ui"), self.text_popup)
        self.text_popup.setWindowTitle('Ajouter un participant')

        #load popup for list choice
        self.list_popup = QtGui.QDialog(self)
        uic.loadUi(("list_popup.ui"), self.list_popup)
        self.list_popup.setWindowTitle('Supprimer un participant')

        #load popup for list choice & text entry
        self.full_popup = QtGui.QDialog(self)
        uic.loadUi(("full_popup.ui"), self.full_popup)
        self.list_popup.setWindowTitle('Ca depend des cas')

        #connexion des boutons de la fenetre principale :
        self.loadButton.clicked.connect(self.load_tab)
        self.saveButton.clicked.connect(self.save_tab)
        self.quitButton.clicked.connect(self.close)
        self.add_player.clicked.connect(self.write_popup)
        self.delete_player.clicked.connect(self.choice_popup)
        self.add_expense.clicked.connect(self.price_popup)

        #connexion des boutons des popup
        self.text_popup.ok_popup.clicked.connect(self.player_add)
        self.list_popup.ok_listpopup.clicked.connect(self.player_del)
        self.full_popup.ok_fullpopup.clicked.connect(self.expense_add)

#===========================================Init des popup=============================================================#

    def price_popup(self):
        self.full_popup.show()
        self.full_popup.list.clear()
        self.full_popup.list.addItems(PLAYERS)

    def write_popup(self):
        self.text_popup.show()

    def choice_popup(self):
        self.list_popup.show()
        self.list_popup.list.addItems(PLAYERS)

    def browser(self):
        """
            This fonction allows the user to load the correct database
        """
        return QtGui.QFileDialog.getOpenFileName(self, "Open Database",
                                                 "/Users/clementmondion/Documents/personal_projects/my_little_budget/src/",
                                                 "TEXT (*.txt)")

    def save_pop(self):
        return QtGui.QFileDialog.getSaveFileName(self, "Open Database",
                                                 "/Users/clementmondion/Documents/personal_projects/my_little_budget/src/",
                                                 "TEXT (*.txt)")

#=========================================Fin init des popup===========================================================#

    def player_add(self):
        """
        This function adds a new player by calling the players function from functions.py
        """
        players("a", str(self.text_popup.name_field.text()))
        self.text_popup.close()
        self.display()

    def player_del(self):
        players("d", self.list_popup.list.currentIndex())
        self.list_popup.close()
        self.display()

    def load_tab(self):
        load_file = self.browser()
        result = readfile(load_file)
        if result:
            self.display()
        else:
            self.popup("Error loading the database", "Database not found")

    def save_tab(self):
        save_file = self.save_pop()
        result = save(save_file)
        if result:
            self.popup("saving successful", "Your database have been saved")
        else:
            self.popup("Error saving the database", "Database not found")

    def popup(self, title, msg):
        """
        Pop up configuration
        """
        QtGui.QMessageBox.information(self, title, msg)

    def expense_add(self):
        expenseAdd(self.full_popup.list.currentIndex(), self.full_popup.amount_field.text())
        self.full_popup.close()
        self.display()

    def display(self):
        self.chart.clear()
        self.total.setText(str(AVERAGE))
        for player, total, balance in zip(PLAYERS, TOTAL, BALANCE):
            self.chart.appendPlainText("Joueur %s : %s \t|\tTotal des depenses : %s\t|\tBalance : %s" % (
            PLAYERS.index(player) + 1, player, total, balance))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = main_window()
    window.show()
    app.exec_()