"""
Module Name: arsenal.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module manages all bullets fired by the ship. It updates bullets,
removes bullets that leave the screen, draws bullets, and controls how
many bullets can be fired at one time.
"""


import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage the group of bullets fired by the ship."""
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the bullet group and game settings."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update all bullets and remove bullets that go off screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()
    
    def _remove_bullets_offscreen(self):
        """Remove bullets when they leave the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets on the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create a new bullet if the bullet limit has not been reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
