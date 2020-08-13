
"""
Given the next strings :
suits = "♠ ♡ ♢ ♣".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Define Card, Deck and Players Type aliases.

Card = combo suit en rank, list of 2 ele or string of 2, better string for in list Deck

Deck = set of 52 cards(suit+rank), list 52 elements
Players = a number, there should be a maximum
Write a program that will create and shuffle the deck. Then distribute the cards to 4 players. Using annotations.

Card
str -str str
deck
list - str
create
"""
class Deck():
    def __init__(self, suits, ranks): #suits and ranks hier liever optioneel
        self.suits = suits
        self.ranks = ranks

    def createDeck(self, suits: List[str], ranks: List[str]) -> List[str]:
        deck = []
        for logo in suits:
            for cardNumber in ranks:
                deck.append(logo + cardNumber)
        print(deck, len(deck))
        return deck

    def shuffleDeck(self,deck):
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
                deckShuffle.append(deck[randomNum])
                posList.remove(randomNum)  # !!!removes actual number not index such as this does : del posList[randomNum]
            print(len(deckShuffle), deckShuffle)
            print(posList)

        shuffleDeck()

    def dealCards(self, numPlayers,deckshuffle):
        player1 = []
        player2 = []
        player3 = []
        player4 = []
        for i in range(0, len(deckShuffle) // 4):
            player1.append(deckShuffle[i])
            player2.append(deckShuffle[i + 1])
            player3.append(deckShuffle[i + 2])
            player4.append(deckShuffle[i + 3])
        print("player 1 :", player1)
        print("player 2 :", player2)
        print("player 3 :", player3)
        print("player 4 :", player4)

    dealCards()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand

from typing import List

def createDeck(suits: List[str], ranks: List[str]) -> List[str]:
    deck = []
    for logo in suits:
        for cardNumber in ranks:
           deck.append(logo + cardNumber)
    print(deck, len(deck))
    return deck

createDeck("♠ ♡ ♢ ♣".split(), "2 3 4 5 6 7 8 9 10 J Q K A".split())
