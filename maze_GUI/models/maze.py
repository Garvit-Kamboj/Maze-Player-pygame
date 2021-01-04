# import pygame
from models.item import Item
from models.player import Player

def openfile(file):
    """This function makes a maze structure for a file, and returns it"""
    with open(file, mode='r') as f:
        content_readlines = f.readlines()
    return [[char for char in line.strip()] for line in content_readlines]


class Maze():
    """This class instantiates Maze structure, sets the starting coordinates of the player,
    sets the ending coordinates of game, displays the structure etc."""

    def __init__(self, filename='maze.txt'):
        self._structure = openfile(filename)
        self.structure()

    def structure(self):
        """Returns the Maze structure"""
        return self._structure

    def set_starting_coordinates(self, start_val, x_cord=0, y_cord=2):
        """Sets the given coordinates to to starting point of the game""" 
        # self.starting_character = start_val
        self._structure[x_cord][y_cord] = start_val
        # print(f"Starting: {start_val} at ({x_cord},{y_cord})")

    def set_ending_coordinates(self, end_val, x_cord=17, y_cord=19):
        """Sets the given coordinates to the ending point of game, by default ehich is 
        (3, 11) which is also an end of maze structure"""
        self.ending_character = end_val
        self._structure[x_cord][y_cord] = end_val
        # print(f"Ending: represented by {end_val} at ({x_cord},{y_cord})")
        return end_val

    def can_move_to(self, line_number, column_number):
        """This function returns True if player can move to given coordinates(i.e if there's no wall),
        false otherwise"""
        return True if self._structure[line_number][column_number] != 'x' else False

    def display(self):
        """This displays the structure onscreen"""
        for line in self._structure:
            print(*line)

    def find_random_spot(self):
        """Returns all the random spots as a tuple of tuples in the maze structure which are empty spaces"""
        self.random_spots = []
        for line in self._structure:
            for index, char in enumerate(line):
                if char == ' ':
                    self.random_spots.append((self._structure.index(line), index))

        return tuple(self.random_spots)

    def check_random_items(self):
        """Returns True if player has gathered all of the Items (which were placed randomly in structure)
        from the Maze structure, flase otherwise""" 
        self.random_items = []
        for line in self._structure:
            for index, char in enumerate(line):
                if isinstance(char, Item):
                    self.random_items.append((self._structure.index(line), index))
        
        return True if len(self.random_items) == 0 else False
                   

    def is_item(self, line_number, column_number):
        """Returns True if the location requested (using coordinates) is of a random Item, 
        false otherwise"""
        return True if isinstance(self._structure[line_number][column_number], Item) else False

    def get_location(self):
        """Returns the coordinates(location) of Player in the Maze structure"""
        for line in self._structure:
            for index, char in enumerate(line):
                if isinstance(char, Player):
                    return (self._structure.index(line), index)

    def is_exit(self, line_number, column_number):
        """ Returns True if location requested is the exit point"""
        return True if self._structure[line_number][column_number] == self.ending_character else False


    
