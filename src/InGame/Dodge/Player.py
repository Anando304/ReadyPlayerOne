##  @file Player.py
#  @author Tamas Leung
#  @brief Player character
#  @date March 23, 2021

import pygame
import os

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)


'''SETUP CONSTANTS/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player and ball position
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        base_path = os.path.dirname(__file__)
        
        car = pygame.image.load(os.path.join(base_path, "../../assets/car.png"))
        car = pygame.transform.scale(car, (100, 200))
        
        self.defaultx, self.defaulty = SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 200
        self.surf = car
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = self.defaultx, self.defaulty
        self.curr_score = 0

    def reset_position(self):
        self.rect.x, self.rect.y = self.defaultx, self.defaulty

    def stay_within_bounds(self):
        # Keep player on the screen
        if self.rect.x < SCREEN_WIDTH / 2 - 50 - 120:
            self.rect.x = SCREEN_WIDTH / 2 - 50 - 120
        if self.rect.x > SCREEN_WIDTH / 2 - 50 + 120:
            self.rect.x = SCREEN_WIDTH / 2 - 50 + 120

    # Move the sprite based on user keypresses
    def move(self, pressed_keys):

        # move left and right unless ball has already been shot
        if pressed_keys == K_LEFT:
            self.rect.move_ip(-120, 0)
        if pressed_keys == K_RIGHT:
            self.rect.move_ip(+120, 0)

        # Keep player on the screen
        self.stay_within_bounds()
