import random

class Card():

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.deck = [[suit, value] for suit in self.suit for value in self.value]
        #print(self.suit, self.value)
        #print(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        print(self.deck)

class Deck():

    def __init__(self):
        self.cards = []
        self.cards = [Card(suit, value) for suit in deck_dict['suit'] for value in deck_dict['value']]
        print(self.cards)


shuffled_deck = Card()
print(shuffled_deck.deck)
print(shuffled_deck.shuffle())
print(shuffled_deck.deck)