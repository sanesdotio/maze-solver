import random
import time
from cell import Cell
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        
        if seed:
            random.seed(seed)
        
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        
    def create_cells(self):
        for i in range(self.num_rows):
            row_cells = []
            for j in range(self.num_cols):
                row_cells.append(Cell(self.window))
            self.cells.append(row_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)
    
    def draw_cell(self, row, col):
        cell = self.cells[row][col]
        x = self.x1 + col * self.cell_size_x
        y = self.y1 + row * self.cell_size_y
        cell.draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self.animate()
        
    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.draw_cell(self.num_rows-1, self.num_cols-1)
    
    def break_walls_r(self, row, col):
        self.cells[row][col].visited = True
        while True:
            to_visit = []
            if row > 0 and not self.cells[row-1][col].visited:
                to_visit.append((row-1, col))
            if row < self.num_rows - 1 and not self.cells[row+1][col].visited:
                to_visit.append((row+1, col))
            if col > 0 and not self.cells[row][col-1].visited:
                to_visit.append((row, col-1))
            if col < self.num_cols - 1 and not self.cells[row][col+1].visited:
                to_visit.append((row, col+1))
            
            if len(to_visit) == 0:
                self.draw_cell(row, col)
                break
            
            next_cell = random.choice(to_visit)
            
            if next_cell[0] == row and next_cell[1] == col + 1:
                self.cells[row][col].has_right_wall = False
                self.cells[next_cell[0]][next_cell[1]].has_left_wall = False
            elif next_cell[0] == row and next_cell[1] == col - 1:
                self.cells[row][col].has_left_wall = False
                self.cells[next_cell[0]][next_cell[1]].has_right_wall = False
            elif next_cell[0] == row + 1 and next_cell[1] == col:
                self.cells[row][col].has_bottom_wall = False
                self.cells[next_cell[0]][next_cell[1]].has_top_wall = False
            elif next_cell[0] == row - 1 and next_cell[1] == col:
                self.cells[row][col].has_top_wall = False
                self.cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
                
            self.break_walls_r(next_cell[0], next_cell[1])
    
    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False
  
    
    def solve(self):
        solved = self.solve_r(0, 0)
        return solved
    
    def solve_r(self, row, col):
        self.animate()
        self.cells[row][col].visited = True
        if row == self.num_rows - 1 and col == self.num_cols - 1:
            return True
        
        directions = ['up', 'down', 'left', 'right']
        random.shuffle(directions)
        
        for direction in directions:
                
            if direction == 'right':    
                if col < self.num_cols - 1 and not self.cells[row][col+1].visited and self.cells[row][col].has_right_wall == False and self.cells[row][col+1].has_left_wall == False:
                    self.cells[row][col].draw_move(self.cells[row][col+1])
                    if self.solve_r(row, col+1) == True:
                        return True
                    else:
                        self.cells[row][col].draw_move(self.cells[row][col+1], undo=True)
            if direction == 'down':    
                if row < self.num_rows - 1 and not self.cells[row+1][col].visited and self.cells[row][col].has_bottom_wall == False and self.cells[row+1][col].has_top_wall == False:
                    self.cells[row][col].draw_move(self.cells[row+1][col])
                    if self.solve_r(row+1, col) == True:
                        return True
                    else:
                        self.cells[row][col].draw_move(self.cells[row+1][col], undo=True)
            if direction == 'left':    
                if col > 0 and not self.cells[row][col-1].visited and self.cells[row][col].has_left_wall == False and self.cells[row][col-1].has_right_wall == False:
                    self.cells[row][col].draw_move(self.cells[row][col-1])
                    if self.solve_r(row, col-1) == True:
                        return True
                    else:
                        self.cells[row][col].draw_move(self.cells[row][col-1], undo=True)
            if direction == 'up':    
                if row > 0 and not self.cells[row-1][col].visited and self.cells[row][col].has_top_wall == False and self.cells[row-1][col].has_bottom_wall == False:
                    self.cells[row][col].draw_move(self.cells[row-1][col])
                    if self.solve_r(row-1, col) == True:
                        return True
                    else:
                        self.cells[row][col].draw_move(self.cells[row-1][col], undo=True)
        
        return False
            
            
            
        
    def animate(self):
        self.window.redraw()
        time.sleep(0.05)
        