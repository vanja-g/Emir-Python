def main():
    word1= str(input("give me a word:"))
    word2= str(input("give me another word:"))
    word_one_mid = int(len(word1)/2)
    print(word1[:word_one_mid] + word2 + word1[word_one_mid:])
main()