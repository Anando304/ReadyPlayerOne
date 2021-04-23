## @file AlienLaser.py
# @author David Yao
# @brief Space Invaders Alien Laser projectile module
# @date April 13, 2021
import pygame

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition):
        super(AlienLaser, self).__init__()
        alienLaser_icon = pygame.image.load('../assets/alienlaser.png')
        self.surf = alienLaser_icon
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = xPosition - 5, yPosition

    def move(self):
        self.rect.move_ip(0,7)
