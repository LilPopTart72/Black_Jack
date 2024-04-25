import Cards
import InputCommands as IC

# print(Cards.init.deck)
Cards.init.shuffle()

player = Cards.UserCards("Player")
dealer = Cards.UserCards("Dealer")


def basic_print(code):
    print(" ")
    print(player.cards)
    print("Player score:", player.score)

    print(dealer.cards)
    print("Dealer score:", dealer.score)
    if code == 1:
        return IC.play(input("Would you like to hit or stay? ").lower(), player)


def win_lose(code):
    choice = ""
    if code == 1:
        choice = basic_print(1)
        if player.score > 21:
            basic_print(0)
            input("you Busted")
            return "stop"
    else:
        basic_print(0)
        if dealer.score > 21:
            input("You Won The Dealer Busted")
        elif dealer.score > player.score:
            input("Dealer Won")
        elif dealer.score < player.score:
            input("you Won")
        elif dealer.score == player.score:
            input("its a tie")
    # print(choice)
    return choice


while True:
    print(Cards.init.deck)
    print(len(Cards.init.deck))
    while True:
        choice = win_lose(1)
        # print(choice)
        if choice == "stay":
            x = "continue"
            break
        elif choice == "stop":
            x = choice
            break
    if x == "continue":
        dealer.dealer_new_card()
        win_lose(0)
    elif len(Cards.init.deck) < 12:
        break
