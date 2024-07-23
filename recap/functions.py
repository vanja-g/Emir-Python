def get_fruits():
    dic = {"grape": "purple","banana":"yellow","apple":"red","watermelon": "green","lemon": "yellow","lime":"green"}
    return dic

def remove_yellow_fruits(fruits:dict):
    keys = list(fruits.keys())
    for key in keys:
        if fruits[key] == "yellow":
            fruits.pop(key)


def to_fruit_string(fruits):
    my_string = ""
    for key in fruits.keys():
        my_string += (fruits[key]+ " " + key + ", ")
    return my_string


def main():
    fruits = get_fruits()
    remove_yellow_fruits(fruits)

    fruitString = to_fruit_string(fruits)

    print(fruitString)

    #Zadaca: napisati funkciju to_dict koja ce string koji smo napravili na kraju
        #vratiti opet u dictionary

main()