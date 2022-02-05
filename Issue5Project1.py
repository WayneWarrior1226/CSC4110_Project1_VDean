print("TREASURE HUNTER!!!!!!")
## BUILD TREASURE CHEST

import random
from operator import add, sub
input('Press RETURN to BUILD CHEST or type exit to finish')

#Create CHEST

treasure_chest=[]
while "exit" not in treasure_chest:
	booty = input("Enter objects to be in chest: \n")
	treasure_chest.append(booty)
treasure_chest.pop(len(treasure_chest)-1)
print(treasure_chest)

## FUND YOUR BANK

input('Press RETURN to put money in!!!')
balance = int(input('Enter BEGINNING balance: \n'))
print(balance)

## PRINT MENU

while balance > 0:
        print ("input 1 if you would like to spin")
        print ("input 2 if you would like to grab")
        option = int(input('Enter what you would like to do: '))
        if option == 1:

## BET
                input('Press RETURN to place bet.') #ADDS USER INTERACTION: creates TENSION
                bet = int(input(f'Place wager: \n Note: Available deposit: {balance}. \n'))
                if bet > balance:
                        print ("Please enter a bet you can afford")
                        input('Press RETURN to place bet.') #ADDS USER INTERACTION: creates TENSION
                        bet = int(input(f'Place wager: \n Note: Available deposit: {balance}. \n'))
                else:
                        print("NOTE: you bet:",bet)
                        input("Get ready to spin the wheel!!")

#SPIN THE WHEEL
                spin = ("gold", "black")
                spin1 = random.choice(spin)  
                print(f'You spun: {spin1}!!')

                if spin1 == "gold":
                        print("You win!!")
                        balance += bet
                        print("Balance: ", balance)

                if spin1 == "black":
                        print("You lose!!")
                        balance -= bet
                        print("Balance: ", balance)

                if balance == (0):
                        print("Balance: 0 Game over")
                        break

        if option == 2:


#TREASURE GRAB
                grabsucc = ("gotit", "didnt")
                grab = random.randint(0, balance)
                grabsuccess = random.choice(grabsucc)

                if grabsuccess == "gotit":
                        print("You got ", grab)
                        balance += grab
                        print("Balance: ", balance)

                if grabsuccess == "didnt":
                        print("Your treasure was vulnerable and ", grab, " got snatched!")
                        balance -= grab
                        print("Balance: ", balance)

                if balance == (0):
                        print("Balance: 0 Game over")
                        break


