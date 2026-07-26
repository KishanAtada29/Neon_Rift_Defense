"""
Module Name: asteroid.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 24, 2026

Purpose:
This module creates the Asteroid class for the Asteroid Rift Defense game.
It handles one asteroid's image, position, movement, edge detection, and drawing.
"""

import pygame 
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asteriod_fleet import AsteroidFleet


class Asteroid(Sprite):
    """Represent one asteroid in the asteroid fleet."""

    def __init__(self, fleet: 'AsteroidFleet', x: float, y: float):
        """Initialize an asteroid at the given x and y position."""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.asteroid_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.asteroid_w, self.settings.asteroid_h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x =  float(self.rect.x)

    def update(self):
        """Move the asteroid left or right based on the fleet direction."""
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Return True if the asteroid reaches the left or right screen edge."""
        return self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left
    
    def draw_asteroid(self):
        """Draw the asteroid on the screen."""
        self.screen.blit(self.image, self.rect)