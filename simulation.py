import numpy as np

from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size) -> None:
        self.grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.run = False


    def draw(self, window):
        self.grid.draw(window)


    """
    Rule 1: If a live cell has less than 2 neighbors alive, it will die.
    Rule 2: If a live cell has 2 or 3 nighbors alive, it will continue to stay alive.
    Rule 3: If a live cell has more than 3 neighbors alive, it will die.
    Rule 4: If a dead cell has exactly 3 neighbors alive, it will become alive.
    """
    

    def count_neighbors(self, row, col):
        live_neighbors = 0

        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for offset in neighbor_offsets:
            new_row = (row + offset[0]) % self.rows
            new_col = (col + offset[1]) % self.cols

            if self.grid.board[new_row][new_col] in [1, 3]:
                live_neighbors += 1

        return live_neighbors
    

    """
    Reference table for in-place changes:

    Original | New | State
        0    |  0  |    0
        1    |  0  |    1
        0    |  1  |    2
        1    |  1  |    3
    """

    
    def update_state(self):
        if self.is_running():  
            for row in range(self.rows):
                for col in range(self.cols):

                    live_neighbors = self.count_neighbors(row, col)

                    if self.grid.board[row][col]:               # if originally 1, live if neighbors alive = 2,3 else die
                        if live_neighbors in [2, 3]:
                            self.grid.board[row][col] = 3
                    else:                                       # if originally 0, live if neighbors alive = 3 else die
                        if live_neighbors == 3:
                            self.grid.board[row][col] = 2

            for row in range(self.rows):
                for col in range(self.cols):

                    if self.grid.board[row][col] == 1:
                        self.grid.board[row][col] = 0
                    elif self.grid.board[row][col] in [2, 3]:
                        self.grid.board[row][col] = 1


    def is_running(self):
        return self.run
    
    def start(self):
        self.run = True

    def stop(self):
        self.run = False

    def clear(self):
        if not self.is_running():
            self.grid.clear()

    def create_random_state(self):
        if not self.is_running():
            self.grid.board = np.random.randint(0, 2, size=(self.rows, self.cols), dtype=np.uint8)

    def toggle_cell(self, row, col):
        if not self.is_running():
            self.grid.toggle(row, col)