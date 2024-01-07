
def average(numbers_list:list):
    avg = sum(numbers_list) / len(numbers_list)
    return avg

def smaller_than_five(numbers_list:list):
    len_list = len(numbers_list)
    smaller_nums = 0
    for i in range(len_list):
        if numbers_list[i] < 5:
            smaller_nums = smaller_nums + 1
    return smaller_nums




def main():
    nums = []
    for i in range(20):
        a = int(input("enter a number"))
        nums.append(a)
    avg = average(nums)
    print(avg)
    smaller_nums = smaller_than_five(nums)
    print(smaller_nums)
main()