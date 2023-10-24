def main():
    credits_earned = int(input("how many credits do you have?>>>>"))
    if credits_earned < 7:
        print("you are a freshman")
    elif credits_earned < 16:
        print("you are a sophmore")
    elif credits_earned < 26:
        print("you are a junior")
    else:
        print("you are a senior")







main()