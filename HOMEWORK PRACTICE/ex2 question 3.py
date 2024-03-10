def user_string_reversed(user_string_split:list):
    reversed_string = ""
    for i in range(len(user_string_split)-1,-1,-1):
        reverse = user_string_split[i]
        reversed_string = reversed_string + reverse + " "
    return reversed_string

def main():
    user_string = str(input("Give me the first sentence that pops us into your head: "))
    user_string_split = user_string.split(" ")
    print(user_string_reversed(user_string_split))
main()