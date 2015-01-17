__author__ = 'clementmondion'
from model import *

if __name__ == "__main__":
    new = Player(raw_input("Name of the new player : "))
    new.addExpense(raw_input("How much did he pay ? "))
