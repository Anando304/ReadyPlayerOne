##  @file timer.py
#  @author Anando Zaman
#  @brief Timer countdown display module
#  @date March 19, 2021

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)

class timer(pygame.sprite.Sprite):
    def __init__(self, start_time):
        super(timer, self).__init__()
        self.frame_count = 0
        self.frame_rate = 30
        self.original_time = start_time
        self.start_time = start_time

    def count_down(self, screen, myfont, SCREEN_WIDTH, SCREEN_HEIGHT):
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = self.frame_count // self.frame_rate

        # --- Timer going down ---
        # Calculate total seconds
        total_seconds = self.start_time - (self.frame_count // self.frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0}".format(total_seconds)
        text = myfont.render(output_string, True, BLACK)
        screen.blit(text, [SCREEN_WIDTH /1.3, SCREEN_HEIGHT / SCREEN_HEIGHT + 10])

        self.frame_count += 1

        return total_seconds

    def restart_timer(self):
        self.start_time = self.original_time
        self.frame_count = 0