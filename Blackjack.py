import Cards

#print(Cards.init.deck)
Cards.init.shuffle()

player_cards = Cards.UserCards()
print(player_cards.cards)
print("Player score:", player_cards.score())

dealer_cards = Cards.UserCards()
print(dealer_cards.cards)
print("Dealer score:", dealer_cards.score())
