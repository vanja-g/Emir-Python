from random import randint
def main():
    first_roll = roll_dice()
    if first_roll() in [2,3,12]:
        print("you lose")
    if first_roll() in [7,11]:
        print("you win")

    print("roll for point")

    next_roll = roll_dice()
    while next_roll not in [first_roll, 7]:
        next_roll = roll_dice()

    if next_roll == 7:
        print("you lose")
    else:
        print("you win")

def roll_dice():
    roll1 = randint(1,7)
    roll2 = randint(1,7)
    print(f"you rolled {0} and {1} = {2}", roll1, roll2, roll1+roll2)
    return roll1 + roll2

main()