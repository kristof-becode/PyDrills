import random
"""
class Card(self, suit, rank ): # ni beter subclass van deck?
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank

    def show_card(self):
        return f"{self.name}"
"""


#class Deck(self, suits : List[str], ranks : List[int] ):

class Deck:
    """
    suits = "♠ ♡ ♢ ♣" .split()
    ranks =  "2 3 4 5 6 7 8 9 10 J Q K A".split()
    """

    def __init__(self, su, ra):
        self.suits = su.split()
        self.ranks = ra.split()

    """
    def __init__(self, s = "♠ ♡ ♢ ♣" , r = "2 3 4 5 6 7 8 9 10 J Q K A"):
        suits = s.split()
        ranks = r.split()
    """
    def shuffle(self, player1, player2, player3, player4): #want create gebuert in def class of toch ook later zoals shuffle of samen met shuffle
        self.player1 = Player.naam
        self.player2 = Player.naam
        self.player3 = Player.naam
        self.player4 = Player.naam
        deck = []
        for logo in self.suits:
            for cardNumber in self.ranks:
                deck.append(logo + cardNumber)
        print(deck)
        # create a list with 52 items with values ranging from 0 to 51, to later generate a number from to shuffle
        posList = []
        for i in range(0, len(deck)): posList.append(i)
        # append to new deckShuffle the card from deck at index generated at random out of posList, everytime a number is generated it is removed from posList
        deckShuffle = []
        print(posList)
        for i in range(0, len(deck)):
            randomNum = random.choice(posList)
            # print(randomNum)
            deckShuffle.append(deck[randomNum])
            # print(deck[randomNum])
            posList.remove(randomNum)
        hand1 = []
        hand2 = []
        hand3 = []
        hand4 = []
        for i in range(0, len(deckShuffle), 4):
            hand1.append(deckShuffle[i])
            hand2.append(deckShuffle[i + 1])
            hand3.append(deckShuffle[i + 2])
            hand4.append(deckShuffle[i + 3])
        return f"{player1} with hand : {hand1} \n {player2} with hand : {hand2} \n {player3} with hand : {hand3} \n {player4} with hand : {hand4}"


"""
    def deal(cards, players): deal cards over players
"""
class Player:
    def __init__(self, player_num : int, name : str):
        self.player_num = player_num
        self.name = name

    def naam(self, name):
        return self.name

    def show_playercards(self): # nah....doesn't make sense, get that from deck shuffle
        return f"{self.name}"

mark = Player(1, "Mark")
cindy = Player(2, "Cindy")
pierot = Player(3, "Pierot")
java = Player(4, "Java")
z = Deck("♠ ♡ ♢ ♣", "2 3 4 5 6 7 8 9 10 J Q K A")
print(z.shuffle(mark,cindy,pierot,java))