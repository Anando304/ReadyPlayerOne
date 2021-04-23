## @file SpaceInvaders.py
# @author David Yao
# @brief Space Invaders gameplay module
# @date April 13, 2021
import sys
import pygame
import random

sys.path.insert(0, './')

# UI components
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay

# Other objects
from InGame.SpaceInvaders.Player import Player
from InGame.SpaceInvaders.Alien import Alien
from InGame.SpaceInvaders.Laser import Laser
from InGame.SpaceInvaders.AlienLaser import AlienLaser

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    MOUSEBUTTONDOWN
)

# Setup constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
XOFFSET = 50
YOFFSET = 50

# Display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize game
pygame.init()
pygame.font.init()

# Initialize text
myfont = pygame.font.SysFont('freesansbold.ttf', 30)
pygame.display.set_caption('3A04 Game Demo')
text_display = TextDisplay()
button_display = ButtonDisplay()

# Initialize objects
player = Player()
clock = pygame.time.Clock()
stars = pygame.image.load('../assets/stars.png')

# Initialize variables
finished = False
score_updated = False

score = 0
playerSpeed = 5

aliens = []
lasers = []
alienLasers = []

global_highscore, global_highscore_user = None, None

def startGame(UpdateLocalHighScore, UpdateGlobalHighScore, runningState):
    global finished, score_updated, score, playerSpeed, aliens, lasers, alienLasers, global_highscore, global_highscore_user

    keysDown = []

    # Reset game state
    if not runningState:
        runningState = True
        reset_game_state()

    while runningState:
        click = False

        # Display background
        screen.blit(stars, (0, 0))

        # Display pause button
        pause = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))
        text_display.add_to_screen(screen, 30, "Pause", 33, 28, BLACK, "freesansbold.ttf")

        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:

            # Key hit?
            if event.type == KEYDOWN:

                # Pause game
                if event.key == K_ESCAPE:
                    print("pause button pressed")
                    return "pause"

                # Movement key
                elif event.key in {K_LEFT, K_RIGHT, K_UP, K_DOWN}:
                    keysDown.append(event.key)

                # Shoot
                elif event.key == K_SPACE and not finished:
                    lasers.append(Laser(player.rect.centerx, player.rect.centery))
                
                # Reset game state
                elif event.key == K_SPACE and finished:
                    reset_game_state()

            # Released movement key
            elif event.type == KEYUP and event.key in keysDown:
                keysDown.remove(event.key)
                

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

        # Pause pressed
        if pause.collidepoint((mx, my)):
            if click:
                print("pause button pressed")
                return "pause"

        # Move and interact with everything on screen
        if not finished:

            #Player movement
            for key in keysDown:
                player.move(key, playerSpeed)
                if player.rect.collidelist(aliens) > -1:
                    player.health = 0

            # Movement, shooting, drawing for each alien
            for alien in aliens:
                alien.move(random.randint(-5,5),random.randint(-5,5))
                shotChance = random.randint(1,240)
                if shotChance == 1:
                    alienLasers.append(AlienLaser(alien.rect.centerx, alien.rect.centery))
                alien.move(0,0)
                screen.blit(alien.surf, alien.rect)
            
            # Spawn more aliens if wiped out
            if len(aliens) == 0:
                for i in range(8):
                    aliens.append(Alien((SCREEN_WIDTH*i/10)+XOFFSET, (SCREEN_HEIGHT/10)))
                    aliens.append(Alien((SCREEN_WIDTH*i/10)+XOFFSET*2, (SCREEN_HEIGHT/10)+YOFFSET))
                    aliens.append(Alien((SCREEN_WIDTH*i/10)+XOFFSET, (SCREEN_HEIGHT/10)+YOFFSET*2))

            # Movement, collision, drawing for each laser
            for laser in lasers:
                laser.move()
                index = laser.rect.collidelist(aliens)
                if index > -1:
                    score += 1
                    lasers.remove(laser)
                    aliens.remove(aliens[index])
                if laser.rect.y < 0:
                    lasers.remove(laser)
                screen.blit(laser.surf, laser.rect)

            # Movement, collision, drawing for each alien laser
            for alienLaser in alienLasers:
                alienLaser.move()
                if alienLaser.rect.colliderect(player.rect):
                    player.health -= 1
                    alienLasers.remove(alienLaser)
                if alienLaser.rect.y > SCREEN_HEIGHT:
                    alienLasers.remove(alienLaser)
                screen.blit(alienLaser.surf, alienLaser.rect)

        # If player dies, game over
        if player.health < 1:
            finished = True
            if not score_updated:

                # update users' current highscore if applicable and return the score
                user_highscore = UpdateLocalHighScore(score)

                # # update global highscore
                global_highscore_user, global_highscore = UpdateGlobalHighScore(user_highscore)
                score_updated = True

            # # Display score information
            text_display.add_to_screen(screen, 30, "Global Highscore: " + str(global_highscore), SCREEN_WIDTH / 1.18 + 10, SCREEN_HEIGHT / SCREEN_HEIGHT + 80, WHITE, "freesansbold.ttf")
            text_display.add_to_screen(screen, 30, "User: " + global_highscore_user, SCREEN_WIDTH / 1.18 + 5,SCREEN_HEIGHT / SCREEN_HEIGHT + 110, WHITE, "freesansbold.ttf")
            text_display.add_to_screen(screen, 40, "Game Over!", 400, 40, WHITE, "freesansbold.ttf")
            text_display.add_to_screen(screen, 35, "Press Space To Play Again", 400, 80, WHITE, "freesansbold.ttf")

        # Display score and lives
        text_display.add_to_screen(screen, 30, "Score: " + str(score), SCREEN_WIDTH / 1.18, SCREEN_HEIGHT / SCREEN_HEIGHT + 15, WHITE, "freesansbold.ttf")
        text_display.add_to_screen(screen, 30, "Health: " + str(player.health), SCREEN_WIDTH / 1.18, SCREEN_HEIGHT / SCREEN_HEIGHT + 40, WHITE, "freesansbold.ttf")
        
        # Draw player on top of everything
        screen.blit(player.surf, player.rect)

        pygame.display.update()

        clock.tick(60)

def reset_game_state():
    global finished, score_updated, score, aliens, lasers, alienLasers
    player.reset_state()

    finished = False
    score_updated = False
    score = 0
    aliens = []
    alienLasers = []
    lasers = []