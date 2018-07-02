# This is part of my answer to Python Crash Course
# Chapter 12 exercise 5
import pygame

class Cowboy:
  def __init__(self, ai_settings, screen):
      """This initializes cowboy"""
      self.screen = screen
      self.ai_settings = ai_settings

      # need to upload the cowboy image
      # that i hand drew in old fashioned paint
      self.image = pygame.image.load('cowboy.bmp')
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()

      # I'm going to start the cowboy in the middle
      # and make him stay on the left of the screen
      self.centery = self.screen_rect.centery
      self.rect.left = self.screen_rect.left

      # now i need a movement flag
      self.moving_up = False
      self.moving_down = False

      self.cowboy_speed_factor = 1

def update(self):
    """This is to update the cowboy's position"""
    if self.moving_up and self.rect.top < self.screen_rect.top:
        self.center += self.ai_settings.cowboy_speed_factor
    elif self.moving.down and self.rect.bottom > 0:
        self.center -= self.ai_settings.cowboy_speed_factor

    self.rect.centery = self.center

def blitme(self):
    """Drawing the cowboy at his current location"""
    self.screen.blit(self.image, self.rect)
