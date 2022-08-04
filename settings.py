import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (44, 111, 180)

FPS = 60

ROWS, COLS = 28, 28
WIDTH = HEIGHT = 392

PIXEL_SIZE = HEIGHT // COLS


def font_size(size):
    return pygame.font.SysFont('comics ans', size)