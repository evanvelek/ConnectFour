# player_moves.py

def game_won(board:list[list[int]]) -> int:
    """Checks if the connect 4 game has been won, returning the player number of the
    winning, or 0 if there is no winner"""
    # Vertical Win
    for row in range(3): # Leave 3
        for col in range(7):
            if board[row][col] == board[row +1][col] == board[row+2][col] == board[row+3]:
                return board[row][col] # Want to return the player

    # Horizontal Win
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return board[row][col]

    # Up-right diagonal
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]

    # Up-left diagonal
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row + 1][col - 1] == board[row + 2][col-2] == board[row + 3][col-3]:
                return board[row][col]

    return 0



def player_move(board:list[list[int]], col: int) -> bool:
     """Changes board in accordance with the move, returns false if the move
     is not possible, or true if it worked, but the function itself modifies
     the 2D array"""
     for row in range(len(board)):
         if board[row][col] == 0:
             board[row][col] = 1
             return True
     return False

def computer_move(board:list[list[int]]) -> bool:
    """Computer thinks of a move to play, and changes the board accordingly"""
    pass



def _is_winning(board:list[list[int]], col: int, player:int):
    """Checks if dropping a piece in a particular column on a board would win the game,
    if player = 1 then for the human and if player = 2 then for the computer"""
    pass

__all__ = [
    "game_won",
    "player_move"
    "computer_move"
]

