from ntpath import join
import random
import time
from tracemalloc import stop
import types
import numpy as np

#VARIABLES
AllCards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack(10)", "Queen(10)", "King(10)"]
Suits = ["♣", "♦", "♥", "♠"]
player1_deck = []
player2_deck = []
allselectedcards = []
player1playing = 1
player2playing = 1
Stop = False

#STARTING
print("Hello, welcome to blackjack made on python")
player1 = str(input("Whats the first players name?\n"))
player2 = str(input("Whats the second players name?\n"))

#MAIN GAME FUNCTION
def playing():
    while True:
        if player1playing == 1 and player2playing == 1:
            player1_turn()
            player2_turn()

        elif player1playing == 0:
            if player2playing == 0:
                print("GAME OVER")
                print(player1, " has ", player1_deck, "\n")
                print(player2, " has ", player2_deck, "\n")
                time.sleep(60)

        elif player1playing == 0:
            if player2playing == 1:
                player2_turn()
        
        elif player2playing == 0:
            if player1playing == 1:
                player1_turn()


#GENERATOR OF RANDOM CARDS
def generate_card():
    global allselectedcards
    global FinalCard
    global actualcurrentcard
    currentcard = str(random.choice(AllCards))
    currentsuit = str(random.choice(Suits))
    actualcurrentcard = currentcard + currentsuit
    FinalCard = "".join(actualcurrentcard)
    allselectedcards.append(FinalCard)

#CHECKS IF THE CARD HAS ALREADY BEEN SELECTED
def checkduplicates():
    if FinalCard in allselectedcards:
        generate_card()

#SERVE 2 CARDS TO PLAYER 1
def player1_starting():
    global player1playing
    global nextturn
    print("It is ", player1, "'s turn")
    generate_card()
    checkduplicates()
    player1_deck.append(FinalCard)
    generate_card()
    checkduplicates()
    player1_deck.append(FinalCard)
    player1_deck_output = "   ".join(player1_deck)
    print(player1_deck_output)

#SERVE 1 CARD TO PLAYER 1
def player1_turn():
    global nextturn
    global player1playing
    print("It is ", player1, "'s turn")
    generate_card()
    checkduplicates()
    player1_deck.append(FinalCard)
    player1_deck_output = "   ".join(player1_deck)
    print(player1_deck_output)

#SERVE 2 CARDS TO PLAYER 2
def player2_starting():
    global nextturn
    global player2playing
    print("It is ", player2, "'s turn")
    generate_card()
    checkduplicates()
    player2_deck.append(FinalCard)
    generate_card()
    checkduplicates()
    player2_deck.append(FinalCard)
    player2_deck_output = "   ".join(player2_deck)
    print(player2_deck_output)

def player2_turn():
    global nextturn
    global player2playing
    print("It is ", player2, "'s turn")
    generate_card()
    checkduplicates()
    player2_deck.append(FinalCard)
    player2_deck_output = "   ".join(player2_deck)
    print(player2_deck_output)



player1_starting()
stand = input("DEAL OR STAND\n")
while Stop != True:
    if stand == ("deal"):
        player1_turn()
        stand = input("DEAL OR STAND\n")

    else:
        Stop = True

else:
    Stop = False
    while Stop != True:
        print("\n" * 10)
        player2_starting()
        stand = input("DEAL OR STAND\n")
        if stand == ("deal"):
            player2_turn()
            stand = input("DEAL OR STAND\n")

        else:
            Stop = True


print("GAME OVER")
print(player1, " has ", player1_deck, "\n")
print(player2, " has ", player2_deck, "\n")
time.sleep(60)
