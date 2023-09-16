def main():
    sentence = input("tell me a sentence:")
    convert_to_sep_strings = sentence.split()
    print("your sentence has this many words", len(convert_to_sep_strings))


main()
