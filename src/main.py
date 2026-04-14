import pygame
from astar import astar
from grid import create_grid

pygame.init()

size = 10
cell = 50
screen = pygame.display.set_mode((size*cell, size*cell))
pygame.display.set_caption("AI Navigation System")

grid = create_grid(size)
start = (0,0)
goal = (9,9)

path = astar(grid, start, goal)

running = True
while running:
    screen.fill((255,255,255))

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                color = (0,0,0)
            else:
                color = (200,200,200)

            pygame.draw.rect(screen, color, (j*cell, i*cell, cell, cell))
            pygame.draw.rect(screen, (50,50,50), (j*cell, i*cell, cell, cell), 1)

    for pos in path:
        pygame.draw.rect(screen, (0,255,0), (pos[1]*cell, pos[0]*cell, cell, cell))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
