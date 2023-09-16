from math import *


def main():
    print("this program calculates the volume and surface of a sphere from its radius")
    radiusofsphere = int(input("what is the radius of your sphere?:"))
    v = (4 / 3 * pi * radiusofsphere ** 3)
    a = (4 * pi * radiusofsphere ** 2)
    print("the volume is", v)
    print("the surface area is", a)


main()
