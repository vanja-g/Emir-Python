def main():
    print("how long will our fizzbuzz game go for?")
    user_input = int(input("pick a number>>>>> "))
    for i in range(1,user_input+1):
        if i % 5 == 0:
            if i % 3 == 0:
                print("fizzbuzz")
            else:
                print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
main()