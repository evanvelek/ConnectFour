import gameplay.player_moves
from gameplay.player_moves import *
import unittest

class TestGameplay(unittest.TestCase):
    def setUp(self):
        self.empty_board = [[0 for _ in range(7)] for _ in range(6)]
    def test_no_winner(self):
        self.assertEqual(game_won(self.empty_board), 0)

    def test_horizontal(self):
        hori_win = self.empty_board
        for col in range(4):
            hori_win[0][col] = 1
        self.assertEqual(1, game_won(hori_win), ) # Tests top left and player 1

        hori_win[0][2] = 0
        for col in range(3, 7):
            hori_win[5][col] = 2
        self.assertEqual(2, game_won(hori_win)) # Tests bottom right and player 2

    def test_vertical(self):
        vert_win = self.empty_board
        for row in range(4):
            vert_win[row][0] = 1
        self.assertEqual(1, game_won(vert_win))

        vert_win[0][0] = 0
        for row in range(2,6):
            vert_win[row][6] = 2
        self.assertEqual(2, game_won(vert_win))

    def test_diagonal(self):
        diag_win = self.empty_board
        for rowcol in range(4):
            diag_win[rowcol][rowcol] = 1
        self.assertEqual(1, game_won(diag_win))

        diag_win[0][0] = 0
        for row in range(5, 1, -1):
            for col in range(3, 7):
                diag_win[row][col] = 2
        self.assertEqual(2, game_won(diag_win))


