from window import Window, Point, Line, Cell
from maze import Maze


def main():
    start = (100, 100)
    cell_size = (20, 20)
    win = Window(800, 600)
    win.redraw()
    max_size = count_max_size(win, *start, *cell_size)
    Maze(*start, *max_size, *cell_size, win)
    win.wait_for_close()


def count_max_size(
    win: Window, x1: int, y1: int, cell_size_x: int, cell_size_y: int
) -> tuple[int]:
    width = win.canvas.winfo_width()
    height = win.canvas.winfo_height()
    x: int = (width - x1 * 2) // cell_size_x
    y: int = (height - y1 * 2) // cell_size_y
    return (y, x)


main()
