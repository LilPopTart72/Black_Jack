import random
import InputCommands as IC


class Card:

    def __init__(self):
        self.suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.value = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
        self.deck = [[value, suit] for suit in self.suit for value in self.value]

    def shuffle(self):
        random.shuffle(self.deck)
        # print(self.deck)


class UserCards:
    def __init__(self, n):
        self.cards = [init.deck.pop(0), init.deck.pop(0)]
        self.score = 0
        self.name = n
        self.value_of_card()

    def new_card(self):
        self.cards.append(init.deck.pop(0))
        self.value_of_card()

    def dealer_new_card(self):
        if self.score < 17:
            self.cards.append(init.deck.pop(0))
            self.value_of_card()
        else:
            return

    def value_of_card(self):
        self.score = 0
        for card in self.cards:
            if type(card[0]) is int:
                self.score += int(card[0])
            elif type(card[0]) is str:
                if card[0] == "Ace":
                    if self.name == "Dealer":
                        self.dealer_ace(card)
                    elif self.name == "Player":
                        self.player_ace(card)
                elif card[0] == "Jack" or "Queen" or "King":
                    self.score += 10

    def dealer_ace(self, card):
        x = self.cards.index(card)
        if len(card) == 3:
            self.score += int(card[2])
        else:
            if self.score + 11 <= 21:
                self.cards[x].append(11)
                self.score += 11
            else:
                self.cards[x].append(1)
                self.score += 1

    def player_ace(self, card):
        x = self.cards.index(card)
        if len(card) == 3:
            self.score += int(card[2])
        else:
            print(" ")
            print(self.cards)
            value = IC.ace(input("Is this Ace a 1 or 11? "))
            self.cards[x].append(value)
            self.score += value


init = Card()
