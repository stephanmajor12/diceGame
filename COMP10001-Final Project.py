#Final Assignment
#Stephan Major, 000828066
#Filename: COMP10001-Final Project.py

import random

def init1():
    global faces
    while True:
        try: 
            faces = int(input("Enter the # of faces [2,20]: "))
            #change from 1 to 2
            assert faces >= 2
            assert faces <= 20
        except (ValueError, AssertionError):
            print("You must enter a valid positive integer between 2-20, please try again.")
        else:
            break

def init2():
    global dies
    while True:
        try:
            dies = int(input("Enter # of dice [3,6]: "))
            assert dies >= 3
            assert dies <= 6
        except (ValueError, AssertionError):
            print("You must enter a number between 3 and 6.")
        else:
            break

def diceRoll():
    return random.randint(1, faces)

def diesAmount():
    global myList,listLength
    if dies == 3:
        myList = [diceRoll(),diceRoll(),diceRoll()]
        print(myList)
        listLength = 3
    elif dies == 4:
        myList = [diceRoll(),diceRoll(),diceRoll(),diceRoll()]
        print(myList)
        listLength = 4
    elif dies == 5:
        myList = [diceRoll(),diceRoll(),diceRoll(),diceRoll(),diceRoll()]
        print(myList)
        listLength = 5
    elif dies == 6:
        myList = [diceRoll(),diceRoll(),diceRoll(),diceRoll(),diceRoll(),diceRoll()]
        print(myList)
        listLength = 6

def diesamount():
    if dies >= 4:
        if myList[0] == myList[1] == myList[2] == myList[3]:
            bonus1 = bonus1+10
            pattern = pattern+1
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4]:
            bonus1 = bonus1+10
            pattern = pattern+1
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4] == myList [5]:
            bonus1 = bonus1+10
            pattern = pattern+1

def bonus1Fun():
    global bonus1,pattern
    if dies >= 4:
        if myList[0] == myList[1] == myList[2] == myList[3]:
            bonus1 = 10
            pattern = pattern+1
            return False
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4]:
            bonus1 = 10
            pattern = pattern+1
            return False
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4] == myList [5]:
            bonus1 = 10
            pattern = pattern+1
            return False
        else:
            return True

def pattern1():
    global pattern1
    if dies >= 4:
        if myList[0] == myList[1] == myList[2] == myList[3]:
            pattern1 = 1
            print("Pattern 1 bonus has been given as all dice are the same!")
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4]:
            pattern1 = 1
            print("Pattern 1 bonus has been given as all dice are the same!")
        elif myList[0] == myList[1] == myList[2] == myList[3] == myList[4] == myList [5]:
            pattern1 = 1
            print("Pattern 1 bonus has been given as all dice are the same!")

def pattern3():
    global shortCircuit
    if dies >= 5:
        for i in myList:
            if i <= average:
                shortCircuit = True
            else:
                shortCircuit = False
    else:
        print("Pattern 3 has not been matched as # dies > = 5.")
        shortCircuit = "nil"

