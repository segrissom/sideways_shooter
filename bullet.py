# this is part of my solution to the Python Crash Course
# Chapter 12, exercise 5
import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """This is in charge of the bullets that come
    from the ship"""

    def __init__(self, ai_settings, screen, cowboy):
        """This creates the bullet where the man is
        and hopefully around the same area as his
        gun"""
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0, ai_setting.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = cowboy.rect.centerx
        self.rect.top = cowboy.rect.midright

        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """moves the bullet to the right on the screen"""
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """This is what draws the bullet
        to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
