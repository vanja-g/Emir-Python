def to_list_of_lists(dic: dict):
    result = []
    for item in dic.items():
        result.append(list(item))
    return result

def main():
    dic = {'apple': 1, 'banana': 2, 'grape': 3}
    print(to_list_of_lists(dic))

main()
