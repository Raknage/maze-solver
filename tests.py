import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 50
        num_rows = 150
        m1 = Maze(0, 0, num_rows, num_cols, 10, 30)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 20, 20)
        m1.break_entrance_and_exit()
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_cols = 4
        num_rows = 3
        m1 = Maze(10, 10, num_rows, num_cols, 20, 20)
        m1.break_walls_r(0, 0)
        self.assertEqual(
            m1.cells[0][1].visited,
            True,
        )
        self.assertEqual(
            m1.cells[3][1].visited,
            True,
        )
        m1.reset_cells_visited()
        self.assertEqual(
            m1.cells[0][1].visited,
            False,
        )
        self.assertEqual(
            m1.cells[3][1].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()
