import unittest
from unittest.mock import Mock
from maze import Maze

mock_window = Mock()
mock_window.draw_line = Mock()

class Tests(unittest.TestCase):
    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        print(f"Creating {num_rows}x{num_cols} maze")
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window=mock_window)
        self.assertEqual(len(m1.cells), num_rows)
        self.assertEqual(len(m1.cells[0]), num_cols)
        print(f"Created {num_rows}x{num_cols} maze")
        
if __name__ == '__main__':
    unittest.main()