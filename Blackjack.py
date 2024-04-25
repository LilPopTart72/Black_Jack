import Cards
import InputCommands as Ic


def basic_print(code):
    print(" ")
    print(player.cards)
    print("Player score:", player.score)

    print(dealer.cards)
    print("Dealer score:", dealer.score)
    if code == 1:
        return Ic.play(player)


def win_lose(code):
    player_choice = ""
    if code == 1:
        player_choice = basic_print(1)
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
    return player_choice


Cards.init.new_deck()
Cards.init.shuffle()

while True:
    # print(Cards.init.deck)
    # print(len(Cards.init.deck))
    player = Cards.UserCards("Player")
    dealer = Cards.UserCards("Dealer")
    while True:
        choice = win_lose(1)
        if choice == "stay":
            x = "continue"
            break
        elif choice == "stop":
            x = choice
            break
    if x == "continue":
        dealer.dealer_new_card()
        win_lose(0)
    elif len(Cards.init.deck) < 30:
        Cards.init.new_deck()
        Cards.init.shuffle()
