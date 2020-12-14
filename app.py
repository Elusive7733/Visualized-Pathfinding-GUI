import pygame
import math
from queue import PriorityQueue
from Node import Node
from global_var import Win, WIDTH
from colors import * 

def heuristic_func(cordinate_1, cordinate_2):
    #manhattan distance (moving in straight lines)
    x1 = p1
    y1 = p1
    x2 = p2
    y2 = p2
    #adding the difference between the x and y cordinates of the grid
    return abs(x1 - x2) + abs(y1 - y2)

def create_grid(rows, width):
    grid = []
    gap = width // rows #integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows): #used rows here because A square grid is required
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def draw_gridlines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(white)
    
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_gridlines(win, rows, width)
    pygame.display.update()

def mouse_clicked_position(position, rows, width):
    gap = width // rows
    x = position[1]
    y = position[0]

    col = x // gap
    row = y // gap

    return row, col

def main(win, width):
    rows = 80
    grid = create_grid(rows, width)

    start_position = None
    end_position = None

    run = True
    Started = False
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if Started:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(position, rows, width)
                node = grid[row][col]
                if not start_position and node != end_position:
                    start_position = node
                    start_position.create_start_node()
                elif not end_position and node != start_position:
                    end_position = node
                    end_position.create_end_node()
                elif node != start_position and node != end_position:
                    node.create_barrier()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(position, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start_position:
                    start_position = None
                if node == end_position:
                    end_position = None
    
    pygame.quit()


main(Win, WIDTH)