import pygame

class ScoreKeeping:
    def __init__(self):
        self.time_score = 999


    def update(self, rmBy):
        # Update the score
        self.time_score -= rmBy
        