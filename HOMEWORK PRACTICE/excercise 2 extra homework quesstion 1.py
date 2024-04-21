def no_duplicates_here(user_list:list):
    temp_list = []
    for i in range(len(user_list)):
        if user_list[i] not in temp_list:
            temp_list.append(user_list[i])
    return temp_list
def main():
    user_list = list(input("input your list here: "))
    print(no_duplicates_here(user_list))
main()