#-*-coding:utf8;-*-
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PLAYERS=[]
GIVERS=[]
RECEIVERS=[]
DEBTS={}
AVERAGE=0.0
TOTAL=[]
BALANCE=[]
start=0

# class PLAYER(self):
#     def __init__(self, n = '', t = 0, b = 0):
#         self.name = n
#         self.total = t
#         self.balance = b
#
#     def total(self, amount):
#         print 'fonction calcul du total'
#         self.balance()
#
#     def balance(self):
#         print 'fonction calcul de la balance'


print 'test'

def expenseAdd(index, amount):
    print "index =", index, "amount = ", amount
    TOTAL[index] += float(amount)
    average()

def average():
    SUM = 0
    for i in TOTAL:
        SUM+=float(i)
        AVERAGE=SUM/len(PLAYERS)
    for index in range(len(BALANCE)):
        BALANCE[index] = TOTAL[index] - AVERAGE
    print "balance =", BALANCE

def payback(a,b,amount):
        # TOTAL[a] = TOTAL[a]-amount
        # TOTAL[b] = TOTAL[a]+amount
    print 'caca'

def debts():
    BAL_COPY = []
    for play in range(len(PLAYERS)):
        for bal in BALANCE:
            BAL_COPY.append(bal)
            if bal<0:
                GIVERS.append(play)
            elif bal == 0:
                pass
            else :
                RECEIVERS.append(play)

    for giver in GIVERS:
        while BAL_COPY[giver]<0 :
            for receive in RECEIVERS:
                while BAL_COPY[receive] > 0:
                    if receive+giver < 0:
                        DEBTS[[giver, receive]] = BALANCE[receive]
                    else:
                        DEBTS[[giver, receive]] = -BALANCE[giver]

    print DEBTS

def players(choice, name):
    if choice == "a":
        PLAYERS.append(name)
        BALANCE.append(0)
        TOTAL.append(0)

    elif choice == "d" :
        del PLAYERS[name]
        del BALANCE[name]
        del TOTAL[name]
    else:
        raise AttributeError("Wrong parameter")
    
def load(filename):
    filename = filename+".txt"
    srcfolder = HERE+"/../src/"
    for f in (f for f in os.listdir(srcfolder)):
        if f==filename:
            print srcfolder+f
            readfile(srcfolder+f)
            return 1

def readfile(file):
    del PLAYERS[:]
    try:
        myFile = open(file, 'r')
        pass
    except:
        return 0

    lines = myFile.readlines()
    flagPlayers =0
    flagTotal=0
    flagBalance=0

    for line in lines:
        if line in "PLAYERS\n":
            flagPlayers =1
        elif flagPlayers ==1 and line not in "TOTAL\n":
            PLAYERS.append(line[:-1])
        elif line in "TOTAL\n" and flagPlayers == 1:
            flagPlayers = 0
            flagTotal=1
        elif flagTotal==1 and line not in "BALANCE\n":
            TOTAL.append(float(line[:-1]))
        elif line in "BALANCE\n" and flagTotal == 1:
            flagTotal=0
            flagBalance=1
        elif flagBalance==1:
            BALANCE.append(float(line[:-1]))

    average()
    return 1

def save(filename):
    try:
        myFile = open(filename, "w")
        pass
    except:
        return 0

    myFile.write("PLAYERS\n")
    for playersLine in PLAYERS:
        myFile.write(str(playersLine)+"\n")
    myFile.write("TOTAL\n")
    for totalLine in TOTAL:
        myFile.write(str(totalLine)+"\n")
    myFile.write("BALANCE\n")
    for balanceLine in BALANCE:
        myFile.write(str(balanceLine)+"\n")
    myFile.close()
    return 1

