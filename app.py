import pygame
from Node import Node
from global_var import Win, WIDTH
from colors import *
from a_star import a_star, heuristic_func
from tkinter import *
from tkinter import messagebox


Tk().wm_withdraw() #to hide the main window


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
    rows = 40

    #last: try to create a dynamic grid
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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    grid = []
                    start_position = None
                    end_position = None 
                    Started = False
                    grid = create_grid(rows, width)
                    draw(win, grid, rows, width)

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start_position and end_position:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)       
                    
                    
                    solution = a_star(lambda: draw(win, grid, rows, width), grid, start_position, end_position) #lambda is an anonymous funtion
                    #-----------------------------------------
                    # x = def func():
                    #        print("hello")
                    # x()
                    #-----------------------------------------
                    # this can be summarized using lambda:
                    # x = lambda: print("hello")
                    
                    #if button 2 selected:
                        #bfs
                    # if button 3 selected:
                        #diasktra
                    # if button 4 selected:
                        #greedy
    
                    if solution == False:
                        messagebox.showinfo(title='Path Doesnt Exist', message="No Path Found")

                if not start_position and (event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_d or event.key == pygame.K_g):
                        messagebox.showerror(title='Start-Position-404', message='Start Position not selected')
                if not end_position and (event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_d or event.key == pygame.K_g):
                        messagebox.showerror(title='End-Position-404', message='End Position not selected')
    pygame.quit()

main(Win, WIDTH)