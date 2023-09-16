def main():
    amount_of_numbers = int(input("how many numbers will there be?:"))
    sum_of_numbers = 0
    for i in range(amount_of_numbers):
        number_pick = int(input("enter a number:"))
        sum_of_numbers = sum_of_numbers + number_pick

    average_of_numbers = float(sum_of_numbers / amount_of_numbers)
    print("the average of your numbers is", average_of_numbers)
main()