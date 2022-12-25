"""
A pygame implementation of Conway's Game of Life.
"""

import sys
import time

import pygame

from pygame.locals import *

from board import Board

class App:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((700, 700))

        self.board = Board()

        self.start_time = time.time()
        self.zoom = 1
        self.x_view = 0
        self.y_view = 0

    def frame(self):
        """
        Perform one frame.
        """
        self.handle_events()
        if time.time() - self.start_time > 0.0001:
            self.board.update_state()
            self.start_time = time.time()
        self.display.blit(self.board.render(700, 700, self.zoom), (self.x_view, self.y_view))
        pygame.display.update()

    def handle_events(self):
        move_step = 15
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    self.zoom -= 0.05
                if event.key == K_s:
                    self.zoom += 0.05
                if event.key == K_UP:
                    self.y_view += move_step
                if event.key == K_DOWN:
                    self.y_view -= move_step
                if event.key == K_LEFT:
                    self.x_view += move_step
                if event.key == K_RIGHT:
                    self.x_view -= move_step

if __name__ == "__main__":
    app = App()
    while True:
        app.frame()