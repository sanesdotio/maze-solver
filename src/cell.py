from line import Line
from point import Point
class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.middle = None
        self.win = window
        self.visited = False
        
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        top_left = Point(x1, y1)
        bottom_left = Point(x1, y2)
        top_right = Point(x2, y1)
        bottom_right = Point(x2, y2)
        self.middle = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        
        if self.has_left_wall:
            self.win.draw_line(Line(top_left, bottom_left))
        else:
            self.win.draw_line(Line(top_left, bottom_left), fill_color="white")
            
        if self.has_right_wall:
            self.win.draw_line(Line(top_right, bottom_right))
        else:
            self.win.draw_line(Line(top_right, bottom_right), fill_color="white")
            
        if self.has_top_wall:
            self.win.draw_line(Line(top_left, top_right))
        else:
            self.win.draw_line(Line(top_left, top_right), fill_color="white")
    
        if self.has_bottom_wall:
            self.win.draw_line(Line(bottom_left, bottom_right))
        else:
            self.win.draw_line(Line(bottom_left, bottom_right), fill_color="white")
    
    def draw_move(self, to_cell, undo=False):
        line_color = "gray"
        if undo:
            line_color = "red"
        
        self.win.draw_line(Line(self.middle, to_cell.middle), fill_color=line_color)
            
        
