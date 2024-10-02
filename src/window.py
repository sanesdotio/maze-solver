from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.running = False
        
        self.root.title = "Maze Solver"
        
        self.canvas.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    