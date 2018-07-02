# This is part of my solution to the Python Crash Course
# Chapter 12 exercise 5


class Settings:
    """A class to store all of the settings
    for my sideways shooter"""
    self.screen_width = 1200
    self.screen_height = 1200
    self.bg_color = (255, 250, 205)

    # Bullet settings
    self.bullet_speed_factor = 1
    self.bullet_width = 2
    self.bullet_height = 8
    self.bullet_color = 60, 60, 60
    self.bullets_allowed = 5
