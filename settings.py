"""
Module Name: settings.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module stores all settings for the Alien Invasion game. It includes
screen size, image files, sound files, ship settings, bullet settings,
alien settings, fleet movement, and starting ship count.
"""

from pathlib import Path
class Settings:
    """Store all game settings for Alien Invasion."""
    def __init__(self):
        """Initialize screen, ship, bullet, alien, and fleet settings."""
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() /'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() /'Assets'/'file'/'scores.json'

        self.ship_file = Path.cwd() /'Assets'/'images' /'ship2(no bg).png'
        self.ship_w = 20
        self.ship_h = 30
        

        self.bullet_file = Path.cwd()  /'Assets' / 'images' / 'laserBlast.png'
        self.bullet_sound = Path.cwd() /'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() /'Assets' / 'sound' / 'impactSound.mp3'

        
        self.bullet_w = 250
        self.bullet_h = 80
        

        self.alien_file = Path.cwd() /'Assets'/'images'/'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        
        self.fleet_direction = 1
        

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size =20
        self.font_file = Path.cwd() /'Assets'/'Fonts'/'Silkscreen'/'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """Set values that can reset or change during the game."""
        self.ship_speed = 5
        self.starting_ship_count = 3
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50
    
    def increase_difficulty(self):
        """Increase game speed when the player reaches the next level."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
