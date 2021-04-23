##  @file pauseScreen.py
#  @author Anando Zaman
#  @brief Generic PauseScreen module
#  @date March 19, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame

# import firebase credentials and text reader input

# import firebase credentials and text reader input
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    MOUSEBUTTONDOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


'''SETUP VARIABLES/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


'''INITIALIZE THE GAME'''
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('3A04 Game Demo')

'''INITIALIZE ICONS AND ASSETS'''
# Instantiate logo icon
logo_icon = pygame.image.load('../assets/readyplayerone.jpg')
logo_icon =  pygame.transform.scale(logo_icon, (351, 168))



'''GAME LOOP'''
# Main program loop
def pauseScreen():

    # Used for creating/displaying buttons and text
    text_display = TextDisplay()
    button_display = ButtonDisplay()

    # background
    screen.fill((220, 220, 220))

    while True:

        # draw game logo
        screen.blit(logo_icon, (195, 70))

        # Draw & create buttons
        quit = button_display.add_button_to_screen(screen, SCREEN_WIDTH / 1.9, SCREEN_HEIGHT / 1.75, 200, 50,
                                                    RED)
        resume = button_display.add_button_to_screen(screen, SCREEN_WIDTH / 5.4, SCREEN_HEIGHT / 1.75, 200, 50,
                                                              (0, 128, 0))
        instructions = button_display.add_button_to_screen(screen, SCREEN_WIDTH / 2.8, (SCREEN_HEIGHT / 1.75) + 68, 200, 50,
                                                              (255,127,80))

        # Draw text
        text_display.add_to_screen(screen, 30, 'GAME PAUSED', SCREEN_WIDTH / 2.15, SCREEN_HEIGHT / 20, BLACK, "arial")
        text_display.add_to_screen(screen, 30, 'Resume', SCREEN_WIDTH / 3.2, (SCREEN_HEIGHT / 1.75) + 18, BLACK, "arial")
        text_display.add_to_screen(screen, 30, 'Quit', SCREEN_WIDTH / 1.54, (SCREEN_HEIGHT / 1.75) + 18, BLACK, "arial")
        text_display.add_to_screen(screen, 30,'Instructions', SCREEN_WIDTH / 2.08, (SCREEN_HEIGHT / 1.75) + 88, BLACK, "arial")

        # if made it past the previous functions, that means click is now false and the functions were terminated.
        click = False
        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # if clicked, set click flag to true
            if event.type == MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:
                    click = True


        # get cursor location
        mx,my = pygame.mouse.get_pos()

        # if login button pressed
        if resume.collidepoint((mx,my)):
            if click:
                print("resume")
                return "resume"

        # if login button pressed
        elif instructions.collidepoint((mx,my)):
            if click:
                print("instruction")
                return "instruction"


        # if register button pressed
        elif quit.collidepoint((mx, my)):
            if click:
                print("quit")
                return "quit"


        pygame.display.update()

#if __name__ == '__main__':
#    pauseScreen()