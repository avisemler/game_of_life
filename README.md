# Game of Life
Conway's game of life, implementing using Python and PyGame.

![Screenshot](https://avisemler.github.io/files/screenshot.jpg)

## Controls
 - `a`: zoom out
 - `s`:  zoom in
 - Arrow keys: move view

To configure the starting position of the board, see `board.py`.

## Structure

`main.py` handles the instantiation of classes and the event loop (including handling user input).

`board.py` implements the class `Board` which abstracts the logic of storing and updating the state of the simulation.
