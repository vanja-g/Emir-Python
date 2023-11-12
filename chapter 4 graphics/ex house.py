from graphics import *
def main():
    win = GraphWin("house",500,500)
    house_botleft = win.getMouse()
    house_topright = win.getMouse()
    house_body = Rectangle(house_botleft,house_topright)
    house_body.draw(win)

    door_top_center = win.getMouse()
    house_width = house_topright.getX() - house_botleft.getX()
    door_width = house_width / 5
    door_divided_by_2 = door_width/2
    door_botleft_x = door_top_center.getX() - door_divided_by_2
    door_botleft_y = house_botleft.getY()
    door_botleft_point = Point(door_botleft_x, door_botleft_y)
    door_topright_x = door_top_center.getX() + door_divided_by_2
    door_topright_y = door_top_center.getY()
    door_topright_point = Point(door_topright_x,door_topright_y)
    door_rectangle = Rectangle(door_botleft_point,door_topright_point)
    door_rectangle.draw(win)













    win.getKey()
    win.close()


main()