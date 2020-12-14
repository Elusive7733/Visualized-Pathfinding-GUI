import pygame
import math
from queue import PriorityQueue


Width = 800
Win = pygame.display.set_mode((Width, Width))
pygame.display.set_caption("A* Path Finding Algorithm")


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
grey = (128, 128, 128)
torquoise = (64, 224, 208)
orange = (255, 165, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows


    #Receieving color from our nodes
    def get_position(self):
	    return self.row, self.col

    def visited(self):
        return self.color == red
    
    def to_visit(self):
        return self.color == green

    def barrier(self):
        return self.color == black

    def start_node(self):
        return self.color == orange

    def end_node(self):
        return self.color == torquoise

    def reset(self):
        return.color == white

    #Assigning color for out nodes
    def create_visited(self):
        return self.color = red
    
    def create_to_visit(self):
        return self.color = green

    def create_barrier(self):
        return self.color = black

    def create_start_node(self):
        return self.color = orange

    def create_end_node(self):
        return self.color = torquoise
    
    def create_path(self):
        return self.color = purple

    def draw(self, Win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(sel, grid):
        pass

    #lesser than funtion
    def __lt__(self, other):
        return False
    
    def heuristic_func(cordinate_1, cordinate_2):
        #manhattan distance (moving in straight lines)
        x1 = p1
        y1 = p1
        x2 = p2
        y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def create_grid(rows, width):
        grid = []
        gap = width // rows #integer division