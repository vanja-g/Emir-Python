def main():
    n = int(input("pick a number:"))
    sum = 0
    for i in range(n+1):
        sum = sum + i**3
    print(sum)
main()
