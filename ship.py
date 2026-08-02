"""
Module Name: ship.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 24, 2026

Purpose:
This module creates the Ship class for the Asteroid Rift Defense game. It handles
the player's custom ship image, movement, firing bullets, drawing the ship, and
checking collisions with asteroids.
"""

import pygame 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asteriod_rift_defence import AsteroidRiftDefence
    from arsenal import Arsenal
class Ship:
    """Represent the player's ship."""

    def __init__(self, game: 'AsteroidRiftDefence', arsenal: 'Arsenal'):
        """Initialize the ship, screen, movement flags, and arsenal."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        #self.image = pygame.image.load(self.settings.ship_file).convert_alpha()
        self.load_ship_image(self.settings.ship_files[0])
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def load_ship_image(self, image_file):
        """Load and scale the ship image."""
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(
        self.image,
        (self.settings.ship_w, self.settings.ship_h)
        )
        self.rect = self.image.get_rect()

    def _center_ship(self):
        """Place the ship at the bottom center of the screen."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship movement and its bullets."""
        #updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()


    def update_ship_for_level(self):
        """Change the ship image based on the current level."""
        level_index = min(
            self.game.game_stats.level - 1,
            len(self.settings.ship_files) - 1
        )

        old_midbottom = self.rect.midbottom
        self.load_ship_image(self.settings.ship_files[level_index])
        self.rect.midbottom = old_midbottom
        self.x = float(self.rect.x)
    

    def _update_ship_movement(self):
        """Move the ship left or right within the screen boundaries."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draw bullets and the ship on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fire a bullet from the ship."""
        return self.arsenal.fire_bullet()
    
    def check_collision(self, other_group):
        """Return True if the ship collides with another sprite group."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
        