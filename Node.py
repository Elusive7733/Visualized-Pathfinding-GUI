import pygame
import math
from colors import *

class Node:
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
        return self.color == aqua
    
    def to_visit(self):
        return self.color == spring_green

    def barrier(self):
        return self.color == black

    def start_node(self):
        return self.color == orange

    def end_node(self):
        return self.color == gold

    #Assigning color for out nodes
    def create_visited(self):
        self.color = aqua
    
    def reset(self):
        self.color = white

    def create_to_visit(self):
        self.color = spring_green

    def create_barrier(self):
        self.color = black

    def create_start_node(self):
        self.color = orange

    def create_end_node(self):
        self.color = gold
    
    def create_path(self):
        self.color = crimson

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(sel, grid):
        pass

    #lesser than funtion
    def __lt__(self, other):
        return False
    
    def display_key(self):
        pass
    
    def display_algorithms(self):
        pass