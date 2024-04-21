def char_delete_100(user_string:str,chars_to_be_removed:int):
    return user_string[chars_to_be_removed:]

def main():
    user_string = str(input("input your string? :"))
    chars_to_be_removed = int(input("how many chars should be removed? :"))
    print(char_delete_100(user_string,chars_to_be_removed))
main()