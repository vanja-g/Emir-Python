import random


def main():
    win_msg = ["wmsg1", "wmsg2",]#add acctual messages
    valid_choices = ["rock", "paper", "scissors"]
    key_beats_value = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    play_more = True
    while play_more:
        user_choice = str(input("rock paper scissor shoot>> "))

        computer_choice = valid_choices[random.randint(0, 2)]

        user_choice = user_choice.replace(" ", "").lower()
        print("You picked: " + user_choice)
        print("Computer picked: " + computer_choice)
        if user_choice in valid_choices:
            if user_choice == computer_choice:
                print("You both picked " + computer_choice)
                print("Its a draw!")
            else:
                if key_beats_value[user_choice] == computer_choice:
                    print(random.choice(win_msg))
                else:
                    print("you picked ")
        else:
            print("choice not valid")
            continue

        play_again_choice = str(input("Do you want to play more? (yes/no)"))
        if play_again_choice == "no":
            play_more = False

main()
