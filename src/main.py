from window import Window
from maze import Maze

def main():
    win = Window(1024, 960)
    
    maze = Maze(50, 50, 15, 15, 50, 50, win)
    maze.solve()
    
    win.wait_for_close()
    
    

main()
