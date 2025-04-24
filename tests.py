import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_maze_create_cells2(self):
        num_cols = 50
        num_rows = 150
        m1 = Maze(0, 0, num_rows, num_cols, 10, 30)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )


if __name__ == "__main__":
    unittest.main()
