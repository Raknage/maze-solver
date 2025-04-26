from window import Window, Cell, Point
import time
import random


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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells: list[list[Cell]] = []
        random.seed(seed)
        self.create_cells()
        if self.win:
            self.break_entrance_and_exit()
            self.break_walls_r(0, 0)
            self.reset_cells_visited()

    def create_cells(self):
        for x in range(self.num_cols):
            self.cells.append([])
            for y in range(self.num_rows):
                self.cells[x].append(Cell(self.win))

        for y in range(self.num_rows):
            for x in range(self.num_cols):
                self.draw_cell(x, y)

    def draw_cell(self, x: int, y: int):
        p1 = Point(self.x1 + self.cell_size_x * x, self.y1 + self.cell_size_y * y)
        p2 = Point(
            self.x1 + self.cell_size_x + self.cell_size_x * x,
            self.y1 + self.cell_size_y + self.cell_size_y * y,
        )
        cell: Cell = self.cells[x][y]
        cell.draw(p1, p2)
        self.animate()

    def animate(self):
        if self.win:
            self.win.redraw()

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[-1][-1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, x: int, y: int):
        current_cell = self.cells[x][y]
        current_cell.visited = True
        while True:
            to_be_visited: list[tuple[int]] = []
            for i in range(x - 1, x + 2):
                if i < 0:
                    continue
                if i > self.num_cols - 1:
                    continue
                if i == x:
                    continue
                if self.cells[i][y].visited == True:
                    continue
                else:
                    to_be_visited.append((i, y))
            for j in range(y - 1, y + 2):
                if j < 0:
                    continue
                if j > self.num_rows - 1:
                    continue
                if j == y:
                    continue
                if self.cells[x][j].visited == True:
                    continue
                else:
                    to_be_visited.append((x, j))
            if len(to_be_visited) == 0:
                self.draw_cell(x, y)
                time.sleep(0.05)
                return
            else:
                destination: tuple[int] = to_be_visited[
                    random.randint(0, len(to_be_visited) - 1)
                ]
                to_be_visited.clear()
                next_cell = self.cells[destination[0]][destination[1]]
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
                self.break_walls_r(destination[0], destination[1])

    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
