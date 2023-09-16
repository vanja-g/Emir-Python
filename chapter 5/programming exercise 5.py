def main():
    name = input("what is your name?:")
    result = 0
    for i in name:
        value = ord(i) - 96
        result = result + value
    print(result)


main()