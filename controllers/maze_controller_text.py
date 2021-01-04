from views.maze_view import MazeView
from models.item import Item

class MazeController():
    """After instantiating maze and player (denoted by m1 and p1), this class controls the maze""" 
    def __init__(self, maze, player):
        self.m1 = maze
        self.p1 = player
        self.control_maze()

    def control_maze(self): 

        direction = input('Enter the direction?')
        while direction != 'q':

            current_loc = self.m1.get_location()
            row = current_loc[0]
            column = current_loc[1]

            print()
            if direction == 'A' or direction =='a':
                """Press a or A to move player left"""
                if self.m1.can_move_to(row, column-1):
                    print(f"Moved: {self.m1.can_move_to(row, column-1)}")
                    if self.m1.is_item(row, column-1):
                        self.p1.backpack.append(self.m1._structure[row][column-1])
                    self.m1._structure[row][column] = ' '
                    self.m1._structure[row][column-1] = self.p1
                else:
                    print(f"Moved: {self.m1.can_move_to(row, column-1)}")

            elif direction == 'S' or direction =='s':
                """Press s or S to move player down"""
                if self.m1.can_move_to(row+1, column):
                    print(f"Moved: {self.m1.can_move_to(row+1, column)}")
                    if self.m1.is_item(row+1, column):
                        self.p1.backpack.append(self.m1._structure[row+1][column])
                    self.m1._structure[row][column] = ' '
                    self.m1._structure[row+1][column] = self.p1
                else:
                    print(f"Moved: {self.m1.can_move_to(row+1, column)}")
                
            elif direction == 'W' or direction =='w':
                """Press w or W to move player up"""
                if self.m1.can_move_to(row-1, column):
                    print(f"Moved: {self.m1.can_move_to(row-1, column)}")
                    if self.m1.is_item(row-1, column):
                        self.p1.backpack.append(self.m1._structure[row-1][column])
                    self.m1._structure[row][column] = ' '
                    self.m1._structure[row-1][column] = self.p1
                else:
                    print(f"Moved: {self.m1.can_move_to(row-1, column)}")
                    
            elif direction == 'D' or direction =='d':
                """Press d or D to move player right"""
                if self.m1.can_move_to(row, column+1):
                    print(f"Moved: {self.m1.can_move_to(row, column+1)}")
                    if self.m1.is_item(row, column+1):
                        self.p1.backpack.append(self.m1._structure[row][column+1])
                    self.m1._structure[row][column] = ' '
                    self.m1._structure[row][column+1] = self.p1
                else:
                    print(f"Moved: {self.m1.can_move_to(row, column+1)}")
            

            print(f"Current location of Player: {self.m1.get_location()}")
            print('-'*40+'Current structure'+'-'*40)
            MazeView(self.m1)

            if not self.m1.check_random_items() and self.m1.get_location() == (3, 11):
                """If player does not collect all items and reaches end of game, 
                exit the game with Status Failed"""

                raise SystemExit('FAILED: You didnt collect all of the items before reaching the end of maze')

            if self.m1.check_random_items() and self.m1.get_location() == (3, 11):
                """If player collects all items and reaches end of game, 
                exit the game with Status Success"""
                
                print(f'Collected Items: {self.p1.backpack}')
                for item in self.p1.backpack:
                    print(f"You collected {item}")
                raise SystemExit('SUCCESS: You have collected all Items and reached end of maze')
            
        
            direction = input('Enter the direction?')
