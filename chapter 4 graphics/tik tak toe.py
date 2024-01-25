from graphics import *

line_middle_coordinates = [225, 425]
field_centers = [
    [Point(125, 125), Point(325, 125), Point(525, 125)],
    [Point(125, 325), Point(325, 325), Point(525, 325)],
    [Point(125, 525), Point(325, 525), Point(525, 525)]]


def main():
    win = GraphWin("TIK TAK TOE", 650, 650)
    draw_board(win)

    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    turn = "o"
    game_won = False
    while True:
        # skontaj na koje je polje kliknuo - DONE
        click = win.getMouse()
        field_coords = get_clicked_field_coords(click)

        if turn == "o":
            # check if valid move, if not make player play again
            draw_O(field_coords, win)
            turn = "x"
        else:
            # check if valid move, if not make player play again
            draw_X(field_coords, win)
            turn = "o"

        # provjeri jel neko pobjedio
        if game_won:
            # do whatever you do when someone wins
            pass
        else:
            # change player turn
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


def get_clicked_field_coords(click: Point) -> tuple:
    colindex = rowindex = 0
    for coordinate in line_middle_coordinates:
        if click.getX() >= coordinate:
            colindex += 1
        if click.getY() >= coordinate:
            rowindex += 1

    return rowindex, colindex


def draw_O(field_coords: tuple, graph_win: GraphWin):
    x, y = field_coords
    field_center = field_centers[x][y]
    c = Circle(field_center, 55)
    c.setOutline("grey")
    c.setWidth(25)
    c.draw(graph_win)


def draw_X(field_coords: tuple, graph_win: GraphWin):
    x, y = field_coords
    field_center = field_centers[x][y]
    cx = field_center.getX()
    cy = field_center.getY()

    x_line_1 = Polygon(Point(cx-65, cy-65), Point(cx+35, cy+65), Point(cx+65, cy+65), Point(cx-35, cy-65))
    x_line_2 = Polygon(Point(cx-65, cy+65), Point(cx+35, cy-65), Point(cx+65, cy-65), Point(cx-35, cy+65))

    x_line_1.setFill("grey")
    x_line_1.setOutline("grey")
    x_line_2.setFill("grey")
    x_line_2.setOutline("grey")

    x_line_1.draw(graph_win)
    x_line_2.draw(graph_win)


main()
