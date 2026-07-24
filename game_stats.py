"""
Module Name: game_stats.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module stores game status information, such as how many ships
the player has left during the game.
"""
#from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    """Track game statistics for Alien Invasion."""
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the number of ships the player has left."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats() 

    def init_saved_scores(self):
        """Load the saved high score file if it exists."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            if not contents:
                print('file empty')
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_score()
            # save the file
    
    def save_score(self):
        """Save the high score to a JSON file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Reset ships, score, and level for a new game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Update score, max score, and high score after collisions."""
        # update score
        self._update_score(collisions)

    
        # update max_score
        self._update_max_score()

        # udate hi_score
        self._update_hi_score()

    def _update_max_score(self):
        """Update max score when the current score is higher."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
    
    def _update_hi_score(self):
        """Update high score when the current score is higher."""
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f'Hi: {self.hi_score}')
        

    def _update_score(self, collisions):
        """Add points for each alien destroyed."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')
        

    def update_level(self):
        """Increase the level by one."""
        self.level += 1
        print(self.level)


    
