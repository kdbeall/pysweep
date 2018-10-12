"""
    Tests for models.py,
    run with python3 -m unittest -v test.py
"""

import unittest
from models import Square, Board
from game import Game, GameState


class TestSquare(unittest.TestCase):

    def test_square__init__(self):
        """ Tests the Square __init__. """
        board = Board(3, 3)
        square = Square(board, 0 ,0, False)
        self.assertFalse(square.mine)
        self.assertFalse(square.clicked)
        square = Square(board, 0, 0, True)
        self.assertTrue(square.mine)
        self.assertFalse(square.clicked)

    def test_square_neighbors(self):
        """ Tests getting a squares neighbors. """
        board = Board(2, 2)
        square = Square(board, 0 ,0, False)
        self.assertEqual(3, len(square.neighbors()))

class TestBoard(unittest.TestCase):

    def test_board__init__(self):
        board = Board(3, 3)
        self.assertEqual(3, board.cols)
        self.assertEqual(3, board.rows)
        board.print_board_wrapper(board.print_board_hook)

    def test_board__init__percentage(self):
        """ Tests mine percentages are calculated correctly. """
        rows = 5
        cols = 5
        max_mines = (cols-1)*(rows-1)
        mines_percent = 100 * max_mines / (rows*cols)
        self.assertEqual(64, mines_percent)



if __name__ == '__main__':
    unittest.main()
