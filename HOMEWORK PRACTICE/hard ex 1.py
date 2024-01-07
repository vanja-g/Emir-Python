def main():
    number1 = int(input("What number is base>>>"))
    numberlist= str(input("give me a list of numbers(seperated by space)>>>"))
    numberlistsplit = numberlist.split(" ")
    all_greater = True
    for i in range(len(numberlistsplit)):
        if int(numberlistsplit[i]) < number1:
            all_greater = False

    if all_greater:
        print("all numbers are greater than base")
    else:
        print("all numbers arent greater than base")











main()