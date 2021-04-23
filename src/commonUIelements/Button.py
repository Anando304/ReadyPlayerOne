##  @file Button.py
#  @author Anando Zaman
#  @brief Button create/display module
#  @date March 19, 2021

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Button:
    def add_button_to_screen(self, screen, corner_x, corner_y, length, height, color):
        button = pygame.Rect(corner_x, corner_y, length, height)
        pygame.draw.rect(screen, color, button)
        return button


