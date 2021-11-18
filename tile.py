import pygame

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE

    def get_position(self):
        return self.row, self.col

    def resurrect(self):
        self.color = BLACK

    def unalive(self):
        self.color = WHITE

    def is_alive(self):
        return self.color == BLACK

    def is_dead(self):
        return self.color == WHITE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def reset_neighbors(self):
        self.neighbors = []

    def get_neighbors(self, grid):
        # bottom left
        if self.row < self.total_rows - 1 and self.col != 0 and grid[self.row + 1][self.col - 1].is_alive():
            self.neighbors.append(grid[self.row + 1][self.col - 1])
        # bottom
        if self.row < self.total_rows - 1 and grid[self.row + 1][self.col].is_alive():
            self.neighbors.append(grid[self.row + 1][self.col])
        # bottom right
        if self.row < self.total_rows - 1 and self.col < self.total_rows - 1 and grid[self.row + 1][self.col + 1].is_alive():
            self.neighbors.append(grid[self.row + 1][self.col + 1])
        # right
        if self.col < self.total_rows - 1 and grid[self.row][self.col + 1].is_alive():
            self.neighbors.append(grid[self.row][self.col + 1])
        # top right
        if self.row != 0 and self.col + 1 < self.total_rows - 1 and grid[self.row - 1][self.col + 1].is_alive():
            self.neighbors.append(grid[self.row - 1][self.col + 1])
        # top
        if self.row != 0 and grid[self.row - 1][self.col].is_alive():
            self.neighbors.append(grid[self.row - 1][self.col])
        # top left
        if self.row != 0 and self.col != 0 and grid[self.row - 1][self.col - 1].is_alive():
            self.neighbors.append(grid[self.row - 1][self.col - 1])
        # left
        if self.col != 0 and grid[self.row][self.col - 1].is_alive():
            self.neighbors.append(grid[self.row][self.col - 1])
