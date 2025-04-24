from __future__ import annotations
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.root = Tk()
        self.root.title("Maze Solver")
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

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
        self.x0: int = None
        self.y0: int = None
        self.x1: int = None
        self.y1: int = None
        self.center: Point = None

    def draw(self, top_left: Point, bottom_right: Point):
        self.x0 = top_left.x
        self.y0 = top_left.y
        self.x1 = bottom_right.x
        self.y1 = bottom_right.y
        self.center = Point((self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2)

        if self.window:
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

    def draw_move(self, to_cell: Cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        line = Line(self.center, to_cell.center)
        self.window.draw_line(line, color)
