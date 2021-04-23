##  @file Text.py
#  @author Anando Zaman
#  @brief TextDisplay to screen module
#  @date March 19, 2021

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Text:
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def add_to_screen(self, screen, font_size, text, center_x, center_y, color, font_name):
        largeText = pygame.font.SysFont(font_name, font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, color)
        TextRect.center = (center_x, center_y)
        screen.blit(TextSurf, TextRect)
