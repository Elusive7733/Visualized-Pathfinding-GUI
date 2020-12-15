import pygame
import math
from colors import *
from a_star import heuristic_func

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows


    #Receieving color from our nodes
    def get_position(self):
	    return self.row, self.col

    def check_visited(self):
        return self.color == aqua
    
    def to_visit(self):
        return self.color == spring_green

    def check_barrier(self):
        return self.color == black

    def check_start_node(self):
        return self.color == orange

    def check_end_node(self):
        return self.color == gold

    #Assigning color for out nodes
    def create_visited(self, end):
        h_score = heuristic_func(self.get_position(), end.get_position())
        self.color = (0, 255 - h_score*2, 230 - h_score*2)
    
    def reset(self):
        self.color = white

    def create_to_visit(self):
        self.color = spring_green

    def create_barrier(self):
        self.color = black

    def create_start_node(self):
        self.color = chocolate

    def create_end_node(self):
        self.color = gold
    
    def create_path(self):
        self.color = crimson

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < (self.total_rows - 1): #checking if down < total number of rows
            if not grid[self.row + 1][self.col].check_barrier(): #checking if the "down" node is not a barrier
                self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0: #checking if up exists (not at the top (row = 0))
            if not grid[self.row - 1][self.col].check_barrier(): #checking if the "up" node is not a barrier
                self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < (self.total_rows - 1): #checking if left < total number of columns (used total_rows here because it's a square)
            if not grid[self.row][self.col + 1].check_barrier(): #checking if the "left" node is not a barrier
                self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0: #checking if right exists (not at the right_most (column = 0))
            if not grid[self.row][self.col - 1].check_barrier(): #checking if the "right" node is not a barrier
                self.neighbours.append(grid[self.row][self.col - 1])

    #lesser than funtion
    def __lt__(self, other):
        return False
    
    def display_key(self):
        pass
    
    def display_algorithms(self):
        pass