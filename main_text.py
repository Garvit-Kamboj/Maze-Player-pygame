from random import choice
from models.item import Item
from models.maze import Maze
from models.player import Player
from controllers.maze_controller_text import MazeController
from views.maze_view import MazeView


# Creating an instance of a Player class
p1 = Player('Garvit')

# Creating an instance of a Maze class
m1 = Maze('maze.txt')

# Player and Maze are in aggregation Relationship
m1.set_starting_coordinates(p1, 0, 2)

# By default, ending coordinates are end of maze
m1.set_ending_coordinates('E')

# Creating four random Items
i1 = Item('Zew', 'Dragon')
i2 = Item('Mai', 'Dinosaur')
i3 = Item('Chaos', 'Bat')
i4 = Item('Kate', 'Fish')
i5 = Item('Juan', 'Pokemon')

# Adding 4 random items to structure
# Depicting Aggregation relationship between Maze and Items 
five_random_spots = [[empty for empty in choice(m1.find_random_spot())] for _ in range (5)]
m1._structure[five_random_spots[0][0]][five_random_spots[0][1]] = i1
m1._structure[five_random_spots[1][0]][five_random_spots[1][1]] = i2
m1._structure[five_random_spots[2][0]][five_random_spots[2][1]] = i3
m1._structure[five_random_spots[3][0]][five_random_spots[3][1]] = i4
m1._structure[five_random_spots[4][0]][five_random_spots[4][1]] = i5

print()
print(f'Initial location of Player: {m1.get_location()}')
print('-'*40+'Initial structure'+'-'*40)
m1.display()

# checking the status of exit point
# print(f"Is exit: {m1.is_exit(3, 11)}")

MazeController(m1, p1) # Controlling maze through maze_controller 





