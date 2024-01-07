from graphics import *


def main():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    win = GraphWin("TIK TAK TOE", 650, 650)

    p1l1 = Point(50, 250)
    p2l1 = Point(600, 200)
    first_horizontal_line = Rectangle(p1l1, p2l1)
    first_horizontal_line.setFill("black")
    first_horizontal_line.draw(win)
    first_horizontal_middle = 225

    p1l2 = Point(50, 450)
    p2l2 = Point(600, 400)
    second_horizontal_line = Rectangle(p1l2, p2l2)
    second_horizontal_line.setFill("black")
    second_horizontal_line.draw(win)
    second_horizontal_middle = 425

    p1l3 = Point(250, 50)
    p2l3 = Point(200, 600)
    first_vertical_line = Rectangle(p1l3, p2l3)
    first_vertical_line.setFill("black")
    first_vertical_line.draw(win)
    first_vertical_middle = 225

    p1l4 = Point(450, 50)
    p2l4 = Point(400, 600)
    second_vertical_line = Rectangle(p1l4, p2l4)
    second_vertical_line.setFill("black")
    second_vertical_line.draw(win)
    second_vertical_middle = 425

    turn = "o"
    draw_O(Point(325, 325), win)
    draw_X(None, win)
    while True:
        click = win.getMouse()
        # skontaj na koje je polje kliknuo
        if turn == "o":
            # nacrtaj o u odgovarajucem polju
            pass
        else:
            # nacrtaj x u odgovarajucem polju
            pass

        # provjeri jel neko pobjedio
        win = False
        if win:
            # uradi sta radis kad neko pobjedi i izadji iz loopa
            pass
        else:
            # promjeni igraca kojem je red
            pass


def draw_O(centerOfField: Point, graphWin: GraphWin):
    c = Circle(centerOfField, 60)
    c.setOutline("red")
    c.setWidth(25)
    c.draw(graphWin)


def draw_X(centerOfField: Point, graphwWin: GraphWin):
    p1 = Point(465,285)
    p2 = Point(425,285)
    p3 = Point(375,350)
    p4 = Point(325,285)
    p5 = Point(285,285)
    p6 = Point(350,375)
    p7 = Point(285,465)
    p8 = Point(325,465)
    p9 = Point(375,400)
    p10 = Point(425,465)
    p11 = Point(465,465)
    p12 = Point(400,375)


def getCenterOfClickedField(pointClicked: Point):
    pass


main()
