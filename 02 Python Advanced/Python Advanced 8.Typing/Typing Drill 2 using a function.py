
import random

#!!!!!! TYPING DRILL 2 MADE WITH JUST A FUNCTION(CAN USE CLASSES TOO) !!!!
import random
def dealCards():
    suits = "♠ ♡ ♢ ♣".split()
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    deck = []
    for logo in suits:
        for cardNumber in ranks:
            deck.append(logo + cardNumber)
    print(deck)
    #create a list with 52 items with values ranging from 0 to 51, to later generate a number from to shuffle
    posList = []
    for i in range(0, len(deck)): posList.append(i)
    # append to new deckShuffle the card from deck at index generated at random out of posList, everytime a number is generated it is removed from posList
    deckShuffle = []
    print(posList)
    for i in range(0, len(deck)):
        randomNum = random.choice(posList)
        #print(randomNum)
        deckShuffle.append(deck[randomNum])
        #print(deck[randomNum])
        posList.remove(randomNum)  # !!!removes actual number not index such as this does : del posList[randomNum]  deletes elem at index
    print(len(deckShuffle), deckShuffle) #deckShuffle only contains unique elements
    print(posList) # is empty list now
    #  deal the shuffled deck of 52 cards to 4 players
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    for i in range(0, len(deckShuffle),4):
        player1.append(deckShuffle[i])
        player2.append(deckShuffle[i + 1])
        player3.append(deckShuffle[i + 2])
        player4.append(deckShuffle[i + 3])
    print("player 1 :", player1, len(player1))
    print("player 2 :", player2, len(player2))
    print("player 3 :", player3, len(player3))
    print("player 4 :", player4, len(player4))

dealCards()