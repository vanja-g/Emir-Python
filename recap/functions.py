def get_fruits():
    dic = {"grape": "purple", "banana": "yellow", "apple": "red", "watermelon": "green", "lemon": "yellow",
           "lime": "green"}
    return dic


def remove_yellow_fruits(fruits: dict):
    keys = list(fruits.keys())
    for key in keys:
        if fruits[key] == "yellow":
            fruits.pop(key)


def to_fruit_string(fruits):
    my_string = ""
    for key in fruits.keys():
        my_string += (fruits[key] + " " + key + ", ")
    return my_string[:-2]


def to_dict(fruits: str):
    dict = {}
    temp_list = fruits.split(",")
    for item in temp_list:
        keyValue = item.lstrip().split(" ")
        dict[keyValue[1]] = keyValue[0]
    return dict




def main():
    fruits = get_fruits()
    remove_yellow_fruits(fruits)

    fruitString = to_fruit_string(fruits)
    fruitDict = to_dict(fruitString)

    print(fruitString)
    print(fruitDict)

    # Zadaca: napisati funkciju to_dict koja ce string koji smo napravili na kraju
    # vratiti opet u dictionary


main()
