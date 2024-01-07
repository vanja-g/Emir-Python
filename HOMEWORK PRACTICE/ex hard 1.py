def main():
    N = int(input("What is N?>>>>"))
    L = str(input("what is L? seperate every number with a comma>>>"))
    lsplit = L.split(",")
    all_smaller = True
    for i in range(len(lsplit)):
        if N > int(lsplit[i]):
            all_smaller = False
            break
    print(all_smaller)
main()