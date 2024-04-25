
def play(choice, player):
    if choice == "hit":
        player.new_card()
    elif choice == "stay":
        return choice
    else:
        core_inputs(choice)


def ace(choice):
    if choice == "1":
        return 1
    if choice == "11":
        return 11
    else:
        core_inputs(choice)


def core_inputs(choice):
    if choice == "quit":
        print("Thank you for playing!")
    elif choice == "reshuffle":
        print("Reshuffling")
