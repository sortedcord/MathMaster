from common_functions import newl, eq
from random import *


def ADD(level):
    if level == "e":
        PointPerQuestion = 10
        a1 = 0
        a2 = 10
    elif level == "m":
        PointPerQuestion = 20
        a1 = 10
        a2 = 99
    elif level == "h":
        PointPerQuestion = 30
        a1 = 100
        a2 = 999
    else:
        print("Error - Invalid Level")
        print("Exiting Game")
        exit()
    EarnedPoints = 0
    while True:
        num1 = randint(a1, a2)
        num2 = randint(a1, a2)
        print("Calculate " + str(num1) + " + " + str(num2))
        newl(1)
        usr_answer = input("Enter Your Answer (enter -1 to quit): ")
        if usr_answer == num1+num2:
            newl(1)
            print("Correct Answer. You get " + str(PointPerQuestion) + " points")
            EarnedPoints += PointPerQuestion
            newl(2)
        elif usr_answer != num1+num2 and usr_answer != -1:
            newl(1)
            print("Wrong Answer! :(")
            newl(2)
        elif usr_answer == -1:
            newl(1)
            print("You have earned " + str(EarnedPoints) + " points")
            break
        else:
            print("Enter a valid Answer")
    return EarnedPoints

def pro(level):
    if level == "e":
        PointPerQuestion = 20
        a1 = 0
        a2 = 10
    elif level == "m":
        PointPerQuestion = 40
        a1 = 10
        a2 = 99
    elif level == "h":
        PointPerQuestion = 60
        a1 = 100
        a2 = 999
    else:
        print("Error - Invalid Level")
        print("Exiting Game")
        exit()
    EarnedPoints = 0
    while True:
        num1 = randint(a1, a2)
        num2 = randint(a1, a2)
        print("Calculate " + str(num1) + " x " + str(num2))
        newl(1)
        usr_answer = input("Enter Your Answer (enter -1 to quit): ")
        if usr_answer == num1*num2:
            newl(1)
            print("Correct Answer. You get " + str(PointPerQuestion) + " points")
            EarnedPoints += PointPerQuestion
            newl(2)
        elif usr_answer != num1*num2 and usr_answer != -1:
            newl(1)
            print("Wrong Answer! :(")
            newl(2)
        elif usr_answer == -1:
            newl(1)
            print("You have earned " + str(EarnedPoints) + " points")
            break
        else:
            print("Enter a valid Answer")
    return EarnedPoints


def selectGame():
    while True:
        eq(" OPERATION ", 2)
        print("1) Add       2) Subtract     3) Multiply     4) Divide       5) Exit")
        newl(2)
        operation = input("Enter a number according to the menu: ")
        while True:
            eq(" LEVELS ", 2)
            print("1) EASY       2) MEDIUM     3) HARD     4) Chose Operation")
            newl(2)
            level = input("Enter a number according to the menu: ")
            if operation == 1:
                if level == 1:
                    startGame("add", "e", 0)
                elif level == 2:
                    startGame("add", "m", 0)
                elif level == 3:
                    startGame("add", "h", 0)
                elif level == 4:
                    break
                else:
                    print("Wrong Level. Try again punk.")
            elif operation == 2:
                if level == 1:
                    startGame("sub", "e", 0)
                elif level == 2:
                    startGame("sub", "m", 0)
                elif level == 3:
                    startGame("sub", "h", 0)
                elif level == 4:
                    break
                else:
                    print("Wrong Level. Try again punk.")
            elif operation == 3:
                if level == 1:
                    startGame("pro", "e", 0)
                elif level == 2:
                    startGame("pro", "m", 0)
                elif level == 3:
                    startGame("pro", "h", 0)
                elif level == 4:
                    break
                else:
                    print("Wrong Level. Try again punk.")
            elif operation == 4:
                if level == 1:
                    startGame("div", "e", 0)
                elif level == 2:
                    startGame("div", "m", 0)
                elif level == 3:
                    startGame("div", "h", 0)
                elif level == 4:
                    break
                else:
                    print("Wrong Level. Try again punk.")
            elif operation == 5:
                break
            else:
                print("Thats not available. Try again.")


def startGame(operation, level, points):
    if operation == "add":
        newl(2)
        eq(" ADDITION ", 2)
        print("You have " + str(points) +  " points with you! Let's see how much you get this time!")
        newl(1)
        earned_points = ADD(level)
        newl(3)
        print("You now have " + str(earned_points) + " in total!")
        newl(1)
        eq("")
    elif operation == "pro":
        newl(2)
        eq(" MULTIPLICATION ", 2)
        print("You have " + str(points) +  " points with you! Let's see how much you get this time!")
        newl(1)
        earned_points = pro(level)
        newl(3)
        print("You now have " + str(earned_points) + " in total!")
        newl(1)
        eq()
