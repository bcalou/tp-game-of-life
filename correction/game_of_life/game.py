import pygame
import copy
from game_of_life.constants import CELL_SIZE, State


def update(screen: pygame.surface.Surface, state: State) -> None:
    """Draw the screen based on the current state"""
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Browse the rows and the cells to find which ones to draw
    for rowIndex, row in enumerate(state):
        for cellIndex, cell in enumerate(row):
            if cell:
                draw_cell(screen, rowIndex, cellIndex)

    # Update the screen
    pygame.display.flip()


def draw_cell(
    screen: pygame.surface.Surface,
    rowIndex: int,
    cellIndex: int
) -> None:
    """Draw a cell at the given position"""
    pygame.draw.rect(screen, (255, 255, 255), [
        cellIndex * CELL_SIZE,
        rowIndex * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE]
    )


def get_next_state(state: State) -> State:
    """Compute the next state according to the game of life's laws"""
    # Deep copy the initial state. We need to do this to keep the original
    # state reference while modifying the next state
    next_state: State = copy.deepcopy(state)

    # Browse the rows and the cells to find which ones live and die
    for rowIndex, row in enumerate(state):
        for cellIndex, cell in enumerate(row):

            # How many neighbors does this cell have?
            neighbors_count: int = \
                get_neighbors_count(state, rowIndex, cellIndex)

            # A living cell with less than 2 or more than 3 neighbors dies
            if cell and (neighbors_count < 2 or neighbors_count > 3):
                next_state[rowIndex][cellIndex] = 0

            # An empty cell with 3 neighbors live
            elif not cell and neighbors_count == 3:
                next_state[rowIndex][cellIndex] = 1

    return next_state


def get_neighbors_count(state: State, rowIndex: int, cellIndex: int) -> int:
    """Get the number of cells alive around the given one"""
    count: int = 0

    # Browse the rows and cells (exclude out of bound neighbors)
    for y in range(max(0, rowIndex - 1), min(rowIndex + 2, len(state))):
        for x in range(max(0, cellIndex - 1), min(cellIndex + 2, len(state))):

            # Check if it is not the main cell itself and if the cell is alive
            if (y != rowIndex or x != cellIndex) and state[y][x]:
                count += 1

    return count
