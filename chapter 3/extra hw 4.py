def main():
    row = 0
    for i in range(1,11):
        for the in range(1,11):
            row = the * i
            print(row, end=" ")
        print()
main()