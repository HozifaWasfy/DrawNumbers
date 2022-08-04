from settings import *
import pygame
import numpy as np


class grid:
    def __init__(self, height, width, color):
        self.pixels = []
        for i in range(height):
            self.pixels.append([])
            for _ in range(width):
                self.pixels[i].append(color)
        self.img = []



    def get_img(self):
        for i in range(len(self.pixels)):
            self.img.append([])
            for j in range(len(self.pixels[i])):
                if self.pixels[i][j] == (255, 255, 255):
                    self.img[i].append(0)
                else:
                    self.img[i].append(255)
        return self.img

    def draw_grid(self, win):
        for i, row in enumerate(self.pixels):
            for j, pixel in enumerate(row):
                pygame.draw.rect(win, pixel, (i*PIXEL_SIZE, j*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


