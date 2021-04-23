##  @file defender.py
#  @author Tamas Leung
#  @brief Defender gameplay module
#  @date March 19, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame
import random
import os

# import UI components
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay
from InGame.Dodge.Player import Player
from InGame.Dodge.Car import Car


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)


'''SETUP CONSTANTS/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


'''INITIALIZE THE GAME'''
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('freesansbold.ttf', 30)
pygame.display.set_caption('3A04 Game Demo')

# Initialize text
text_display = TextDisplay()
button_display = ButtonDisplay()

base_path = os.path.dirname(__file__)
road = pygame.image.load(os.path.join(base_path, "../../assets/road.png"))

finished = False
cars = []
score = 0
currentSpeed = 10
maxSpeed = 20
road_y = 0
score_updated = False

# Initialize objects
player = Player()

#TODO: Bug with resuming the game. The gamescore resets even though it should continue from where it left off.
def startGame(UpdateLocalHighScore, UpdateGlobalHighScore, runningState):
    
    global finished, cars, score, currentSpeed, maxSpeed, road_y
    # if game restarted externally by GameStateController
    if not runningState:
        runningState = True
        finished = False
        cars = []
        score = 0
        currentSpeed = 10
        maxSpeed = 20
        road_y = 0

    score_updated = False
    # else:
    #     cars = []
    #     finished = False
    #     score = 0
    #     currentSpeed = 10
    #     maxSpeed = 20
    #     road_y = 0
    #     score_updated = False

    # game execution loop
    while runningState:
        

        click = False
        if not finished:
            for car in cars[:]:
                car.move()
                if car.rect.y > SCREEN_HEIGHT + currentSpeed:
                    cars.remove(car)
                    score += 1
                    if currentSpeed < maxSpeed:
                        currentSpeed += 0.5
            road_y += 3
            if road_y > 200:
                road_y = road_y % 200
        

        if len(cars) < 1:
            number_of_cars = random.randint(1, 2)
            positions = random.sample(range(-1, 2), number_of_cars)
            for pos in positions:
                cars.append(Car(pos, currentSpeed))
        
        # background
        screen.fill((220, 220, 220))
        screen.blit(road, (0, -200 + road_y))

        

        # isGameOver
        if finished:

            if not score_updated:

                # update users' current highscore if applicable and return the score
                user_highscore = UpdateLocalHighScore(score)

                # # update global highscore
                global_highscore_user, global_highscore = UpdateGlobalHighScore(user_highscore)
                score_updated = True

            # # Display score information
            text_display.add_to_screen(screen, 30, "Global Highscore: " + str(global_highscore), SCREEN_WIDTH / 1.18 + 10, SCREEN_HEIGHT / SCREEN_HEIGHT + 50, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(screen, 30, "User: " + global_highscore_user, SCREEN_WIDTH / 1.18 + 5,SCREEN_HEIGHT / SCREEN_HEIGHT + 80, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(screen, 40, "Game Over!", 400, 40, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(screen, 35, "Press Space To Play Again", 400, 80, BLACK, "freesansbold.ttf")

        # pause button
        pause = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))
        text_display.add_to_screen(screen, 30, "Pause", 33, 28, BLACK, "freesansbold.ttf")

        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:

            # Did the user hit a key?
            if event.type == KEYDOWN:
                if finished:
                    if event.key == K_SPACE:
                        player.reset_position()
                        score = 0
                        finished = False
                        cars = []
                        currentSpeed = 5
                        score_updated = False
                else:

                    if event.key == K_ESCAPE:
                        print("pause button pressed")
                        return "pause"

                    player.move(event.key)

            # if clicked, set click flag to true
            if event.type == MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:
                    click = True

            # Did the user click the window close button? If so, stop the loop.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Cursor location
        mx, my = pygame.mouse.get_pos()
        # back pressed
        if pause.collidepoint((mx, my)):
            if click:
                print("pause button pressed")
                return "pause"

        if not finished:
            for car in cars:
                if player.rect.colliderect(car.rect):
                    finished = True

        # Draw to the screen
        # player.rect lets us move the player dynamically based on its rect coordinates
        screen.blit(player.surf, player.rect)
        for car in cars:
            screen.blit(car.surf, car.rect)
        # display score!
        text_display.add_to_screen(screen, 30, "Your Score: " + str(score), SCREEN_WIDTH / 1.18, SCREEN_HEIGHT / SCREEN_HEIGHT + 110, BLACK, "freesansbold.ttf")

        pygame.display.update()
        clock.tick(60)
