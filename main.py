import numpy as np
import pygame
from settings import *
from grid import *
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Number and copy it")
run = True
clock = pygame.time.Clock()
Grid = grid(ROWS, COLS, WHITE)
model = tf.keras.models.load_model('elmodel_elgamed.model')
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
def convert_binary(pixels):
    li = pixels

    newMatrix = [[] for x in range(len(li))]

    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[j][i] == (255, 255, 255):
                newMatrix[i].append(1)
            else:
                newMatrix[i].append(0)

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_test = tf.keras.utils.normalize(x_test, axis=1)
    for row in range(28):
        for x in range(28):
            x_test[0][row][x] = newMatrix[row][x]

    return x_test[:1]

def print_predict(img):
    model = tf.keras.models.load_model('elmodel_elgamed.model')
    predictions = model.predict(img)
    print(predictions)
    t = (np.argmax(predictions))
    print("I predict this number is a:", t)


def pos_from_mouse(pos) -> (int, int):
    x, y = pos
    r = x // PIXEL_SIZE
    c = y // PIXEL_SIZE
    if r >= ROWS:
        raise IndexError
    return r, c


def draw(win):
    win.fill(BLUE)
    Grid.draw_grid(WIN)
    pygame.display.update()


while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            try:
                (rows, cols) = pos_from_mouse(pygame.mouse.get_pos())
                Grid.pixels[rows][cols] = BLACK
            except IndexError:
                pass
        if pygame.mouse.get_pressed()[2]:
            try:
                (rows, cols) = pos_from_mouse(pygame.mouse.get_pos())
                Grid.pixels[rows][cols] = WHITE
            except IndexError:
                pass
        if keys[pygame.K_SPACE]:
            print(Grid.get_img())
            run = False
            #Grid = grid(ROWS, COLS, WHITE)
        if keys[pygame.K_RETURN]:
            run = False

            img = convert_binary(Grid.pixels)/255
            plt.imshow(img[0], cmap='gray')
            plt.show()
            #print(type(img))
            print_predict(img)
            #model.evaluate(x_test,y_test)
    draw(WIN)
#img = np.array(Grid.get_img())

pygame.quit()