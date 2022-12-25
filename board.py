import itertools
import random

import pygame

class Board:
    """Holds and renders the current board state
    """

    def __init__(self, initial_state=None):
        if not initial_state:
            self.state = Board.get_empty()
            self.state[50][50] = True
            self.state[50][51] = True
            self.state[50][49] = True
            self.state[51][49] = True
            self.state[49][50] = True
            print(self.get_neighbours(6, 5))
        else:
            self.state = initial_state

    def update_state(self):
        """Run every time step to update the board."""
        new_board = Board.get_empty()
        for x in range(len(self.state)):
            for y in range(len(self.state[0])):
                neighbours = self.get_neighbours(x, y)
                living_neighbours = 0
                for neighbour in neighbours:
                    if neighbour:
                        living_neighbours += 1
                if living_neighbours == 3:
                    #Reproduce
                    new_board[x][y] = True
                elif living_neighbours in (2, 3):
                    #Survive
                    new_board[x][y] = self.state[x][y]
                else:
                    #Die
                    new_board[x][y] = False
        self.state = new_board

    def get_neighbours(self, x, y):
        neighbours = []
        options = [
            (0, 1),
            (0, -1),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
        ]
        for option in options:
            try:
                x_offset = option[0]
                y_offset = option[1]
                neighbours.append(self.state[x + x_offset][y + y_offset])
            except IndexError:
                pass
        return neighbours

    def render(self, width, height, zoom):
        """
        Render the board to a surface with set dimensions.
        """
        surface = pygame.Surface((width, height))
        cell_width = zoom * width / len(self.state[0])
        for row_number, row in enumerate(self.state):
            for cell_number, cell in enumerate(row):
                if cell:
                    cell_surface = pygame.Surface((cell_width, cell_width))
                    cell_surface.fill((120, 230, 34))
                    surface.blit(cell_surface, (cell_number * cell_width, row_number * cell_width))
        return surface

    def get_empty():
        row = [False] * 200
        new = []
        for i in range(200):
            new.append(row[:])
        return new