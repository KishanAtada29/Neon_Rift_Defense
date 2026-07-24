"""
Module Name: bullet.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module creates the Bullet class. It handles the bullet image,
starting position, upward movement, and drawing bullets on the screen.
"""

import pygame 
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represent one bullet fired by the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize a bullet at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.imgae = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upward on the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)