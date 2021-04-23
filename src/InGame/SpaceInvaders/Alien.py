## @file Alien.py
# @author David Yao
# @brief Space Invaders Alien module
# @date April 13, 2021
import pygame

# Constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Alien(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition):
        super(Alien, self).__init__()
        alien_icon = pygame.image.load('../assets/alien.png')
        self.surf = alien_icon
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = xPosition, yPosition

    def stay_within_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= SCREEN_HEIGHT/10:
            self.rect.top = SCREEN_HEIGHT/10
        if self.rect.bottom >= SCREEN_HEIGHT - SCREEN_HEIGHT/6:
            self.rect.bottom = SCREEN_HEIGHT - SCREEN_HEIGHT/6

    def move(self, xDelta, yDelta):
        self.rect.move_ip(xDelta, yDelta)
        
        self.stay_within_bounds()