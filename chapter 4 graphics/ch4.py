from graphics import *


def main():
    win = GraphWin("ex1", 500, 500)
    rectangle = Rectangle(Point(200, 200), Point(300, 300))
    rectangle.setFill("#004225")
    rectangle.draw(win)

    text = Text(Point(30, 30), "0")
    text.draw(win)

    while True:
        key = win.checkKey()
        if key == "w":
            rectangle.move(0, -5)
        elif key == "s":
            rectangle.move(0, 5)
        elif key == "a":
            rectangle.move(-5, 0)
        elif key == "d":
            rectangle.move(5, 0)
        elif key == "q":
            win.close()
            break
        num = text.getText()
        new_num = str(int(num) + 1)
        text.setText(new_num)


main()
