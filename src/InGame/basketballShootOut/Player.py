##  @file Player.py
#  @author Anando Zaman
#  @brief Player character/ball module
#  @date March 19, 2021

import pygame

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
        ball_icon = pygame.image.load('../assets/ball.png')
        ball_icon = pygame.transform.scale(ball_icon, (40, 40))
        self.defaultx, self.defaulty = SCREEN_WIDTH / 2.68, SCREEN_HEIGHT / 1.2
        self.surf = ball_icon
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = self.defaultx, self.defaulty
        self.shoot = False
        self.balls_left = 3
        self.curr_score = 0

    def reset_position(self):
        self.rect.x, self.rect.y = self.defaultx, self.defaulty

    def restart_game(self):
        self.reset_position()
        self.balls_left = 3
        self.shoot = False
        self.curr_score = 0

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

    # Move the sprite based on user keypresses
    def move(self, pressed_keys):

        # move left and right unless ball has already been shot
        if pressed_keys == K_LEFT and not self.shoot:
            self.rect.move_ip(-30, 0)
        if pressed_keys == K_RIGHT and not self.shoot:
            self.rect.move_ip(30, 0)

        # Keep player on the screen
        self.stay_within_bounds()

    def shoot_ball(self):
        # launch ball:
        self.rect.y -= 20

        # if misses and goes out of bounds
        if self.rect.y <= 0:
            self.balls_left -= 1
            self.reset_position()
            self.shoot = False

        # Keep player on the screen
        self.stay_within_bounds()

    def get_balls_remaining(self):
        return self.balls_left

    def get_score(self):
        return self.curr_score

    def increment_score(self):
        self.curr_score += 1