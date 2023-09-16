def main():
    word = str(input("give me a single word:"))
    middle_position = round(len(word)/2)

    print(word[0] + word[middle_position] + word[-1])


main()