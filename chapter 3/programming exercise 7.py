def main():
    import math
    x1=int(input("enter the first cordinates of plane 1:"))
    y1=int(input("enter the second cordinates of plane 1:"))
    x2=int(input("enter the first cordinate of plane 2:"))
    y2=int(input("enter the second cordinate of plane 2:"))
    ydiff = y2 - y1
    slope=((y2-y1)/(x2-x1))
    distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("your distance is",distance)
    print("your slope is", slope)
main()
