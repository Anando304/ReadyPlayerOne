## @file InputBox.py
#  @author Anando Zaman
#  @brief InputBox for user input module
#  @date March 19, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame

class InputBox():

    def __init__(self, x, y, screen):

        self.font = pygame.font.Font(None, 28)

        self.inputBox = pygame.Rect(x, y, 140, 32)

        self.colourInactive = pygame.Color('lightskyblue3')
        self.colourActive = pygame.Color('dodgerblue2')
        self.colour = self.colourInactive

        self.screen = screen

        self.text = ''

        self.active = False
        self.isBlue = True

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    temp = self.text
                    print(self.text)
                    #self.text = ''
                    return temp

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.screen.fill((220, 220, 220))
                    # This is required so that we can update the backspace viewings
                    # we must only have one display.update() but does cause flickering!
                    pygame.display.update()
                else:
                    self.text += event.unicode

    def get_text(self):
        return self.text

    def draw(self, screen, position):
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(236, txtSurface.get_width()+10)
        self.inputBox.w = width
        screen.blit(txtSurface, position)
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)

        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)