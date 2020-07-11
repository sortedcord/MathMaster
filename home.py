from common_functions import newl, eq
from game import selectGame

def menu():
    print("1) Check Points      2)Play      3)Exit")
    newl(1)
    user_choice = str(input("Enter your choice: "))
    if user_choice == "1":
        print("you chose 1")
    elif user_choice == "2":
        eq("", 3)
        selectGame()
        print("you chose 2")
    elif user_choice == "3":
        exit()
    else: 
        print("Please choose a valid option out of 1, 2 or 3")
        menu()
    eq()

    


eq(" MathMaster NOGUI ", 2)
print("0.0.1")
newl(2)
menu()
