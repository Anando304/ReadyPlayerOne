##  @file net.py
#  @author Anando Zaman
#  @brief Basketball net object module
#  @date March 19, 2021

import pygame
import sys
sys.path.insert(0, './')

'''SETUP CONSTANTS/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class net(pygame.sprite.Sprite):
    def __init__(self):
        super(net, self).__init__()
        net_icon = pygame.image.load('../assets/ballnet.png')
        net_icon = pygame.transform.scale(net_icon, (90, 90))
        self.surf = net_icon
        #self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.speedx = 2

    def default_position(self):
        self.rect.x = SCREEN_WIDTH/2

    def restart_game(self):
        self.default_position()
        self.speedx = 2

    def move(self):
        if self.rect.left <= 0:
            self.speedx = abs(self.speedx)
        elif self.rect.right >= SCREEN_WIDTH:
            self.speedx = -abs(self.speedx)
        self.rect.x += self.speedx

    def increase_speed(self):
        print(self.speedx)
        if abs(self.speedx) <16:
            self.speedx *= 2
