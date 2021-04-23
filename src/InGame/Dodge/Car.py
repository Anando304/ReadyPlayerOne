import pygame
import os

'''SETUP CONSTANTS/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Car(pygame.sprite.Sprite):
    def __init__(self,  position, speed):
        super(Car, self).__init__()
        base_path = os.path.dirname(__file__)
        car = pygame.image.load(os.path.join(base_path, "../../assets/taxi.png"))
        car = pygame.transform.scale(car, (100, 200))
        self.surf = car
        self.rect = self.surf.get_rect()
        self.speed = speed
        
        self.rect.x, self.rect.y = SCREEN_WIDTH/2 - 50 + (position*120), -200

    # Move the sprite based on user keypresses
    def move(self):
        self.rect.y += self.speed
