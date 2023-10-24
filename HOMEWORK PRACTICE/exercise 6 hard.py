import random


def main():
    player_input = str(input("rock,paper,scissors shoot!!>>>"))
    player = player_input.replace(" ", "")
    rock_paper_scissors = ("rock", "paper", "scissors")

    computer = random.choice(rock_paper_scissors)
    if player == "shoot":
        print("funny guy")
        print("lets go again for real")
        main()

    if player not in rock_paper_scissors:
        print("Invalid move")

    if any(rock_paper_scissors):

        if player == "rock" and computer == "paper":
            print("rock losses to paper I win, HAHAHAAHHA")
        elif player == "rock" and computer == "scissors":
            print("ROCK beats scissors oh no I LOST")
        elif player == "rock" and computer == "rock":
            print("rock and rock is a tie?!?!?! my calculations were wrong")
        elif player == "scissors" and computer == "rock":
            print("rock beats scissors, i win muhahaahaha")
        elif player == "scissors" and computer == "paper":
            print("scissors beat paper no way I lost")
        elif player == "scissors" and computer == "scissors":
            print("no way scissors and scissors in a tie no way")
        elif player == "paper" and computer == "rock":
            print("paper beats rock I lose no way")
        elif player == "paper" and computer == "scissors":
            print("scissors beat paper I win hahahaha")
        elif player == "paper" and computer == "paper":
            print("paper and paper is a tie no way")

    while True:
        user_input1 = str(input("wanna play again? yes/no>>>>>"))
        user_input = user_input1.replace(" ","")
        if user_input.lower() == "no":
            print("unfortunate")
            exit()
        elif user_input.lower() == "yes":
            print("ready? go")
            main()
main()