def main():
    user_string = str(input("input your string? :"))
    chars_to_be_removed = int(input("how many chars should be removed? :"))
    new_string = ""
    for i in range(chars_to_be_removed,len(user_string)):
        new_string = new_string + user_string[i]

    print(new_string)
main()