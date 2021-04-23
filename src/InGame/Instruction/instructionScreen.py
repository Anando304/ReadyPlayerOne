##  @file InstructionScreen.py
#  @author Anando Zaman
#  @brief Generic PauseScreen module
#  @date March 27, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame

# import UI components
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

# Used for creating/displaying buttons and text
text_display = TextDisplay()
button_display = ButtonDisplay()

def instruction_basketball():
    text_display.add_to_screen(screen, 20,
                               'BASKETBALL SHOOTOUT',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) -8, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'Objective is to get as many points by shooting the ball before the time runs out!', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 18, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'Move left and right using the left and right arrow keyboard keys. Use Space button to launch!', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 48, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'There is a total of 3 balls. If you miss the net, a ball will be deducted.', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 78, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'Game ends when time expires OR if the number of available balls becomes zero', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 108, BLACK,
                               "arial")

# TODO Below methods need to be completed with instructions TEXT
def instruction_dodge():
    text_display.add_to_screen(screen, 20,
                               'DODGE',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) -8, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Objective is to dodge cars, each car dodged gets 1 point.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 18, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Move left and right using the left and right arrow keyboard keys.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 48, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'The game ends when you crash, so survive as long as possible!',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 78, BLACK,
                               "arial")

def instruction_spaceinvader():
    text_display.add_to_screen(screen, 20,
                               'SPACE INVADERS',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) -8, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Objective is to destroy as many aliens as possible before running out of health.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 18, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Use the arrow keys to move, and space to shoot.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 48, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Avoid the alien attacks and do not crash into them! You cannot survive a crash.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 78, BLACK,
                               "arial")

def instruction_flappybird():
    text_display.add_to_screen(screen, 20,
                               'FLAPPYBIRD',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) -8, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Objective is to avoid the pipes and go through as many as possible.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 18, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'Hit space bar to jump or flutter.',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 48, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20,
                               'The game ends when you crash, so survive as long as possible!',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 78, BLACK,
                               "arial")

def instruction_fruitninja():
    text_display.add_to_screen(screen, 20,
                               'FRUIT NINJA',
                               SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) -8, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'Objective is to cut as many fruites before the time runs out!', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 18, BLACK,
                               "arial")
    text_display.add_to_screen(screen, 20, 'Place your mose on the screen as a knife to cut fruites', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 48, BLACK,"arial")
    text_display.add_to_screen(screen, 20, 'Game ends when time expires', SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 1.75) + 108, BLACK,
                               "arial")



'''GAME LOOP'''
# Main program loop
def instructionScreen(game):

    # background
    screen.fill((220, 220, 220))

    while True:

        # draw game logo
        screen.blit(logo_icon, (195, 70))

        # back viewing buttons
        back = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))

        # draw text
        text_display.add_to_screen(screen, 30, 'Instructions', SCREEN_WIDTH / 2.15, SCREEN_HEIGHT / 20, BLACK, "arial")
        text_display.add_to_screen(screen, 30, "Back", 33, 28, BLACK, "freesansbold.ttf")

        # draw instruction text for the specific game
        if game.lower().strip() == "basketball":
            instruction_basketball()

        elif game.lower().strip() == "dodge":
            instruction_dodge()

        elif game.lower().strip() == "spaceinvader":
            instruction_spaceinvader()

        elif game.lower().strip() == "flappybird":
            instruction_flappybird()

        elif game.lower().strip() == "fruitninja":
            instruction_fruitninja()

        # if made it past the previous functions, that means click is now false and the functions were terminated.
        click = False
        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    print("back")
                    return "back"

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
        if back.collidepoint((mx,my)):
            if click:
                print("back")
                return "back"


        pygame.display.update()
