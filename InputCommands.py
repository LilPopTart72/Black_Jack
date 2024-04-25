
def play(player):
    while True:
        choice = input('Would you like to "hit" or "stay"? ')
        if choice == "hit":
            # print(player.score) just a reminder for your tkinter gui you don't need to import for the variables self.x
            player.new_card()
            break
        elif choice == "stay":
            return choice
        else:
            core_inputs(choice)


def ace():
    while True:
        choice = input("Is this Ace a 1 or 11? ")
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
    else:
        print("Not a valid choice")
