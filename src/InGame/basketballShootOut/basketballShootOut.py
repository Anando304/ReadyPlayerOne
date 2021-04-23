##  @file basketballShootOut.py
#  @author Anando Zaman
#  @brief Basketball shootout gameplay module
#  @date March 19, 2021

# Import the pygame module
import sys
sys.path.insert(0, './')
import pygame
from commonUIelements.timer import timer as timer

# import UI components
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay
from InGame.basketballShootOut.Player import Player
from InGame.basketballShootOut.net import net

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
myfont = pygame.font.SysFont('freesansbold.ttf', 30)
pygame.display.set_caption('3A04 Game Demo')

# Initialize objects
ball_net = net()
player = Player()
countdown = timer(30)
clock = pygame.time.Clock()

# Initialize text
text_display = TextDisplay()
button_display = ButtonDisplay()

def startGame(UpdateLocalHighScore, UpdateGlobalHighScore, runningState):

    # if game restarted externally by GameStateController
    if not runningState:
        runningState = True
        player.shoot = False
        player.restart_game()
        ball_net.restart_game()
        countdown.restart_timer()

    # game execution loop
    while runningState:
        click = False
        # background
        screen.fill((220, 220, 220))

        # pause button
        pause = button_display.add_button_to_screen(screen, 0, 0, 100, 50, (177, 0, 0))
        text_display.add_to_screen(screen, 30, "Pause", 33, 28, BLACK, "freesansbold.ttf")

        # TIMER COUNTDOWN
        total_seconds = countdown.count_down(screen, myfont, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Look at every event in the queue
        events = pygame.event.get()
        for event in events:

            # Did the user hit a key?
            if event.type == KEYDOWN:
                # NEED to CHANGE such that it displays the pause screen
                if event.key == K_ESCAPE:
                    print("pause button pressed")
                    return "pause"

                # Player shoots the ball
                if (event.key == K_SPACE or event.key == K_UP) and total_seconds > 0 and player.get_balls_remaining() > 0:
                    player.shoot = True

                # if game ended, and wants to restart!
                elif (event.key == K_SPACE or event.key == K_UP):
                    player.shoot = True
                    player.restart_game()
                    ball_net.restart_game()
                    countdown.restart_timer()

                # update player throwing position
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

        # isGameOver
        if total_seconds <= 0 or player.balls_left <= 0:

            # move net back to default location
            ball_net.default_position()

            # update users' current highscore if applicable and return the score
            current_score = player.get_score()
            user_highscore = UpdateLocalHighScore(current_score)

            # update global highscore
            global_highscore_user, global_highscore = UpdateGlobalHighScore(user_highscore)

            # Display score information
            text_display.add_to_screen(screen, 30, "Global Highscore: " + str(global_highscore), SCREEN_WIDTH / 1.18, SCREEN_HEIGHT / SCREEN_HEIGHT + 50, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(screen, 30, "Global Highscore User: " + global_highscore_user, SCREEN_WIDTH / 1.28,SCREEN_HEIGHT / SCREEN_HEIGHT + 80, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(screen, 40, "Game Over!", SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 1.05, BLACK, "freesansbold.ttf")

        # move net left & right
        if total_seconds > 0:
            ball_net.move()


        # check if player shot the ball
        if player.shoot:
            player.shoot_ball()

        # check if ball hit the net
        if player.rect.colliderect(ball_net.rect) and total_seconds > 0:
            player.increment_score()
            print("COLLIDED")
            # reset flag
            player.shoot = False
            # reset position for next shot
            player.reset_position()
            # increase difficulty
            ball_net.increase_speed()

        # Draw to the screen
        # player.rect lets us move the player dynamically based on its rect coordinates
        screen.blit(player.surf, player.rect)
        screen.blit(ball_net.surf, ball_net.rect)
        # display remaining balls and score!
        text_display.add_to_screen(screen, 40, "Balls: " + str(player.get_balls_remaining()), SCREEN_WIDTH / 1.2, SCREEN_HEIGHT / 1.05, BLACK, "freesansbold.ttf")
        text_display.add_to_screen(screen, 30, "Your Score: " + str(player.get_score()), SCREEN_WIDTH / 1.18, SCREEN_HEIGHT / SCREEN_HEIGHT + 110, BLACK, "freesansbold.ttf")

        pygame.display.update()
        clock.tick(30)
