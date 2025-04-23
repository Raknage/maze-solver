from window import Window, Point, Line


def main():
    win = Window(800, 600)
    start = Point(20, 20)
    end = Point(800-20, 600-20)
    line1 = Line(start, end)
    win.draw_line(line1, "red")
    win.canvas.create_line(20, 600-20, 800-20, 20, fill="black", width=5)
    win.wait_for_close()


main()
