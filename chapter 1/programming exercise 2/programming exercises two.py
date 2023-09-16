def main():
    print("this program illistrates a chaotic funtion")
    x = eval(input("enter a number between 1 and 0 >>>"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()