def main():
    list1 = list(input("Give me a list of numbers"))
    list2 = list(input("give me a list of numbers"))
    sum = []

    for i in range(len(list1)):
        if int(list1[i]) % 2 == 0:
            sum.append(list1[i])

    for i in range(len(list2)):
        if int(list2[i]) % 2 != 0:
            sum.append(list2[i])
    print(sum)

main()