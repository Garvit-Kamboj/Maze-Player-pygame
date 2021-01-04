import pygame
from os import path, truncate, system
import sys
from random import choice
from models.item import Item
from models.maze import Maze
from models.player import Player
from views.background import Background
from controllers.maze_controller_GUI import AppController
from views.maze_view import MazeView
from models.score_keeping import ScoreKeeping


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

char_to_image = {
    'x': 'images/block.png',
}

def draw_text(surf, text, size, x, y):
    """This functions draws the text on screen"""
    font_name = pygame.font.SysFont(None, size)
    text_surface = font_name.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.topright = (x, y)
    surf.blit(text_surface, text_rect)


class App(pygame.sprite.Sprite):
    """This class handles the pygame, instantiates different surfaces, makes window and blits them on screen"""
    WORLD_SIZE = 20
    BLOCK_SIZE = 32
    WIDTH = WORLD_SIZE*BLOCK_SIZE
    HEIGHT = WORLD_SIZE*BLOCK_SIZE

    SIZE = [WORLD_SIZE*BLOCK_SIZE, WORLD_SIZE*BLOCK_SIZE]
    clock = pygame.time.Clock()

    def __init__(self):
        """This class instantiates display, player and wall surfaces and sets their coordinates"""
        super().__init__()
        self._running = True
        self._display_surf = None
        self._player_surf = None
        self._block_surf = None

        # Creating an instance of a Player class
        self.p1 = Player('Garvit')
        # Creating an instance of a Maze class
        self.m1 = Maze('maze.txt')

        # Player and Maze are in aggregation Relationship
        self.m1.set_starting_coordinates(self.p1, 0, 2)

        # By default, ending coordinates are end of maze
        self.m1.set_ending_coordinates('E')

        # Creating four random Items
        self.make_random_items()

        #Adding random items to the maze
        self.add_random_items()
        
    def init(self):
        """This function sets the different surfaces of game, such as player, wall, items etc."""
        pygame.init()

        # Set-up for music
        pygame.mixer.init()
        pygame.mixer.music.load("./sounds/intro_music.mp3")
        pygame.mixer.music.play(loops=-1)

        #Creating the surface for display, key and player
        self._display_surf = pygame.display.set_mode(App.SIZE)
        self._door_surf = pygame.image.load('images/key.png').convert()
        self._door_surf.set_colorkey((0, 0, 0))
        self._player_surf = pygame.image.load('images/player.png').convert()
        self._player_surf.set_colorkey((0, 0, 0))

        #Creating random items surfaces
        self.i1_surf = pygame.image.load('images/dragon.png').convert()
        self.i2_surf = pygame.image.load('images/tiger.png').convert()
        self.i3_surf = pygame.image.load('images/bat.png').convert()
        self.i4_surf = pygame.image.load('images/fish.png').convert()
        self.i5_surf = pygame.image.load('images/pokemon.png').convert()
        self._items_surf = [self.i1_surf, self.i2_surf, self.i3_surf, self.i4_surf, self.i5_surf]
        for items in self._items_surf:
            items.set_colorkey((0, 0, 0))

    def make_random_items(self):
        """This function creates the random items"""
        self.i1 = Item('Zew', 'Dragon')
        self.i2 = Item('Mai', 'Tiger')
        self.i3 = Item('Chaos', 'Bat')
        self.i4 = Item('Kate', 'Fish')
        self.i5 = Item('Juan', 'Pokemon')

    def add_random_items(self):
        """This function adds the random items to the structure at the random places"""
        # Adding 4 random items to structure
        # Depicting Aggregation relationship between Maze and Items 
        five_random_spots = [[empty for empty in choice(self.m1.find_random_spot())] for _ in range (5)]
        self.m1._structure[five_random_spots[0][0]][five_random_spots[0][1]] = self.i1
        self.m1._structure[five_random_spots[1][0]][five_random_spots[1][1]] = self.i2
        self.m1._structure[five_random_spots[2][0]][five_random_spots[2][1]] = self.i3
        self.m1._structure[five_random_spots[3][0]][five_random_spots[3][1]] = self.i4
        self.m1._structure[five_random_spots[4][0]][five_random_spots[4][1]] = self.i5

    def draw_surface(self):
        """This function draws the surfaces on screen, i.e walls, player and key"""
        for y, row in enumerate(self.m1._structure):
            for index, char in enumerate(row):
                image = char_to_image.get(char, None)
                if image:
                    self._display_surf.blit(pygame.image.load(char_to_image[char]), (index*App.BLOCK_SIZE, y*App.BLOCK_SIZE))
        self._display_surf.blit(self._player_surf, (self.m1.get_location()[1]*App.BLOCK_SIZE, self.m1.get_location()[0]*App.BLOCK_SIZE))
        self._display_surf.blit(self._door_surf, (19*App.BLOCK_SIZE, 17*App.BLOCK_SIZE))

    def draw_item(self):
        """This function draws the items on the screen """
        item = 0
        for y, row in enumerate(self.m1._structure):
            for index, char in enumerate(row):
                if isinstance(char, Item):
                    self._display_surf.blit(self._items_surf[item], (index*App.BLOCK_SIZE, y*App.BLOCK_SIZE))
                    item += 1

    def render(self):
        """render function renders the display and draw surfaces on screen every time in while loop"""
        self._display_surf.fill((32, 32, 32))
        self.draw_surface()
        self.draw_item()

    def clean(self):
        """End of pygame"""
        pygame.quit()

    def intro(self):
        """This is intro of our pygame"""
        self.init()
        self.background = Background('images/intro.jpg', [0,0])

        '''display main menu'''
        # display instructions for game
        arrow_keys = pygame.image.load(path.join('images', 'arrow_keys.png')).convert_alpha()
        arrow_keys = pygame.transform.scale(arrow_keys, (200, 120))

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Use arrow keys to move player', False, (0, 0, 0))
        textsurface1 = myfont.render('1. Hit enter to start game', False, (0, 0, 0))
        textsurface2 = myfont.render('2. Hit escape to quit', False, (0, 0, 0))

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self._display_surf.fill([245, 245, 245])
            self._display_surf.blit(textsurface,(200, 590))
            self._display_surf.blit(textsurface1,(50, 445))
            self._display_surf.blit(textsurface2,(50, 470))
            self._display_surf.blit(self.background.image, self.background.rect)
            self._display_surf.blit(arrow_keys, (400, 475))
            pygame.display.flip()

    def execute(self):
        """This function runs the main game. This is the function where controller controls 
        the player on screen (i.e controller interacts with the App class)"""
        pygame.mixer.music.load("./sounds/game_music.mp3")
        pygame.mixer.music.play(loops=-1)

        time_score = 0
        first_key = True

        while(self._running):

            if type(time_score) == ScoreKeeping and self._running:
                time_score.update(1)    

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if first_key == True:
                        time_score = ScoreKeeping()
                        first_key = False
                    if event.key == K_ESCAPE:
                        self._running = False
                    elif event.key in (K_DOWN, K_LEFT, K_RIGHT, K_UP):
                        AppController(self.m1, self.p1, self._display_surf, self._player_surf, event.key, time_score)
                elif event.type == QUIT:
                    self._running = False

            self.render()
            if type(time_score) == ScoreKeeping:
                draw_text(self._display_surf, str(time_score.time_score), 50, 640, 1)
            pygame.display.flip()
            App.clock.tick(30)
        self.clean()


if __name__ == "__main__":
    """Starting point of game"""
    game = App()
    game.intro()
    game.execute()


# print()
# print(f'Initial location of Player: {m1.get_location()}')
# print('-'*40+'Initial structure'+'-'*40)
# m1.display()

# # checking the status of exit point
# print(f"Is exit: {m1.is_exit(3, 11)}")

# AppController(m1, p1) # Controlling maze through maze_controller 





