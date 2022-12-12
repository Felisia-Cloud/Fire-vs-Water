from random import randint
from playsound import playsound

#create a list of play options
t = ["Fire", "Water"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Fire, Water? ")
    if player == computer:
        print("Tie!")
    elif player == "Fire":
        if computer == "Water":
            print("You lose!", computer, "covers", player)
    elif player == "Water":
        if computer == "Fire":
            print("You win!", player, "covers", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,1)]