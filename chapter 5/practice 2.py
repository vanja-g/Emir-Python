def main():
    word = str(input("give me a word"))
    middle = round(len(word)/2)-1
    print(word[middle-1] + word[middle] + word[middle+1])


main()