import unittest
from unittest.mock import patch
from gameboard import Board, Cell
from play import get_coordinates

class TestGame(unittest.TestCase):
    @patch('builtins.input', return_value='0 1')

    def test_get_coordinates_success(self, mock_input):
        result_row, result_column = get_coordinates()
        self.assertEqual(result_row, 0)
        self.assertEqual(result_column, 1)

    def test_board_init(self):
        board = Board()
        self.assertEqual(board.size, 10)

    def test_cell_init(self):
        cell = Cell()
        self.assertEqual(cell.flagged, False)

    def test_reveal(self):
        board = Board()
        init_unrevealed = board.unrevealed
        board.board[0][0].reveal(board)
        self.assertEqual(board.unrevealed, init_unrevealed - 1)
        self.assertEqual(board.board[0][0].revealed, True)

    def test_flag_on(self):
        cell = Cell()
        cell.toggle_flag()
        self.assertEqual(cell.flagged, True)

    def test_flag_off(self):
        cell = Cell()
        cell.flagged = not cell.flagged
        cell.toggle_flag()
        self.assertEqual(cell.flagged, False)

    def test_add_number(self):
        cell = Cell()
        cell.add_number()
        self.assertEqual(cell.number, 1)

    


    



if __name__ == "__main__":
    unittest.main()