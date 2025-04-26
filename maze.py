import time
import random
from window import Window, Point
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        random.seed(seed)
        self._create_cells()
        if self._win:
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()

    def _create_cells(self):
        for x in range(self._num_cols):
            self._cells.append([])
            for y in range(self._num_rows):
                self._cells[x].append(Cell(self._win))

        for y in range(self._num_rows):
            for x in range(self._num_cols):
                self._draw_cell(x, y)

    def _draw_cell(self, x: int, y: int):
        p1 = Point(self._x1 + self._cell_size_x * x, self._y1 + self._cell_size_y * y)
        p2 = Point(
            self._x1 + self._cell_size_x + self._cell_size_x * x,
            self._y1 + self._cell_size_y + self._cell_size_y * y,
        )
        cell: Cell = self._cells[x][y]
        cell.draw(p1, p2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, x: int, y: int):
        current_cell = self._cells[x][y]
        current_cell.visited = True
        while True:
            to_be_visited: list[tuple[int]] = []
            for i in range(x - 1, x + 2):
                if i < 0:
                    continue
                if i > self._num_cols - 1:
                    continue
                if i == x:
                    continue
                if self._cells[i][y].visited == True:
                    continue
                else:
                    to_be_visited.append((i, y))
            for j in range(y - 1, y + 2):
                if j < 0:
                    continue
                if j > self._num_rows - 1:
                    continue
                if j == y:
                    continue
                if self._cells[x][j].visited == True:
                    continue
                else:
                    to_be_visited.append((x, j))
            if len(to_be_visited) == 0:
                self._draw_cell(x, y)
                time.sleep(0.05)
                return
            else:
                destination: tuple[int] = to_be_visited[
                    random.randint(0, len(to_be_visited) - 1)
                ]
                to_be_visited.clear()
                next_cell = self._cells[destination[0]][destination[1]]
                if destination[0] > x:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                elif destination[0] < x:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif destination[1] > y:
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                elif destination[1] < y:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                self._break_walls_r(destination[0], destination[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
