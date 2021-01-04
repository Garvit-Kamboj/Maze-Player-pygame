import pygame
import sys
import json
import time
from pygame.locals import *
from os import path
from string import punctuation
from views.maze_view import MazeView
from views.background import Background
from models.item import Item
from models.score import Score
from models.score_manager import ScoreManager

musics = {
    'winner': path.join(path.dirname(__file__), '..', 'sounds', 'winner.mp3'),
    'loser': path.join(path.dirname(__file__), '..', 'sounds', 'loser.mp3')
}


def highscores(username, total_score):
    file_path = path.join(path.dirname(__file__), '..', 'game_data', 'database.json')
    highscore_list = ScoreManager()
    if not path.isfile(file_path):
        open(file_path, "w+")
    with open(file_path, 'r') as file:
        data = file.readline()
        if data == '':
            with open(file_path, "w") as file:
                file.write('{"scores": []}')
    highscore_list.from_json(file_path)
    highscore_list.add_score(Score(str(username), int(total_score)))
    return highscore_list.to_json(file_path)


def draw_text(surf, text, x, y, color):
    """This function draws the text on screen"""
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    text_str = myfont.render(text, True, color)
    text_rect = text_str.get_rect()
    text_rect.bottomleft = (x, y)
    surf.blit(text_str, text_rect)


class AppController():
    """After instantiating maze, player, their respective surfaces, keys and scores, this class controls the maze"""

    def __init__(self, m1, p1, d_surf, p_surf, key, time_score):
        self.m1 = m1
        self.p1 = p1
        self.player_surf = p_surf
        self.display_surf = d_surf
        self.key = key
        self.time_score = time_score
        self.control_maze()

    def exit(self):
        """This is a function which runs when the game is over"""
        pygame.mixer.music.load(musics['winner'])
        pygame.mixer.music.play(loops=-1)

        self.background = Background(
            (path.join(path.dirname(__file__), '..', 'images', 'exit.jpg')), [0, 0])
        username = ''
        totalscore = 0

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == K_RETURN and username != '':
                        highscores(username, totalscore)
                        pygame.quit()
                        sys.exit()
                    elif len(username) < 4 and (event.unicode not in punctuation) and event.key != K_SPACE:
                        username += event.unicode
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # text/sentence to be written on the final screen
                itemsCollected = (
                    f'Items collected: {len(self.p1.backpack)} X 250')
                timeBonus = (f'Time Bonus: {self.time_score.time_score}')
                totalscore = (len(self.p1.backpack) * 250) + \
                    int(self.time_score.time_score)
                totalscorestr = (f'Total score: {totalscore}')
                highscore_line = (f'--- Register highscore ---')
                input_prompt = (f'Enter username here(4 letters max): ')
                treasures = f'Collection bonus: 500'

                self.display_surf.fill([245, 245, 245])

                # draw the items collected text
                draw_text(self.display_surf, itemsCollected,
                          12, 502, (153, 0, 0))
                # draw the time left
                draw_text(self.display_surf, timeBonus, 12, 522, (153, 0, 0))
                # if all the treasures are collected, add a bonus 500 points
                if self.m1.check_random_items():
                    draw_text(self.display_surf, treasures,
                              12, 544, (153, 0, 0))
                    totalscore = (len(self.p1.backpack) * 250) + \
                        int(self.time_score.time_score) + 500
                    totalscorestr = (f'Total score: {totalscore}')
                    draw_text(self.display_surf, totalscorestr,
                              12, 566, (153, 0, 0))
                    draw_text(self.display_surf, highscore_line,
                              12, 588, (153, 0, 0))
                    draw_text(self.display_surf, input_prompt,
                              12, 610, (153, 0, 0))
                    input_rect = pygame.Rect(360, 584, 100, 28)
                # else do the total without bonus
                else:
                    draw_text(self.display_surf, totalscorestr,
                              12, 544, (153, 0, 0))
                    draw_text(self.display_surf, highscore_line,
                              12, 566, (153, 0, 0))
                    draw_text(self.display_surf, input_prompt,
                              12, 588, (153, 0, 0))
                    input_rect = pygame.Rect(360, 562, 100, 28)

                # making the input rectangle
                pygame.draw.rect(self.display_surf,
                                 (65, 105, 225), input_rect, 2)

                # setting the font for the input
                myfont = pygame.font.SysFont('Comic Sans MS', 20)
                # set the font type for the input
                username_surface = myfont.render(username, True, (153, 0, 0))
                # write the user input inside the input rectangle
                self.display_surf.blit(
                    username_surface, (input_rect.x + 10, input_rect.y - 2))

                # show the 'Game Over' picture
                self.display_surf.blit(
                    self.background.image, self.background.rect)
                pygame.display.flip()

    def control_maze(self):
        """This function controls the maze based on user keypresses"""

        current_loc = self.m1.get_location()
        row = current_loc[0]
        column = current_loc[1]

        # print()
        if self.key == K_LEFT:
            """Press left key to move player left"""
            if self.m1.can_move_to(row, column-1):
                # print(f"Moved: {self.m1.can_move_to(row, column-1)}")
                if self.m1.is_item(row, column-1):
                    self.p1.backpack.append(self.m1._structure[row][column-1])
                self.m1._structure[row][column] = ' '
                self.m1._structure[row][column-1] = self.p1
            # else:
            #     print(f"Moved: {self.m1.can_move_to(row, column-1)}")

        elif self.key == K_DOWN:
            """Press down key to move player down"""
            if self.m1.can_move_to(row+1, column):
                # print(f"Moved: {self.m1.can_move_to(row+1, column)}")
                if self.m1.is_item(row+1, column):
                    self.p1.backpack.append(self.m1._structure[row+1][column])
                self.m1._structure[row][column] = ' '
                self.m1._structure[row+1][column] = self.p1
            # else:
            #     print(f"Moved: {self.m1.can_move_to(row+1, column)}")

        elif self.key == K_UP:
            """Press up key to move player up"""
            if self.m1.can_move_to(row-1, column):
                # print(f"Moved: {self.m1.can_move_to(row-1, column)}")
                if self.m1.is_item(row-1, column):
                    self.p1.backpack.append(self.m1._structure[row-1][column])
                self.m1._structure[row][column] = ' '
                self.m1._structure[row-1][column] = self.p1
            # else:
            #     print(f"Moved: {self.m1.can_move_to(row-1, column)}")

        elif self.key == K_RIGHT:
            """Press right to move player right"""
            if self.m1.can_move_to(row, column+1):
                # print(f"Moved: {self.m1.can_move_to(row, column+1)}")
                if self.m1.is_item(row, column+1):
                    self.p1.backpack.append(self.m1._structure[row][column+1])
                self.m1._structure[row][column] = ' '
                self.m1._structure[row][column+1] = self.p1
            # else:
            #     print(f"Moved: {self.m1.can_move_to(row, column+1)}")

        # print(f"Current location of Player: {self.m1.get_location()}")
        # print('-'*40+'Current structure'+'-'*40)
        # MazeView(self.m1)

        # if not self.m1.check_random_items() and self.m1.get_location() == (17, 19):
        #     """If player does not collect all items and reaches end of game,
        #     exit the game with Status Failed"""
        #     self.exit('FAILED: You didnt collect all items before reaching an end', 'loser')
        #     # raise SystemExit('FAILED: You didnt collect all of the items before reaching the end of maze')

        if self.m1.get_location() == (17, 19):
            """If player collects all items and reaches end of game,
            exit the game with Status Success"""
            # print(f'Collected Items: {self.p1.backpack}')
            # for item in self.p1.backpack:
            #     print(f"You collected {item}")
            self.exit()
