import pytest
from models.maze import Maze, openfile
from models.player import Player

@pytest.fixture
def maze():
    return Maze('maze.txt')

@pytest.fixture
def player():
    return Player('Garvit')

def test_open_file():
    """ 010A checks if file is openeed correctly"""
    assert Maze()._structure == openfile('maze.txt')

def test_starting_coordinates(maze, player):
    """ 020A checks if starting coordinates are set correctly"""
    maze.set_starting_coordinates(player, 0, 2)
    assert maze._structure[0][2] == player

def test_ending_coordinates(maze, player):
    """ 020B checks if ending coordinates are set correctly"""
    maze.set_ending_coordinates('X')
    assert maze._structure[17][19] == 'X'

def test_moveto(maze):
    """020C checks if player can move to given coordinates"""
    assert maze.can_move_to(0, 1) == False

def test_random_spot(maze):
    """030A checks if given random spot is an instance of class Maze"""
    assert isinstance(maze.find_random_spot(), Maze) == False

def test_random_item(maze):
    """ 050A checks if any random items are still left in Maze game"""
    assert maze.check_random_items() == True
    
def test_isitem(maze):
    """ 040A checks if location is random item"""
    assert maze.is_item(0, 1) == False

def test_isexit(maze):
    """ 060A checks if location is exit point"""
    maze.set_ending_coordinates('X')
    assert maze.is_exit(0, 1) == False

def test_location(maze, player):
    """ 040B checks and confirms the current location of Player"""
    maze.set_starting_coordinates(player, 0, 1) == None
    assert maze.get_location() == (0, 1)