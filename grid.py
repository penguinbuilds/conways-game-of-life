import numpy as np
import pygame

class Grid:
    def __init__(self, width, height, cell_size) -> None:
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        self.board = np.random.randint(0, 1, size=(self.rows, self.cols), dtype=np.uint8)
    
    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                color = (0, 200, 0) if self.board[row][col] else (50, 50, 50)
                pygame.draw.rect(window, color, (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
                
    def clear(self):
        self.board[:, :] = 0

    def toggle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.board[row][col] = not self.board[row][col]