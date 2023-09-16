def main():
    import math
    a = int(input("what is length of a?:"))
    b = int(input("what is length of b?:"))
    c = int(input("what is length of c?:"))
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("your area is",area)
main()
