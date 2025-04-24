from window import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell1.has_right_wall = False
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3.has_top_wall = False
    cell1.draw(Point(10, 10), Point(30, 30))
    cell2.draw(Point(30, 10), Point(50, 30))
    cell3.draw(Point(30, 30), Point(50, 50))
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)
    win.wait_for_close()


main()
