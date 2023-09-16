def main():
    print("this program calculates the future value of an investment")
    timescale = eval(input("how long do you play to have this investment going for?>>>>"))
    principal = eval(input("enter the initial principal>>>"))
    apr = eval(input("enter the annual intrest rate>>>>>"))

    for i in range(timescale):
        principal = principal * (1 + apr)

    print("the value of your investment is", principal)


main()
