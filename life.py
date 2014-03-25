__author__ = 'Sotaya'
'''
Overpopulation: If a living cell is surrounded by more than three living cells it dies.
Stasis: If a living cell is surrounded by two or three living cells it survives.
Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.
'''

import pygame
import sys
from pygame.locals import *
import random


class life:
    FPS = 5
    pygame.init()
    WIDTH = 640
    HEIGHT = 480
    CELLSIZE = 10

    assert WIDTH % CELLSIZE == 0
    assert HEIGHT % CELLSIZE == 0

    CELLWIDTH = WIDTH / CELLSIZE  # number of horizontal cells
    CELLHEIGT = HEIGHT / CELLSIZE  # number of vertical cells

    BLACK = (0, 0, 0)  # line colors
    WHITE = (255, 255, 255)  # background color
    DARKGRAY = (40, 40, 40)
    GREEN = (0, 255, 0)  # color for living cells

    def __init__(self):
        pass

    #The grid method draws the grid system, vertical and horizontal lines
    def grid(self):
        for x in range(0, self.WIDTH, self.CELLSIZE):
            pygame.draw.line(DISPLAY, self.DARKGRAY, (x, 0), (x, self.HEIGHT))

        for y in range(0, self.HEIGHT, self.CELLSIZE):
            pygame.draw.line(DISPLAY, self.DARKGRAY, (0, y), (self.WIDTH, y))

    #This initializes the grid system to 0 (empty at beginning)
    def empty_grid(self):
        grid_dict = {}
        for yy in range(self.CELLHEIGT):
            for xx in range(self.CELLWIDTH):
                grid_dict[xx, yy] = 0
        return grid_dict

    #this fills in the grid with live and dead cells, 0 or 1 randomly
    def begin_grid_random(self, life_dict):
        for item in life_dict:
            life_dict[item] = random.randint(0, 1)
        return life_dict

    #After filling the grid with 0's and 1's we color each cell according
    #to if its alive or dead.
    def color_grid(self, item, life_dict):
        x = item[0]
        y = item[1]
        y = y * self.CELLSIZE
        x = x * self.CELLSIZE

        if life_dict[item] == 0:
            pygame.draw.rect(DISPLAY, self.WHITE, (x, y, self.CELLSIZE, self.CELLSIZE))

        if life_dict[item] == 1:
            pygame.draw.rect(DISPLAY, self.GREEN, (x, y, self.CELLSIZE, self.CELLSIZE))
        return None

    #With this method we go through the each cell counting its neighbors
    def get_neighbors(self, item, life_dict):
        neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                check_cell = (item[0] + x, item[1] + y)
                if self.CELLWIDTH > check_cell[0] >= 0:
                    if self.CELLHEIGT > check_cell[1] >= 0:
                        if life_dict[check_cell] == 1:
                            if x == 0 and y == 0:
                                neighbors += 0
                            else:
                                neighbors += 1
        return neighbors

    #According to the number of neighbors found around a cell, we
    #either kill the cell or bring it to life
    def tick(self, life_dict):
        new_tick = {}
        for item in life_dict:
            number_neighbors = self.get_neighbors(item, life_dict)
            if life_dict[item] == 1:
                if number_neighbors < 2:
                    new_tick[item] = 0
                elif number_neighbors > 3:
                    new_tick[item] = 0
                else:
                    new_tick[item] = 1
            elif life_dict[item] == 0:
                if number_neighbors == 3:
                    new_tick[item] = 1
                else:
                    new_tick[item] = 0
        return new_tick

    #main method of the program, it  contains the games loop and
    #necessary initializations of data.
    def main(self):
        pygame.init()
        global DISPLAY
        FPSCLOCK = pygame.time.Clock()
        DISPLAY = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Yo Bitches - Game of Life")
        DISPLAY.fill(self.WHITE)  # background color
        life_dict = self.empty_grid()
        life_dict = self.begin_grid_random(life_dict)

        for item in life_dict:
            self.color_grid(item, life_dict)

        self.grid()
        pygame.display.update()

        #game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            life_dict = self.tick(life_dict)

            for item in life_dict:
                self.color_grid(item, life_dict)

            self.grid()
            pygame.display.update()
            FPSCLOCK.tick(self.FPS)


if __name__ == '__main__':
    main = life()
    main.main()