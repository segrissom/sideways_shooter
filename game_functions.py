# this is a part of my answer to Python Crash Course
# Chapter 12 exercise 5
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, cowboy):
  """This is what responds to the keypresses"""
  if event.key == pygame.K_UP:
    cowboy.moving_up = True
  elif event.key == pygame.K_DOWN:
    cowboy.moving_down = True
  elif event.key == pygame.K_SPACE:
    fire_bullet(ai_settings, screen, cowboy, bullet)

def fire_bullet(ai_settings, screen, cowboy, bullets):
    """This fires a bullet granted that the
    limit hasn't been reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, cowboy)
        bullets.add(new_bullet)

def check_keyup_events(event, cowboy):
    """This is what responds when you
    release the key"""
    if event.key == pygame.K_UP:
        cowboy.moving_up = False
    elif event.key == pygame.K_DOWN:
        cowboy.moving_down = False

def check_events():
    """This reponds to key presses in general
    and mouse events"""
    screen.fill(background_color)
    cowboy.blitme()
    # need to redraw the bullets since they are moving
    for bullet in bullets.sprite():
        bullet.draw_bullet()
    # need to make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """This function updates the bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 12
            bullets.remove(bullet)
