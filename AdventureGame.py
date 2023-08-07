# greeting and introduction
def start_game():
    print("Welcome to the adventure game!")
    print("You are going to your friend's Bachelor party. Either you walk to the party (1) or book an Uber(2).")
    print("Which option do you choose? (1 or 2)")
    choice = input("> ")

    # deciding the path of game
    if choice == "1":
        option_1()
    elif choice == "2":
        option_2()
    else:
        print("Invalid choice. Try again.")
        start_game()

# path 1


def option_1():
    print("You end up reaching late!")
    print("Party is already over and so is the Game.")
    play_again()

# path 2


def option_2():
    print("Great idea, you got the best driver in the City!")
    print("Party Hard.")
    play_again()

# play again prompt


def play_again():
    print("Do you want to play again? (yes or no)")
    choice = input("> ")

    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Thank you for playing!")
    else:
        print("Invalid choice. Try again.")
        play_again()


start_game()
