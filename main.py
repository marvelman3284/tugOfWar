# Imports
import random

#Constants
STATIONARY = "<-->" 
LEFT = "<--"
RIGHT = "-->"

#Variables
netForce = 0 
aiChoice = int(random.randint(1, 50))

#Welcome message
print("Welcome to a tug of war simulator! You are on the right side of a box, and your opponent is on the left side of a box. \nYou will be given a choice of how many newtons of force you would like to apply to the box, and your opponent will be given a choice.\n")


while True:
    userChoice = int((input("How many newtons would you like to apply(Enter a number 1-50)? ")))
    if userChoice > 50:
        print("Your number must be below 50.")
    #Output
    else:
        print(f"You applied {userChoice} newtons, your opponent applies {aiChoice} newtons.")

        if userChoice > aiChoice:
            netForce = userChoice - aiChoice
            print(f"The net force is now {netForce}.\nThe box is now moving to the right({RIGHT}).\nThis is an example of unbalanced forces.")

            
        elif userChoice < aiChoice:
            netForce = aiChoice - userChoice
            print(f"The net force is now {netForce}.\nThe box is now moving to the left({LEFT}).\nThis is an example of unbalanced forces.")

        elif userChoice == aiChoice:
            netForce = 0
            print(f"The net force is now {netForce}.\nThe box isn't moving at all({STATIONARY}).\nThis is an example of balanced forces.")
            
