# board_generator.py

# Contains functions related to board generation visually

import pygame
import gameplay.player_moves as moves

class InvalidBoardError(Exception):
    pass


def generate_board(board_state:list[list[int]], surface: pygame.display):
    """Makes the game board with colored circles or white circles depending
    on the board position. Board_state should be a 2D list with the values 0 (no tile),
    1 (player 1), and 2 (player 2). Any other values may have unintended results."""
    width = surface.get_width()
    height = surface.get_height()

    # Want a boarder -- ~10% on every side

    circ_rad = (width * .8) / 19

    rec = pygame.Rect(width * .1, height * .1,
                      width * .8, height * .8 - (circ_rad * 2.5))
    # Need to subtract because connect 4 boards aren't square
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
            pygame.draw.circle(surface, pygame.Color(8, 18, 40),
                               ((2 + col * 2.5) * circ_rad + width * .1,
                                (2 + row * 2.5) * circ_rad + height * .1),
                               circ_rad, width = 2)
            pygame.draw.circle(surface, color,
                               ((2 + col * 2.5) * circ_rad + width * .1,
                                (2 + row * 2.5) * circ_rad + height * .1),
                               circ_rad - 2)

    pygame.display.flip()
def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    board = [[0 for _ in range(7)] for _ in range(6)]
    generate_board(board, surface)
    clock = pygame.time.Clock()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                y_pos = event.pos[1]
                if (surface.get_height() * .1) < y_pos < (surface.get_height() * .9):
                    if (surface.get_width() * .1) < x_pos < (surface.get_width() * .9):
                        circ_rad = (surface.get_width() * .8) / 19
                        base_x_pos = x_pos - surface.get_width() * .1 - circ_rad
                        pos = base_x_pos // (2.5 * circ_rad)
                        moves.player_move(board, int(pos))
                        generate_board(board, surface)
                        if (moves.game_won(board)):
                            print("PLAYER 1 WON")
                        clock.tick(100)
                        moves.computer_move(board)
                        clock.tick(1)
                        generate_board(board, surface)
                        if (moves.game_won(board)):
                            print("PLAYER 2 WON")





    pygame.quit()
    exit()

__all__ = [
    "main"
]



