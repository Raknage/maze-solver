from __future__ import annotations
from window import Window, Line, Point


class Cell:
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
        self._x0: int = None
        self._y0: int = None
        self._x1: int = None
        self._y1: int = None
        self._center: Point = None
        self.visited = False

    def draw(self, top_left: Point, bottom_right: Point):
        self._x0 = top_left.x
        self._y0 = top_left.y
        self._x1 = bottom_right.x
        self._y1 = bottom_right.y
        self._center = Point((self._x0 + self._x1) / 2, (self._y0 + self._y1) / 2)

        if self.window:
            left_wall = Line(Point(self._x0, self._y0), Point(self._x0, self._y1))
            top_wall = Line(Point(self._x0, self._y0), Point(self._x1, self._y0))
            right_wall = Line(Point(self._x1, self._y0), Point(self._x1, self._y1))
            bottom_wall = Line(Point(self._x0, self._y1), Point(self._x1, self._y1))
            if self.has_left_wall:
                self.window.draw_line(left_wall)
            else:
                self.window.draw_line(left_wall, self.window.bg)
            if self.has_top_wall:
                self.window.draw_line(top_wall)
            else:
                self.window.draw_line(top_wall, self.window.bg)
            if self.has_right_wall:
                self.window.draw_line(right_wall)
            else:
                self.window.draw_line(right_wall, self.window.bg)
            if self.has_bottom_wall:
                self.window.draw_line(bottom_wall)
            else:
                self.window.draw_line(bottom_wall, self.window.bg)

    def draw_move(self, to_cell: Cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        line = Line(self._center, to_cell._center)
        self.window.draw_line(line, color)
