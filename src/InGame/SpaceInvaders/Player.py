## @file Player.py
# @author David Yao
# @brief Space Invaders Player module
# @date April 13, 2021
import pygame

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
)

from InGame.SpaceInvaders.Laser import Laser

# Constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        ship_icon = pygame.image.load('../assets/spaceship.png')
        self.defaultx, self.defaulty = SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50
        self.surf = ship_icon
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = self.defaultx, self.defaulty
        self.health = 3
        
    def reset_state(self):
        self.rect.x, self.rect.y = self.defaultx, self.defaulty
        self.health = 3

    def stay_within_bounds(self):
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def move(self, pressed_keys, speed):
        if pressed_keys == K_LEFT:
            self.rect.move_ip(-speed, 0)
        if pressed_keys == K_RIGHT:
            self.rect.move_ip(speed, 0)
        if pressed_keys == K_UP:
            self.rect.move_ip(0, -speed)
        if pressed_keys == K_DOWN:
            self.rect.move_ip(0, speed)
        
        self.stay_within_bounds()

