# this is my result for the sideways shooter for Python Crash Course Chapter
# 12 exercise 5
# i will be making a sideways shooter and it will be a cowboy

import pygame
from pygame.sprite import Group
from settings import Settings
from cowboy import Cowboy
import game_functions as gf

def run_game():
    # need to Initialize the screen
    pygame.init()
    screen = pygame.display.set_mode((1200,1200))
    pygame.display.set_caption("Cowboy Shoot 'Em")

    # making our Cowboy
    cowboy = Cowboy(ai_settings, screen)

    # make a group to store the bullets in
    bullets = Group()

    # Setting a background background color
    background_color = (255, 250, 205)

    while True:
        gf.check_events(cowboy, ai_settings, screen, bullets)
        cowboy.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
