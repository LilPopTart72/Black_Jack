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
    if code == 1:
        choice = basic_print(1)
        if player.score > 21:
            print("you Busted")
            return "stop"
    else:
        basic_print(0)
        if dealer.score > 21:
            print("Dealer Busted")
        elif dealer.score > player.score:
            print("Dealer Won")
        elif dealer.score < player.score:
            print("you Won")
        elif dealer.score == player.score:
            print("its a tie")
    return choice


while True:
    choice = win_lose(1)
    if choice == "stay":
        x = "continue"
        break
    elif choice == "stop":
        x = choice
if x == "continue":
    dealer.dealer_new_card()
    win_lose(0)
