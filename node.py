# node.py
import pygame
from settings import *

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = HIGHWAY
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        
        self.is_signal = False
        self.signal_timer = 0
        self.is_red = False
        self.search_state = None 

    def get_pos(self): return self.row, self.col
    
    def get_weight(self):
        if self.color == ROUGH_LANE: return 5
        if self.color == TRAFFIC: return 10
        if self.is_signal and self.is_red: return float('inf')
        return 1 

    def is_obstacle(self): return self.color == WHITE or (self.is_signal and self.is_red)
    
    def reset(self): 
        self.color = HIGHWAY
        self.is_signal = False
        self.search_state = None 
        
    def make_wall(self): self.color = WHITE
    def make_rough(self): self.color = ROUGH_LANE
    def make_traffic(self): self.color = TRAFFIC
    def make_signal(self): 
        self.is_signal = True
        self.color = SIGNAL_GREEN
        self.is_red = False

    def update_signal(self):
        if self.is_signal:
            self.signal_timer += 1
            if self.signal_timer > 60: 
                self.is_red = not self.is_red
                self.color = SIGNAL_RED if self.is_red else SIGNAL_GREEN
                self.signal_timer = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
        if self.color not in [ORANGE, TURQUOISE, YELLOW]:
            margin = max(1, self.width // 4)
            inner_w = self.width - (2 * margin)
            
            if self.search_state == 'OPEN':
                pygame.draw.rect(win, WAVE_OPEN, (self.x + margin, self.y + margin, inner_w, inner_w))
            elif self.search_state == 'CLOSED':
                pygame.draw.rect(win, WAVE_CLOSED, (self.x + margin, self.y + margin, inner_w, inner_w))

    def update_neighbors(self, grid):
        self.neighbors = []
        # ADDED 8-WAY MOVEMENT (Straight + Diagonals)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),   # Up, Down, Left, Right
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonals
        ]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < self.total_rows and 0 <= c < self.total_rows:
                if not grid[r][c].is_obstacle():
                    self.neighbors.append(grid[r][c])

    def __lt__(self, other): return False