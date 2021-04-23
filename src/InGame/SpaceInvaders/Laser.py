## @file Laser.py
# @author David Yao
# @brief Space Invaders Laser projectile module
# @date April 13, 2021
import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition):
        super(Laser, self).__init__()
        laser_icon = pygame.image.load('../assets/laser.png')
        self.surf = laser_icon
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = xPosition - 5, yPosition

    def move(self):
        self.rect.move_ip(0,-20)
