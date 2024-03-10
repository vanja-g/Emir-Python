def user_string_reversed(user_string_split:list):
    reversed_list = ""
    for i in range(len(user_string_split)-1,-1,-1):
        reverse = user_string_split[i]
        reversed_list = reversed_list + reverse + " "
    return reversed_list

def main():
    user_string = str(input("Give me the first sentance that pops us into your head: "))
    user_string_split = user_string.split(" ")
    print(user_string_reversed(user_string_split))
main()