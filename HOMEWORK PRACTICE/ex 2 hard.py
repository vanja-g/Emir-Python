def main():
    m = int(input("give me a number>>>"))
    n = int(input("give me another number>>>"))

    m = m*n
    n = m/n
    m = m/n

    # temp = m
    # m = n
    # n = temp

    print(m,n)




main()