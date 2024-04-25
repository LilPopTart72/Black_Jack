import random
import InputCommands as IC


class Card():

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.deck = [[value, suit] for suit in self.suit for value in self.value]

    def shuffle(self):
        random.shuffle(self.deck)
        # print(self.deck)

    def card_name(self, suit, value):
        print(suit, value)


class UserCards():
    def __init__(self):
        self.cards = [init.deck.pop(0), init.deck.pop(0)]
        self.score = 0
        self.value_of_card()

    def new_card(self):
        self.cards.append(init.deck.pop(0))
        self.value_of_card()

    def value_of_card(self):
        self.score = 0
        for card in self.cards:
            if type(card[0]) is int:
                self.score += int(card[0])
            elif type(card[0]) is str:
                if card[0] == "Ace":
                    self.score += IC.ace(input("Is this Ace a 1 or 11? "))
                elif card[0] == "Jack" or "Queen" or "King":
                    self.score += 10


init = Card()
