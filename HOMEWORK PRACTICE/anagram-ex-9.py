def get_input():
    word_1 = str(input("write your first word"))
    word_2 = str(input("write your second word"))
    return word_1, word_2


def is_anagram(word_1: str, word_2: str):
    if len(word_1) != len(word_2):
        return False
    checker = {}
    for i in range(len(word_1)):
        if word_1[i] not in word_2:
            return False
        if checker.get(word_1[i]) is None:
            checker[word_1[i]] = 1
        else:
            checker[word_1[i]] += 1

    for i in range(len(word_2)):
        checker[word_2[i]] -= 1

    for val in list(checker.values()):
        if val != 0:
            return False

    return True


def main():
    w1, w2 = get_input()
    if is_anagram(w1, w2):
        print("your word is a anagram")
    else:
        print("your word is not an anagram")


main()
