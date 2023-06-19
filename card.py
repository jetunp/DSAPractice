import random


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        return f"[{self.suit}-{self.rank}-{self.value}]"


class Deck:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return str(self.cards)

    def createDeck(self):
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        ranks = ['ace', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'jack', 'queen', 'king']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for i in range(len(suits)):
            for j in range(len(ranks)):
                self.cards.append(Card(suits[i], ranks[j], values[j]))

    def shuffleDeck(self):
        location1, location2, tmp = None, None, None
        for _ in range(1000):
            location1 = random.randint(0, len(self.cards)-1)
            location2 = random.randint(0, len(self.cards)-1)
            print(location1)
            tmp = self.cards[location1]
            self.cards[location1] = self.cards[location2]
            self.cards[location2] = tmp


class Player:
    def __init__(self, name):
        self.playerName = name
        self.playerCards = []

    def __repr__(self):
        return f"{self.playerCards}, {self.playerName}"


class Board:
    def __init__(self):
        self.cardsInTheMiddle = []
        self.players = []

    def __repr__(self):
        return str(self.players)

    def start(self, player1, player2):
        self.players.append(Player(player1))
        self.players.append(Player(player2))
        deck1 = Deck()
        deck1.createDeck()
        deck1.shuffleDeck()
        self.players[0].playerCards = deck1.cards[0:27]
        self.players[1].playerCards = deck1.cards[27:53]


gameBoard = Board()
gameBoard.start('jetun', 'pooja')
print(gameBoard.players)
