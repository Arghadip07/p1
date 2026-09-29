# algorithm.py
import math
from queue import PriorityQueue
from settings import *

def h(p1, p2):
    # EUCLIDEAN DISTANCE: Best for 8-way diagonal movement grids
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        if current.color not in [ORANGE, TURQUOISE]:
            current.color = YELLOW

def run_astar(grid, start, end):
    for row in grid:
        for node in row:
            node.update_neighbors(grid)

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    
    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current != start and current != end:
            current.search_state = 'CLOSED'

        if current == end:
            reconstruct_path(came_from, end)
            return g_score[end]

        for neighbor in current.neighbors:
            # Check if movement is diagonal to apply realistic distance cost
            is_diagonal = (current.row != neighbor.row) and (current.col != neighbor.col)
            movement_cost = 1.414 if is_diagonal else 1.0
            
            temp_g_score = g_score[current] + (neighbor.get_weight() * movement_cost)

            if temp_g_score <= MAX_FUEL and temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    
                    if neighbor != end:
                        neighbor.search_state = 'OPEN'

    return -1 # Failed