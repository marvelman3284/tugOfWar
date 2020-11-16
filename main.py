# Imports
import random
from colorama import Fore, Style

#Constants
STATIONARY = "<-->" 
LEFT = "<--"
RIGHT = "-->"

#Variables
netForce = 0 

#Welcome message
print(Fore.RED + "Welcome to a tug of war simulator! You are on the right side of a box, and your opponent is on the left side of a box. \nYou will be given a choice of how many newtons of force you would like to apply to the box, and your opponent will be given a choice." + Style.RESET_ALL)


while True:
    aiChoice = int(random.randint(1, 50))
    userChoice = int(input(Fore.BLUE + "\nHow many newtons would you like to apply(Enter a number 1-50)? " + Style.RESET_ALL))
    if userChoice > 50:
        print("Your number must be below 50.")
    #Output
    else:
        print(Fore.GREEN + f"\nYou applied {userChoice} newtons, your opponent applies {aiChoice} newtons.")

        if userChoice > aiChoice:
            netForce = userChoice - aiChoice
            print(f"The net force is now {netForce}.\nThe box is now moving to the right({RIGHT}).\nThis is an example of unbalanced forces.")

            
        elif userChoice < aiChoice:
            netForce = aiChoice - userChoice
            print(f"The net force is now {netForce}.\nThe box is now moving to the left({LEFT}).\nThis is an example of unbalanced forces.")

        elif userChoice == aiChoice:
            netForce = 0
            print(f"The net force is now {netForce}.\nThe box isn't moving at all({STATIONARY}).\nThis is an example of balanced forces.")
            
