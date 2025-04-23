from window import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(Point(10, 10), Point(30, 30))
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(Point(30, 10), Point(50, 30))
    win.wait_for_close()


main()
