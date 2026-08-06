"""
Module Name: bullet.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 24, 2026

Purpose:
This module creates the Bullet class for the Asteroid Rift Defense game.
It handles the custom laser bullet image, starting position, upward movement,
and drawing the bullet on the screen.
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asteriod_rift_defence import AsteroidRiftDefence
    from arsenal import Arsenal

class Button:
    """Create and manage a clickable game button."""

    def __init__(self, game: 'AsteroidRiftDefence' , msg):
        """Initialize the button settings, position, font, and message."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w,self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)
    

    def _prep_msg(self,msg):
        """Render the button message and center it on the button."""
        self.msg_img = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def  draw(self):
        """Draw the button as a red parallelogram and draw its text."""
        points = [
            (self.rect.left + 30, self.rect.top),
            (self.rect.right, self.rect.top),
            (self.rect.right - 30, self.rect.bottom),
            (self.rect.left, self.rect.bottom)
        ]

        # red parallelogram
        pygame.draw.polygon(self.screen, self.settings.button_color, points)

        # white border
        pygame.draw.polygon(self.screen, (0, 0, 0), points, 1)

        self.screen.blit(self.msg_img, self.msg_img_rect)

    def check_clicked(self, mouse_pos):
        """Return True if the mouse position is inside the button."""
        return self.rect.collidepoint(mouse_pos)