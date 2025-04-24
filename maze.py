from window import Window, Cell, Point
import time


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells: list[list[Cell]] = []
        self.create_cells()

    def create_cells(self):
        for y in range(self.num_rows):
            self.cells.append([])
            for x in range(self.num_cols):
                self.cells[y].append(Cell(self.win))

        for y in range(self.num_rows):
            for x in range(self.num_cols):
                self.draw_cell(x, y)

    def draw_cell(self, x: int, y: int):
        p1 = Point(self.x1 + self.cell_size_x * x, self.y1 + self.cell_size_y * y)
        p2 = Point(
            self.x1 + self.cell_size_x + self.cell_size_x * x,
            self.y1 + self.cell_size_y + self.cell_size_y * y,
        )
        cell: Cell = self.cells[y][x]
        cell.draw(p1, p2)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.01)


