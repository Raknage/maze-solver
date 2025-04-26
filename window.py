from __future__ import annotations
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int, bg: str = "slategray"):
        self.bg = bg
        self._width = width
        self._height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self._close)
        self.__canvas = Canvas(
            self.__root, width=width, height=height, background=self.bg
        )
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def _close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color="black"):
        line._draw(self.__canvas, fill_color)

    def count_max_size(
        self, x1: int, y1: int, cell_size_x: int, cell_size_y: int
    ) -> tuple[int]:
        x: int = (self._width - x1 * 2) // cell_size_x
        y: int = (self._height - y1 * 2) // cell_size_y
        return (y, x)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def _draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=2,
        )
