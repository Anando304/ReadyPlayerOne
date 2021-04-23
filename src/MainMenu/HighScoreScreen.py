##  @file HighScoreScreen.py
#  @author Anando Zaman
#  @brief Highscore screen view/display module
#  @date March 19, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame

# import firebase credentials and text reader input
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay

from pygame.locals import (
    MOUSEBUTTONDOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)
RED = (255, 0, 0)

'''SETUP VARIABLES/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


'''INITIALIZE THE GAME'''
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('arial', 30)
pygame.display.set_caption('3A04 Game Demo')

# game homescreen with score
def HighScoreScreen(GetGameList, GetScoreList):

    # text and button initalization
    text_display = TextDisplay()
    button_display = ButtonDisplay()

    # get games and score list
    gamesList, getScoreList = GetGameList(), GetScoreList()

    running = True
    while running:
        click = False
        screen.fill((220, 220, 220))

        # create back and score viewing buttons
        back = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))

        # draw text for buttons
        text_display.add_to_screen(screen, 30, "Back", 33, 28, BLACK, "freesansbold.ttf")
        text_display.add_to_screen(screen, 30, "HighScore View", SCREEN_WIDTH/2, 100, BLACK, "freesansbold.ttf")

        # draw text for scores of each game, repeat for each game
        width, height = 400, 150
        for game in getScoreList:
            text_display.add_to_screen(screen, 30, "GAME: " + game +", USER: " + list(getScoreList[game].keys())[0] + ", SCORE: " + str(list((getScoreList[game]).values())[0]), width, height, BLACK, "freesansbold.ttf")
            height += 50

        events = pygame.event.get()
        for event in events:

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

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


        # Cursor location
        mx, my = pygame.mouse.get_pos()

        # back pressed
        if back.collidepoint((mx, my)):
            if click:
                print("back button pressed")
                running = False
                return "back_button"

        pygame.display.update()