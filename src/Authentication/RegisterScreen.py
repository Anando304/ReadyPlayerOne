##  @file RegisterScreen.py
#  @author Anando Zaman
#  @brief Registration screen module
#  @date March 19, 2021


# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame

# import UI components
from commonUIelements.InputBox import InputBox
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

#def register(myfont, SCREEN_WIDTH, SCREEN_HEIGHT, screen, firebase_instance, db):
def registerScreen(register_func):

    # Logos
    logo_icon = pygame.image.load('../assets/readyplayerone.jpg')
    logo_icon = pygame.transform.scale(logo_icon, (351, 168))

    # Used for creating/displaying buttons and text
    text_display = TextDisplay()
    button_display = ButtonDisplay()

    # create input boxes
    username_box = InputBox(SCREEN_WIDTH / 2.8, SCREEN_HEIGHT / 2, screen)
    password_box = InputBox(SCREEN_WIDTH / 2.8, SCREEN_HEIGHT / 1.5, screen)
    clock = pygame.time.Clock()

    # background
    screen.fill((220, 220, 220))

    while True:

        # draw game logo
        screen.blit(logo_icon, (195, 70))

        # Draw buttons
        enter = button_display.add_button_to_screen(screen, SCREEN_WIDTH / 2.8, SCREEN_HEIGHT / 1.3, 200, 50,
                                                    (0, 120, 00))
        # Draw text
        text_display.add_to_screen(screen, 30, 'Register Screen', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20, BLACK, "arial")
        text_display.add_to_screen(screen, 30, 'Enter email', SCREEN_WIDTH / 2.1, (SCREEN_HEIGHT / 2) - 20, BLACK, "arial")
        text_display.add_to_screen(screen, 30, 'Enter password', SCREEN_WIDTH / 2.1, (SCREEN_HEIGHT / 2) + 72, BLACK, "arial")
        text_display.add_to_screen(screen, 30, 'Enter!', SCREEN_WIDTH / 2.1, (SCREEN_HEIGHT / 1.28) + 14, BLACK, "arial")

        # if made it past the previous functions, that means click is now false and the functions were terminated.
        click = False
        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:
            # handle every event
            username_box.handle_event(event)
            password_box.handle_event(event)

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    return

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # if clicked, set click flag to true
            if event.type == MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:
                    click = True

        # draw input boxes
        username_box.draw(screen, (SCREEN_WIDTH / 2.8, SCREEN_HEIGHT / 2))
        password_box.draw(screen, (SCREEN_WIDTH / 2.8, SCREEN_HEIGHT / 1.5))

        # get cursor location
        mx,my = pygame.mouse.get_pos()
        if enter.collidepoint((mx,my)):
            if click:
                print("Registration username: " + username_box.get_text())
                print("Registration password: " + password_box.get_text())

                register_status = register_func(username_box.get_text(), password_box.get_text())

                # if succuss, notify ValidationController using True
                if register_status:
                    return True

                # Otherwise display error screen
                else:
                    text_display.add_to_screen(screen, 20, 'SIGN UP FAILED', SCREEN_WIDTH / 2.05, (SCREEN_HEIGHT / 1.1), RED, "arial")
                    pygame.display.flip()


        pygame.display.flip()
        clock.tick(60)
