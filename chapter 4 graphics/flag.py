from graphics import *


def main():
    win = GraphWin("flag", 800, 400)

    win.setBackground("#001489")

    triangle = Polygon(Point(200, 0), Point(670, 0), Point(670, 400))
    triangle.setFill("#FFCD00")
    triangle.draw(win)

    pr = (40, 40)

    p1 = Point(18, 44)
    p2 = Point(36, 44)
    p3 = Point(40, 62)
    p4 = Point(42, 44)
    p5 = Point(62, 44)
    p6 = Point(44, 38)
    p7 = Point(48, 20)
    p8 = Point(40, 34)
    p9 = Point(32, 20)
    p10 = Point(36, 38)

    star = Polygon(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    star.setFill("white")
    star.setOutline("white")
    star.move(154, -10)
    star.draw(win)
    for i in range(1,11):
        new_star = star.clone()
        new_star.move(i * 40, i * 35)
        new_star.setFill("white")
        new_star.setOutline("white")
        new_star.draw(win)



main()
