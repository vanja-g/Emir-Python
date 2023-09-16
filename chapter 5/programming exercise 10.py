def main():
    sentence = str(input("give me a random sentence:"))
    words = sentence.split(" ")
    count = 0
    for i in range(len(words)):
        count = count + len(words[i])
    print(count / len(words))


main()
