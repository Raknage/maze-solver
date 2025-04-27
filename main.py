from window import Window
from maze import Maze


def main():
    start = (120, 100)
    cell_size = (20, 20)
    win = Window(800, 600)
    max_size = win.count_max_size(*start, *cell_size)
    maze = Maze(*start, *max_size, *cell_size, win)
    maze.solve()
    win.wait_for_close()


main()
