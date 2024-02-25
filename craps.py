from random import *


def main():
    win_counter = 0
    number_of_runs = int(input("how many times do you want to run craps"))
    for i in range(number_of_runs):
        win_counter = win_counter + play_craps()
    print(f"win counter is {win_counter}")
    print("win percent is",win_counter/number_of_runs)


def play_craps():
    dice_roll = roll_dice()
    loss_numbers = [2, 3, 12]
    win_numbers = [7, 11]
    if dice_roll in loss_numbers:
        # print("you lose")
        return 0
    if dice_roll in win_numbers:
        # print("you win")
        return 1
    # print("roll for point")

    while True:
        second_roll = roll_dice()
        if second_roll == dice_roll:
            # print("you win")
            return 1
        if second_roll == 7:
            # print("you lose")
            return 0


def roll_dice():
    sum = 0
    for i in range(2):
        dice_sides = randint(1, 7)
        sum = sum + dice_sides
    # print("your dice sum is ", sum)
    return sum


main()
