
def place_in_inventory(item:str,item_list:list):
    item_list.append(item)


def count_inventory(item_list:list):
    dict = {}
    for item in item_list:
        if item in dict:
            dict[item] +=1
        else:
            dict[item] = 1
    return dict

def main():
    item_list = []
    while True:
        user_item = str(input("input what you will enter into the backpack: "))
        if user_item == "stop":
            break
        else:
            place_in_inventory(user_item,item_list)
    print(item_list)
    print(count_inventory(item_list))

main()