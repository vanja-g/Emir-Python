def main():
    user_input = int(input("give me a number"))
    for i in range(0,user_input+1):
        if i%2 == 1:
            print("odd")
        else:
            print(i)

main()