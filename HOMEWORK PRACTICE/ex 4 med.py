def main():
    user_input = str(input("give me a letter>>>"))
    vowels = ("a,e,i,o,u")
    if user_input in vowels:
        print("its a vowel")
    else:
        print("its not a vowel")
main()