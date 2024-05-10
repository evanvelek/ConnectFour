# board_generator.py

# Contains functions related to board generation visually

import pygame

class InvalidBoardError(Exception):
    pass


def generate_board(board_state:list[list[int]], surface: pygame.display):
    """Makes the game board with colored circles or white circles depending
    on the board position. Board_state should be a 2D list with the values 0 (no tile),
    1 (player 1), and 2 (player 2). Any other values may have unintended results."""
    width = surface.get_width()
    height = surface.get_height()

    # Want a boarder -- ~10% on every side


    rec = pygame.Rect(left = (width * .1),top = (height * .1),
                      width = (width * .8), height = (height * .8))
    pygame.draw.rect(surface, pygame.Color(43, 101, 201), rec) # Entire board
    for row in range(len(board_state)):
        for col in range(len(board_state[row])):
            if board_state[row][col] == 0:
                color = pygame.Color(239, 226, 216) # No player -- White
            elif board_state[row][col] == 1:
                color = pygame.Color(234, 58, 52) # Player 1 -- Red
            elif board_state[row][col] == 2:
                color = pygame.Color(249, 224, 79) # Player 2 -- Yellow
            else:
                raise InvalidBoardError("There was an unexpected value in "
                                        f"the board state: {board_state[row][col]}")
            circ_rad = (width * .8) / 21
            pygame.draw.circle(surface, pygame.Color(8, 18, 40),
                               ((2 + col * 2.5) * circ_rad, (2 + row * 2.5) * circ_rad),
                               circ_rad, width = 2)
            pygame.draw.circle(surface, color,
                               ((2 + col * 2.5) * circ_rad, (2 + row * 2.5) * circ_rad),
                               circ_rad - 2)

    pygame.display.flip()


__all__ = [
    "generate_board"
]



