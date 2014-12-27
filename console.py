#-*-coding:utf8;-*-
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PLAYERS=[]
AVERAGE=0
TOTAL=[]
BALANCE=[]
start=0
class colors:
    OKBLUE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def debug(type, message):
    if type == "INFO":
        print colors.OKBLUE + message + colors.END
    elif type == "DEBUG":
        print colors.BLUE + message + colors.END
    elif type == "QUESTION":
        return raw_input(colors.GREEN + message + colors.END)
    elif type == "WARNING":
        print colors.ORANGE + message + colors.END
    elif type == "ERROR":
        print colors.RED + message + colors.END
    else:
        print message

def main():
    print "welcome to the main menu of 'My little budget' \n"
    print "press 'e' to access expenses menu\n"
    print "press 'b' to access pay back menu\n"
    print "press 'd' to see the debts\n"
    print "press 'p' to access players menu\n"
    print "press 'l' to load a table\n"
    print "press 's' to save a table\n"

    result = raw_input("choice: ")
    print result

    if result == "e": 
        expenses()
    elif result == "b": 
        payback()
    elif result == "d": 
        debts()
    elif result == "p": 
        players()
    elif result == "l": 
        load()
    elif result == "s": 
        save()
    else:
        print("incorrect selection please try again :")
        main()

def expenses():
    print "press 'r' to return to the main menu\n"
    if PLAYERS == []:
        print "there are no players please return to main menu and select 'p' to add a new player\n"
        main()
    else:
        print "select the players who paied today: \n"
        print "total of player =%s" %len(PLAYERS)
        for j in range(len(PLAYERS)):
            print "%s: name: %s \n" %(j+1, PLAYERS[j])
    result = int(raw_input("choice :"))
    print type(result)
    if result == "r":
        main()
    elif result < len(PLAYERS)+1:
        expenseAdd(result-1)
        print "add of a new expense for %s" %PLAYERS[result]
    else:
        print colors.ORANGE + result + "was entered. Debug" + colors.END
        print "incorrect selection please try again"
        expenses()

    
def expenseAdd(poorPlayer):
    expense = int(raw_input("enter the amount of the expense of %s : " % PLAYERS[int(poorPlayer)]))
    debug("DEBUG", str(type(expense)))
    try:
        TOTAL[poorPlayer] += expense
    except:
        debug("ERROR", "Please enter an integer value. Try again")
        expenseAdd(poorPlayer)
    print "the total amount of the expenses for %s is %s" %(PLAYERS[poorPlayer], TOTAL[poorPlayer])
    average()

def average():
    SUM = 0
    for i in TOTAL:
        SUM+=int(i)
        AVERAGE=SUM/len(PLAYERS)

def payback():
    #to be continued....
    print "press 'r' to return to the main menu\n"
    if result == "r":
        main()

def debts():
    #to be continued....
    print "here are the debts of the players:"
    
    
def players():
    print "press 'a' to add a player"
    print "press 's' to see the players"
    print "press 'd' ro delete a player"
    print "press 'r' to return to the main menu\n"
    result = raw_input ("choice: ")
    if result == "r":
        main()
    if result == "a":
        PLAYERS.append(raw_input("enter your players name:"))
        BALANCE.append(0)
        TOTAL.append(0)
        print "player succesfully added"
        print PLAYERS
        players()
    elif result == "s" :
        print "total of player =%s" %len(PLAYERS)
        for j in range(len(PLAYERS)):
            print "|name: %s \t | total of expenses = %s \t | balance = %s" %(PLAYERS[j], TOTAL[j], BALANCE[j])
    elif result == "d" :
        name = raw_input("enter the name of the player to delete:")
        i = 0
        for compare in PLAYERS:
            i+=1
            if compare == name:
                del PLAYERS[i]
                flag = 1
        if flag == 1:
            print "succesfull deletion of %s" %name
            players()
        else:
            print "unable to find %s in your database" %name
            players()
    else :
        print "incorrect selection please try again boloss"
        players()
    players()
    
    #to be continued....
    
def load():
    filename = raw_input("enter the name of the data base you want to load: ")
    filename = filename+".txt"
    srcfolder = HERE+"/../src/"
    flag=0
    filelist=[]
    for f in (f for f in os.listdir(srcfolder)):
        filelist.append(f)
        if f==filename:
            debug("INFO", "found file :%s" %f)
            answer = raw_input("do you want to open the file %s ? (y or n) : " %f)
            if answer == "y" or answer == "Y":
                flag=0
                readfile(srcfolder+f)
                debug("DEBUG", "what the fuck ??? %s" %flag)
                break
            else:
                flag=1
        else:
            flag=1
    debug("DEBUG", str(filelist))
    debug("DEBUG", str(flag))
    if flag==1:
        flag = 0
        debug("INFO", "couldn\'t find %s, other files found :" %filename)
        debug("INFO", '\n'.join(filelist))
        filewanted = debug("QUESTION", "type the name of the file you want to open (don\'t forget the extension) : ")
        for name in filelist:
            if filewanted == name:
                result = debug("QUESTION", "do you want to open the file %s (y or n) :" %name)
                if result == "y" or result =="Y":
                    readfile(srcfolder+name)
                    flag = 0
                    break
                else:
                    debug("INFO", "couldn\'t find open any database, back to main menu :")
                    main()
            else:
                flag=1
    if flag == 1:
        debug("INFO", "couldn\'t find open any database, back to main menu :")
        main()

def readfile(file):
    try:
        myFile = open(file, 'r')
        pass
    except:
        debug("ERROR", "couldn\'t open file %s, back to loading menu" %file)
        load()

    lines = myFile.readlines()
    flagPlayers =0
    flagTotal=0
    flagBalance=0

    for line in lines:
        debug("DEBUG", "%s" %line)
        if line in "PLAYERS\n":
            debug("DEBUG", "found PLAYERS in the text file, state of players flag = %s" %str(flagPlayers))
            flagPlayers =1
            debug("DEBUG", "found PLAYERS in the text file, state of players flag = %s" %str(flagPlayers))
        elif flagPlayers ==1 and line not in "TOTAL\n":
            PLAYERS.append(line[:-1])
        elif line in "TOTAL\n" and flagPlayers == 1:
            flagPlayers = 0
            flagTotal=1
            debug("DEBUG", "found TOTAL in the text file, state of players flag = %s state of total flag = %s" %(str(flagPlayers), str(flagTotal)))
        elif flagTotal==1 and line not in "BALANCE\n":
            TOTAL.append(int(line[:-1]))
        elif line in "BALANCE\n" and flagTotal == 1:
            flagTotal=0
            flagBalance=1
            debug("DEBUG", "found TOTAL in the text file, state of total flag = %s state of balance flag = %s" %(str(flagTotal), str(flagBalance)))
        elif flagBalance==1:
            BALANCE.append(int(line[:-1]))

    debug("INFO", "Database successfuly loaded, back to main menu")
    debug("DEBUG", "content of the database : \nPLAYERS :")
    debug("DEBUG", '\n'.join(PLAYERS))
    debug("DEBUG", "TOTAL :")
    debug("DEBUG", '\n'.join(str(TOTAL)))
    debug("DEBUG", "BALANCE :")
    debug("DEBUG", '\n'.join(str(BALANCE)))
    average()
    main()

def save():
    filename = raw_input("enter the name of the data base you want to save: ")
    filename = "../src/"+filename+".txt"
    try:
        myFile = open(filename, "w")
    except:
        print colors.RED + "error occured while opening the file" + colors.END
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
    print colors.BLUE+"saving ok"+colors.END
    main()

if __name__ == "__main__":     
    main() 
