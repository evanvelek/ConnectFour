# player_moves.py
from random import choice
def game_won(board:list[list[int]]) -> int:
    """Checks if the connect 4 game has been won, returning the player number of the
    winning, or 0 if there is no winner. Returning -1 means a tie game"""
    # Vertical Win
    for row in range(3): # Leave 3
        for col in range(7):
            if board[row][col] == board[row +1][col] == board[row+2][col] == board[row+3][col] != 0:
                return board[row][col] # Want to return the player

    # Horizontal Win
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != 0:
                return board[row][col]

    # Up-right diagonal
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != 0:
                return board[row][col]

    # Up-left diagonal
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row + 1][col - 1] == board[row + 2][col-2] == board[row + 3][col-3] != 0:
                return board[row][col]

    # Non-tie checker
    for col in range(7):
        if board[0][col] == 0:
            return 0 # Only goes through to end of for loop if all the spaces are filled

    # Must be a tie if it gets here
    return -1



def player_move(board:list[list[int]], col: int) -> bool:
     """Changes board in accordance with the move, returns false if the move
     is not possible, or true if it worked, but the function itself modifies
     the 2D array"""
     for row in range(len(board) - 1, -1, -1):
         if board[row][col] == 0:
             board[row][col] = 1
             return True
     return False

def computer_move(board:list[list[int]]):
    """Computer thinks of a move to play, and changes the board accordingly"""
    # First -- If there's a winning move, play it
    for col in range(7):
        if _is_winning(board, col, 2):
            _drop_piece(board, col, 2)
            return

    # Next -- Block and immediately winning moves
    for col in range(7):
        if _is_winning(board, col, 1):
            _drop_piece(board, col, 2)
            return

    # Now is the interesting part

    # Look for spaces that give 2 winnable tiles
    temp = _find_two_winnable_tile(board, 2)
    if temp >= 0:
        _drop_piece(board, temp, 2)
        return

    # Look for spaces that give player 2 winnable tiles
    temp = _find_two_winnable_tile(board, 1)
    if temp >= 0:
        _drop_piece(board, temp, 2)
        return


    # Just pick a random column
    _drop_piece(board, choice(_get_valid_moves(board)), 2)
    return

def _find_two_winnable_tile(board: list[list[int]], player:int) -> int:
    """Finds a tiles that gives the given player 2 ways to win the next
    turn. Returns -1 if this is not possible, otherwise it returns the column"""
    for col in range(7):
        temp_board = [list(row) for row in board]  # deep copy as to not change the original board
        _drop_piece(temp_board, col, player)
        count = 0
        for temp_col in range(7):
            if _is_winning(temp_board, temp_col, player):
                count += 1
        if count >= 2:
            return col
    return -1

def _is_valid_move(board, col) -> bool:
    return board[0][col] == 0

def _get_valid_moves(board) -> list[int]:
    ret = []
    for col in range(7):
        if _is_valid_move(board, col):
            ret.append(col)
    return ret

def _drop_piece(board: list[list[int]], col: int, player: int):
    for row in range(len(board) -1, -1, -1): # Need to start at the bottom
        if board[row][col] == 0:
            board[row][col] = player
            break

def _is_winning(board:list[list[int]], col: int, player:int) -> int:
    """Checks if dropping a piece in a particular column on a board would win the game,
    if player = 1 then for the human and if player = 2 then for the computer"""
    deep_copy = []
    for row in board:
        deep_copy.append(list(row))
    _drop_piece(deep_copy, col, player)
    return game_won(deep_copy)

__all__ = [
    "game_won",
    "player_move",
    "computer_move"
]

