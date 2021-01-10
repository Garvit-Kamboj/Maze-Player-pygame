# Maze-Player-pygame
This is an interactive pygame in which player collects five different items and reach the end of maze by collecting a key. There is also a welcome and good-bye screen.

Description and Features
This is the MVC pattern for Maze game. Firstly, in Models, Maze class instantiates the structure
(which is structure/maze of game). Maze class is in aggregation relationship with Player class.
Player class instantiates name and its backpack (in which collected items will be stored). Maze
class is also in aggregation relationship with Item class. Item class instantiates name of any item
and family it belongs to.
The Maze class also interacts with MazeController class. MazeController class captures all the
keyboard movements (up/down/left/right) and takes action (moves player) accordingly. As
player moves on every keystroke (a/s/w/d), Maze view is showed to the player, which comes
from interaction of controllers (MazeController) with Views (MazeView).
Simply put, this is the pygame version of the maze game. The MVC pattern duplicated and integrated into
pygame to have a character that moves through the maze and to also allow the game to be run
using both the MVC and pygame. The player and backpack work the same, where the backpack
holds all the collected items, and the player has a backpack. In the pygame version, player is
moved using the (left, up, right, down) arrows on the keyboard. The player sprites move
according to the arrow.
On the whole, we start by creating instances in main_GUI.py program. After creating an instance
of Maze, a player is instantiated and its starting point is decided (by default which is zero). At the
same time, end point of game is decided (by default which is end of maze, (3, 11) in this case).
We then place the 5 items on Maze grid. After, this controller and views class come into place.
Some Extra-Features Implemented in the Maze grid:
1. Setting starting coordinates of player manually.
2. Setting ending character and ending coordinates of game manually.
3. Getting all of the random empty spots.
4. Checking if player collected all the items from the Maze grid (if yes, then true).
5. Getting the exact location (coordinates) of a player.
6. We added a functionality of sounds in background
7. We made display screen and game end screen
8. All the random items which user collects, they eat each other, to confuse the player. For
example, lion who is stronger than pokemon will eat him and go to the pokemon’s place,
if user catches lion. This makes game more interactive.
9. Player has to collect the key in order to go to exit door.
10. Calculate high score based on how many animals does user collect.

Some features about Scores and Database
As an added feature, at the exit/game-over menu players are shown their points according to the
amount of time they took, and the number of items collected. Each item is multiplied by 250 to
calculate the amount of points for the items. If all items are collected a bonus of 500 points is
given. Right when the player presses a key to move the time-bonus starts counting down. It goes
from 999 to 0, a negative time-bonus is not possible. Total score is shown in the last line of
scores. Players have the option to add a username to keep the score in their local database. The
database is a json based file keeping a list of dictionaries. Each score is added as a dictionary of
name and score. Score is saved when a username with a max length of 4 letters is entered and the
ENTER key is pressed. If the exit window is closed with out entering a username and pressing
ENTER score is not saved to the database. To view the high score table, the flask application
needs to be running. Then all the scores will we loaded into the high score table, going from
highest score to the lowest

To run the game, just download and extract the code, type "python main_GUI.py" in terminaal (Hit Enter) for GUI version and "python main_text.py" (Hit Enter) for text version.
