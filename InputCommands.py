
def play(choice, player):
    if choice == "hit":
        # print(player.score) just a reminder for your tkinter gui you dont need to import for the variables and self.x
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
