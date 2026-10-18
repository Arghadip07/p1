# main.py
import pygame
import random
from settings import *
from node import Node
from algorithm import run_astar

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Smart City Pathfinding - 8-Way Instant GPS")

def draw_grid(win, rows, width, grid):
    win.fill(BLACK)
    for row in grid:
        for node in row:
            node.draw(win)
    
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
    pygame.display.update()

def generate_demo_city(grid, rows):
    for row in grid:
        for node in row: node.reset()
            
    start = grid[5][5]
    end = grid[rows-6][rows-6]
    start.color = ORANGE
    end.color = TURQUOISE
    
    for row in range(rows):
        for col in range(rows):
            node = grid[row][col]
            if node == start or node == end: continue
            
            chance = random.random()
            if chance < 0.12: 
                node.make_wall()      # 12% impassable buildings (keeps it navigable)
            elif chance < 0.35: 
                node.make_rough()     # 23% rough roads (forces the path to curve)
            elif chance < 0.45: 
                node.make_traffic()   # 10% heavy traffic (forces major detours)
            elif chance < 0.48: 
                node.make_signal()    # 3% traffic lights
                
    return start, end

def main():
    #comment
    gap = WIDTH // ROWS
    grid = [[Node(i, j, gap, ROWS) for j in range(ROWS)] for i in range(ROWS)]
    start = end = None
    run = True

    while run:
        for row in grid:
            for node in row:
                node.update_signal()

        draw_grid(WIN, ROWS, WIDTH, grid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    start, end = generate_demo_city(grid, ROWS)
                
                if event.key == pygame.K_SPACE and start and end:
                    cost = run_astar(grid, start, end)
                    if cost != -1:
                        print(f"Path found instantly! Fuel Cost: {cost:.2f}")
                    else:
                        print("Route failed: Out of fuel or completely blocked.")
                
                if event.key == pygame.K_c:
                    start = end = None
                    grid = [[Node(i, j, gap, ROWS) for j in range(ROWS)] for i in range(ROWS)]

    pygame.quit()

if __name__ == "__main__":
    main()