"""
Module Name: button.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module creates the Button class for the Alien Invasion game. It handles
the button's position, text, drawing, and checking if the player clicked it.
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Button:
    """Create and manage a clickable game button."""

    def __init__(self, game: 'AlienInvasion', msg):
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
        """Draw the button and its text on the screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

    def check_clicked(self, mouse_pos):
        """Return True if the mouse position is inside the button."""
        return self.rect.collidepoint(mouse_pos)