def pattern4():
    global flag
    if dies >= 4 and faces > dies:
        if dies == 3:
            if myList[0] in myList[1:2]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[1] in myList[0:1:2]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1 
            elif myList[2] in myList[0:1]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            else:
                print("Pattern 4 has been matched. As all dice are different!")
                flag = 0
        if dies == 4:
            if myList[0] in myList[1:3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[1] in myList[0:1:3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag =1 
            elif myList[2] in myList[0:2:3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[3] in myList[0:2]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[3] == myList[2]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            else:
                print("Pattern 4 has been matched. As all dice are different!")
                flag = 0
        if dies == 5:
            if myList[0] in myList[1:4]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[1] in myList[0:1:4]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag =1 
            elif myList[2] in myList[0:2:4]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[3] in myList[0:3:4]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[4] in myList[0:3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[4] == myList[3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            else:
                print("Pattern 4 has been matched. As all dice are different!")
                flag = 0
        if dies == 6:
            if myList[0] in myList[1:5]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[1] in myList[0:1:5]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag =1 
            elif myList[2] in myList[0:2:5]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[3] in myList[0:3:5]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[4] in myList[0:3]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[4] == myList[5]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1
            elif myList[5] in myList[0:4]:
                print("Pattern 4 has not been matched. As some dice are the same!")
                flag = 1 
            else:
                print("Pattern 4 has been matched. As all dice are different!")
                flag = 0
    else:
        print("Pattern 4 does not apply, as either sides <= 4 or # sides <= # dice.")

#This stops a error, of roundAmount being called before assignment.
roundAmount = 0
def outputsMain():
    global sumList,myList,average,maxScore,faces,dies,percentage,averageRound,roundAmount
    sumList = sum(myList)
    average = sumList/listLength
    average = float("{:.0f}".format(average))
    maxScore = faces*dies
    percentage = sumList/maxScore
    roundAmount = roundAmount + 1
    averageRound = FinalScore/roundAmount
    print("These die sum to",sumList,"and have an average rounded value of",average)

def vars():
    global pattern,bonus,bonus1,bonus2,bonus3,bonus4,bonus5,bonusF
    pattern = 0
    bonus = 0
    bonus1 = 0
    bonus2 = 0
    bonus3 = 0
    bonus4 = 0
    bonus5 = 0
    bonusF = 0

#-------------Mainline-----------------
playAgain = 'yes'
FinalScore = 0
FinalScoreAvg = 0
print("Stephan Major, 000828066. COMP 10001 - W2020 Final Project.")
#---------

#Start
while playAgain == 'yes':
    vars()
    
    init1()

    init2()

    #Couldn't figure out how to do this with a diceRoll()*variable
    diesAmount()

    #reroll time
    #for some reason when this was in a function, it wouldn't work AT ALL.
    #so as last resort I have left it just how it is, I believe this happened as it kept saying "str not callable"
    rerollMain = input("Would you like to reroll any dice? ['yes' or 'no']:")
    rerollMain = rerollMain.lower()
    while rerollMain == ('yes'):
        rerollDie = input("Which die would you like to reroll? [1-6] ('Q' to exit):")
        if rerollDie == '1':
            myList[0] = diceRoll()
            print(myList)
        elif rerollDie == '2':
            myList[1] = diceRoll()
            print(myList)
        elif rerollDie == '3':
            myList[2] = diceRoll()
            print(myList)
        elif rerollDie == '4':
            myList[3] = diceRoll()
            print(myList)
        elif rerollDie == '5':
            myList[4] = diceRoll()
            print(myList)
        elif rerollDie == '6':
            myList[5] = diceRoll()
            print(myList)
        else:
            break

    outputsMain()

    #Check if all dice have same value
    #wont work as a function for some reason
    pattern1()
    if pattern1 == 1:
        bonus1 = 10
        pattern = pattern+1

    if bonus1Fun() == True:
        print("Pattern 1 bonus not given as",myList,"... some dice are different.")

    if bonus1Fun() == None:
        print("Pattern 1 bonus not given as there are less than 4 dice.")

    #Checks if it equals a prime number.
    pattern2 = 0
    if sumList > 1:
        for i in range(2,sumList):
            if (sumList % i) == 0:
                pattern2 == True
        else:
            pattern2 == False

    if pattern2 == False:
        bonus2 = 15
        pattern = pattern+1
        print("Pattern 2 bonus has been given as",sumList,"is a prime number!")
    
    if pattern2 == True:
        print("Pattern 2 bonus not given as",sumList,"is not a prime number.")

    #check for atleast half dice are greater than or equal to rounded average
    pattern3()

    #A short circuit error was occuring, line 194 would run multiple times, it would print any result that many times that a number was above average.
    if shortCircuit == True:
        print("Pattern 3 has been matched. As atleast half the dice are greater than or equal to the rounded average.")
        bonus3 = 5
        pattern = pattern+1
    if shortCircuit == False:
        print("Pattern 3 has not been matched. As atleast half the dice are less than the rounded average.")

    #check for diff values
    flag = 0

    #check for any same dices
    pattern4()
    if flag == 0:
        bonus4 = 8
        pattern = pattern+1

    #checks if no patterns match
    if pattern == 0:
        bonus5 = 1
        print("Since none of the other Patterns matched, a bonus is given.")
    else:
        bonus5 = 0
        print("Since other Patterns match, a bonus is not given.")

    studentNum = (828066 % 500)

    bonusF = (bonus1+bonus2+bonus3+bonus4+bonus5+studentNum)

    print("These are the bonuses:",bonus1,bonus2,bonus3,bonus4,bonus5,studentNum,"Final Bonus:",bonusF)
    roundScore = (sumList+bonusF)
    print("These dice are worth:",roundScore)

    FinalScore = FinalScore + roundScore
    
    #playAgain
    playAgain = input("Would you like to play another round? ['yes' or 'no']: ")
    playAgain = playAgain.lower()
    if playAgain == ('yes'):
        playAgain == 'yes'
        FinalScore = FinalScore + roundScore
        if roundAmount >= 2:
            if roundScore == averageRound:
                print("You got an average round score.")
            elif roundScore < averageRound:
                print("You got an above average round score.")
            elif roundScore > averageRound:
                print("You got a below average round score.")
    else:
        playAgain == 'no'
        FinalScoreAvg = (FinalScore/roundAmount)
        print("You played",roundAmount,"time(s)!")
        print("Your average score was:",FinalScoreAvg)
        print("Your final score was:",FinalScore)
        break


