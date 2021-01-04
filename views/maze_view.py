class MazeView():
    """After instantiating maze, this class displays the structure of maze 
    and interacts with controller"""
    def __init__(self, maze):
        self.m1 = maze
        self.show_map()

    def show_map(self):
        """Shows the structure of maze"""
        self.m1.display() 
