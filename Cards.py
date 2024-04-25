import random

class Card():

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.deck = [[value, suit] for suit in self.suit for value in self.value]

    def shuffle(self):
        random.shuffle(self.deck)
        #print(self.deck)

    def card_name(self, suit, value):
        print(suit, value)

    def value_of_card(self, cards):
        score = 0
        for card in cards:
            if type(card[0]) is int:
                score += int(card[0])
            elif type(card[0]) is str:
                if card[0] == "Ace":
                    score += 1
                elif card[0] == "Jack" or "Queen" or "King":
                    score += 10
        return score


class UserCards():
    def __init__(self):
        self.cards = [init.deck.pop(0), init.deck.pop(0)]

    def score(self):
        return init.value_of_card(self.cards)


init = Card()

