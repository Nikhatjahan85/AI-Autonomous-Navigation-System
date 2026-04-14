import numpy as np

def create_grid(size):
    grid = np.zeros((size, size))
    grid[3:7, 5] = 1
    grid[6, 2:6] = 1
    return grid