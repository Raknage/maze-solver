from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height, background="gray75")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

    def draw(self, top_left, bottom_right):
        self.x0 = top_left.x
        self.y0 = top_left.y
        self.x1 = bottom_right.x
        self.y1 = bottom_right.y

        if self.has_left_wall:
            left_wall = Line(Point(self.x0, self.y0), Point(self.x0, self.y1))
            self.window.draw_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self.x0, self.y0), Point(self.x1, self.y0))
            self.window.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self.x1, self.y0), Point(self.x1, self.y1))
            self.window.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.x0, self.y1), Point(self.x1, self.y1))
            self.window.draw_line(bottom_wall)
