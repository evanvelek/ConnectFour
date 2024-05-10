from graphics import board_generator
import pygame

def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    empty_grid = [[0 for _ in range(7)] for _ in range(6)]
    board_generator(empty_grid, surface)