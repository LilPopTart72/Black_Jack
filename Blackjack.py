import Cards

#print(Cards.init.deck)
Cards.init.shuffle()
player_cards = Cards.UserCards()
dealer = Cards.UserCards()
def basic_print():
    print(" ")
    print(player_cards.cards)
    print("Player score:", player_cards.score)

    print(dealer.cards)
    print("Dealer score:", dealer.score)


basic_print()
player_cards.new_card()
basic_print()
