import Cards
import InputCommands as IC
import os

# print(Cards.init.deck)
Cards.init.shuffle()
player = Cards.UserCards()
dealer = Cards.UserCards()


def basic_print():
    print(" ")
    print(player.cards)
    print("Player score:", player.score)

    print(dealer.cards)
    print("Dealer score:", dealer.score)
    return IC.play(input("Would you like to hit or stay? ").lower(), player)


while True:
    choice = basic_print()
    if choice == "stay":
        break


