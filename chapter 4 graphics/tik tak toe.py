from graphics import *

line_middle_coordinates = [225, 425]
field_centers = [
        [Point(125,125), Point(325, 125), Point(525, 125)],
        [Point(125, 325), Point(325, 325), Point(525, 325)],
        [Point(125, 525), Point(325, 525), Point(525, 525)]]


def get_clicked_field_coords(click: Point, line_middle_coordinates: list) -> tuple:
    colindex = rowindex = 0
    for coordinate in line_middle_coordinates:
        if click.getX() >= coordinate:
            colindex += 1
        if click.getY() >= coordinate:
            rowindex += 1

    return rowindex, colindex


def main():
    win = GraphWin("TIK TAK TOE", 650, 650)
    draw_board(win)

    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    # for r in field_centers:
    #     for p in r:
    #         draw_O(p, win)

    # draw_X(None, win)

    turn = "o"
    while True:
        # skontaj na koje je polje kliknuo - DONE
        click = win.getMouse()
        coords = get_clicked_field_coords(click, line_middle_coordinates)

        if turn == "o":
            #check if valid move, if not make player play again
            draw_O(coords, win)
            turn = "x"
        else:
            # check if valid move, if not make player play again
            draw_X(coords, win)
            turn = "o"

        # provjeri jel neko pobjedio
        game_won = False
        if game_won:
            # uradi sta radis kad neko pobjedi i izadji iz loopa
            pass
        else:
            # promjeni igraca kojem je red
            pass


def draw_board(win):
    first_horizontal_line = Rectangle(Point(50, 250), Point(600, 200))
    first_horizontal_line.setFill("black")
    first_horizontal_line.draw(win)

    second_horizontal_line = Rectangle(Point(50, 450), Point(600, 400))
    second_horizontal_line.setFill("black")
    second_horizontal_line.draw(win)

    first_vertical_line = Rectangle(Point(250, 50), Point(200, 600))
    first_vertical_line.setFill("black")
    first_vertical_line.draw(win)

    second_vertical_line = Rectangle(Point(450, 50), Point(400, 600))
    second_vertical_line.setFill("black")
    second_vertical_line.draw(win)


def draw_O(field_coords: tuple, graph_win: GraphWin):
    x,y = field_coords
    field_center = field_centers[x][y]
    c = Circle(field_center, 60)
    c.setOutline("red")
    c.setWidth(25)
    c.draw(graph_win)


def draw_X(field_coords: tuple, graph_win: GraphWin):
    x, y = field_coords
    field_center = field_centers[x][y]

    p1 = Point(465, 285)
    p2 = Point(425, 285)
    p3 = Point(375, 350)
    p4 = Point(325, 285)
    p5 = Point(285, 285)
    p6 = Point(350, 375)
    p7 = Point(285, 465)
    p8 = Point(325, 465)
    p9 = Point(375, 400)
    p10 = Point(425, 465)
    p11 = Point(465, 465)
    p12 = Point(400, 375)


main()
