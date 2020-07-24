"""
import random
def shuffleDeck():
    suits = "♠ ♡ ♢ ♣".split()
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    deck = []
    for logo in suits:
        for cardNumber in ranks:
           deck.append(logo + cardNumber)

    posList = []
    for i in range(0, len(deck)): posList.append(i)

    deckShuffle = []
    for i in range(0, len(deck)):
        randomNum = random.choice(posList)
        #print("random:", randomNum, " deck to be moved to shuffle: ", deck[randomNum])
        deckShuffle.append(deck[randomNum])
        posList.remove(randomNum) # !!!removes mumber not index such as this does : del posList[randomNum]
        #print("posList: ", posList)
        #print("shuffle: ",deckShuffle)
        #print("deck: ", deck)
        #print("length : ", len(posList))
        #print("----------------------")
    print(len(deckShuffle),deckShuffle)
    print(posList)


shuffleDeck()
"""
#!!!!!! TYPING DRILL 2 MADE WITH JUST A FUNCTION(CAN USE CLASSES TOO) !!!!
import random
def dealCards():
    suits = "♠ ♡ ♢ ♣".split()
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    deck = []
    for logo in suits:
        for cardNumber in ranks:
            deck.append(logo + cardNumber)
    #create a list with 52 items with values ranging from 0 to 51, to later generate a number from to shuffle
    posList = []
    for i in range(0, len(deck)): posList.append(i)
    # append to new deckShuffle the card from deck at index gnerated at random out of posList, everytime a number is generated it is removed from posList
    deckShuffle = []
    for i in range(0, len(deck)):
        randomNum = random.choice(posList)
        deckShuffle.append(deck[randomNum])
        posList.remove(randomNum)  # !!!removes actual number not index such as this does : del posList[randomNum]  deletes elem at index
    print(len(deckShuffle), deckShuffle)
    print(posList)
    #  deal the shuffled deck of 52 cards to 4 players
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    for i in range(0, len(deckShuffle), 4):
        #print(i)
        player1.append(deckShuffle[i])
        player2.append(deckShuffle[i + 1])
        player3.append(deckShuffle[i + 2])
        player4.append(deckShuffle[i + 3])
    print("player 1 :", player1)
    print("player 2 :", player2)
    print("player 3 :", player3)
    print("player 4 :", player4)

dealCards()