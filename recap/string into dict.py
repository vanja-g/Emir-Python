def main():
    dict = {}
    user_string = str(input("input string: "))

    for i in range(len(user_string)):
        if user_string[i] in dict:
            dict[user_string[i]] += 1
        else:
            dict[user_string[i]] = 1

    print(dict)


main()
