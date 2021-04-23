## @file fruitNinjia.py
#  @author Qiushi Xu
#  @brief FruitNinjia module
#  @date April 12, 2021


import pygame, sys, os
import time
import random
from commonUIelements.timer import timer as timer

# import UI components
from commonUIelements.Text import Text as TextDisplay
from commonUIelements.Button import Button as ButtonDisplay
from pygame.locals import (
    K_UP,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

width = 800
height = 600
white = (255,255,255)
red = (177,0,0)
BLACK = (0, 0, 0)
black = (0,0,0)
clock = pygame.time.Clock()
g = 1
score = 0
fps = 13
fruits = ['watermelon', 'orange']
text_display = TextDisplay()
button_display = ButtonDisplay()

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
font = pygame.font.Font(os.path.join(os.getcwd(), '../Ingame/FruitNinja/comic.ttf'), 30)
score_text = font.render(str(score), True, black, white)
time_text = font.render(str(time), True, black, white)
countdown = timer(30)
clock = pygame.time.Clock()
gameDisplay.fill(white)
def generate_random_fruits(fruit):
    path = os.path.join(os.getcwd(), '../Ingame/FruitNinja/'+fruit+'.png')
    data[fruit] = {
        'img' : pygame.image.load(path),
        'x' : random.randint(100, 500),
        'y' : 800,
        'speed_x' : random.randint(-10, 10),
        'speed_y' : random.randint(-80, -60),
        'throw' : False,
        't' : 0,
        'hit' : False,
    }

    if(random.random() >= 0.75):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

pygame.display.update()
def startGame(UpdateLocalHighScore, UpdateGlobalHighScore, runningState):
    
    global score_text
    global time_text
    global countdown
    global clock
    global score
    global text_display
    global button_display
    play = True
  
    if not play:
        play = True
        countdown.restart_timer()
    while play:
        click = False
        gameDisplay.fill(white)
        pause = button_display.add_button_to_screen(gameDisplay, 0, 0, 100, 50, red)
        text_display.add_to_screen(gameDisplay, 30, "Pause", 33, 28, BLACK, "freesansbold.ttf")
        gameDisplay.blit(score_text, (0,60))
        total_seconds = countdown.count_down(gameDisplay, font, width-90, height)
        time_text = font.render(str(time), True, black, white)
        for key,value in data.items():
            if value['throw']:
                value['x'] = value['x'] + value['speed_x']
                value['y'] = value['y'] + value['speed_y']
                value['speed_y'] += (g*value['t'])
                value['t'] += 1

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'],value['y']))
                else:
                    generate_random_fruits(key)

                current_position = pygame.mouse.get_pos()
                if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                    path = os.path.join(os.getcwd(),'../Ingame/FruitNinja/'+'half_'+key+'.png')
                    value['img'] = pygame.image.load(path)
                    value['speed_x'] += 10
                    score += 1
                    score_text = font.render(str(score), True, black, white)
                    value['hit'] = True

            else:
                generate_random_fruits(key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mx, my = pygame.mouse.get_pos()
        # back pressed
        if pause.collidepoint((mx, my)):
            if click:
                print("pause button pressed")
                return "pause"
        if total_seconds <= 0:
            for key,value in data.items():
                value['throw'] = False
    

            # update users' current highscore if applicable and return the score
            current_score = score
            user_highscore = UpdateLocalHighScore(current_score)

            # update global highscore
            global_highscore_user, global_highscore = UpdateGlobalHighScore(user_highscore)
            text_display.add_to_screen(gameDisplay, 30, "Global Highscore: " + str(global_highscore), width / 1.18, height / height + 70, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(gameDisplay, 30, "Global Highscore User: " + global_highscore_user, width / 1.28,height / height + 100, BLACK, "freesansbold.ttf")
            text_display.add_to_screen(gameDisplay, 40, "Game Over!", width / 2.2, height / 1.05, BLACK, "freesansbold.ttf")

        pygame.display.update()
        clock.tick(fps)

        


