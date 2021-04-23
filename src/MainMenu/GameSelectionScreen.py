##  @file GameSelectionScreen.py
#  @author Anando Zaman
#  @brief Displays the available games and allows the user to select the game of their choice
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

'''INITIALIZE ICONS AND ASSETS'''
# Instantiate logo icon
logo_icon = pygame.image.load('../assets/puzzlerama.png')
logo_icon =  pygame.transform.scale(logo_icon, (351, 168))

# game homescreen with score
def GameSelectionScreen():

    # instantiate button logos, better to make class button images after!
    flappybird = pygame.image.load('../assets/flappybird.png')
    dodge = pygame.image.load('../assets/dodge.png')
    basketball = pygame.image.load('../assets/ball.png')
    fruitninja = pygame.image.load('../assets/fruitninja.png')
    spaceinvaders = pygame.image.load('../assets/spaceinvaders.png')

    # scale the images down
    flappybird = pygame.transform.scale(flappybird, (100, 100))
    dodge = pygame.transform.scale(dodge, (160, 100))
    basketball = pygame.transform.scale(basketball, (100, 100))
    fruitninja = pygame.transform.scale(fruitninja, (140, 140))
    spaceinvaders = pygame.transform.scale(spaceinvaders, (140, 140))

    # change their location
    flappybird_rect = flappybird.get_rect()
    flappybird_rect.x, flappybird_rect.y = 100, 200

    dodge_rect = dodge.get_rect()
    dodge_rect.x, dodge_rect.y = 300, 200

    basketball_rect = basketball.get_rect()
    basketball_rect.x, basketball_rect.y = 200, 370

    fruitninja_rect = fruitninja.get_rect()
    fruitninja_rect.x, fruitninja_rect.y = 600, 200

    spaceinvaders_rect = spaceinvaders.get_rect()
    spaceinvaders_rect.x, spaceinvaders_rect.y = 470, 370

    text_display = TextDisplay()
    button_display = ButtonDisplay()

    running = True
    while running:
        click = False
        screen.fill((220, 220, 220))

        # create back and score viewing buttons
        back = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))
        score_button = button_display.add_button_to_screen(screen, SCREEN_WIDTH-100,0,100,50,(255,255,0))

        # draw text
        text_display.add_to_screen(screen, 30, "Back", 33, 28, BLACK, "freesansbold.ttf")
        text_display.add_to_screen(screen, 30, "Score", SCREEN_WIDTH-48, 28, BLACK, "freesansbold.ttf")
        text_display.add_to_screen(screen, 30, "Main Menu - Game Selection", SCREEN_WIDTH/2, 100, BLACK, "freesansbold.ttf")

        # draw button logos
        screen.blit(flappybird, flappybird_rect)
        screen.blit(dodge, dodge_rect)
        screen.blit(basketball, basketball_rect)
        screen.blit(fruitninja, fruitninja_rect)
        screen.blit(spaceinvaders, spaceinvaders_rect)

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

        elif score_button.collidepoint((mx, my)):
            if click:
                print("score button pressed")
                return "score_button"

        # return name of game pressed to controller
        elif basketball_rect.collidepoint((mx,my)):
            if click:
                print("Basketball Shootout selected")
                return "BasketballShootOut"

        elif dodge_rect.collidepoint((mx,my)):
            if click:
                print("Dodge selected")
                return "Dodge"
        elif flappybird_rect.collidepoint((mx,my)):
            if click:
                print("FlappyBird selected")
                return "FlappyBird"
        elif fruitninja_rect.collidepoint((mx,my)):
            if click:
                print("fruitninja_rect selected")
                return "fruitninja"
        elif spaceinvaders_rect.collidepoint((mx,my)):
            if click:
                print("spaceinvaders_rect selected")
                return "SpaceInvaders"

        pygame.display.update()
