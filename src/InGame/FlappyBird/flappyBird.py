import pygame, sys, random, os
sys.path.insert(0, './')


'''SETUP CONSTANTS/ASSETS/CLASSES'''
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


'''INITIALIZE THE GAME'''
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("04B_19.ttf", 40)
pygame.display.set_caption('3A04 Game Demo')


#game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
can_score = True

base_path = os.path.dirname(__file__)
bg_surface = pygame.image.load(os.path.join(base_path,'../../assets/background-day.png')).convert()
bg_surface = pygame.transform.scale(bg_surface, (800, 600))

floor_surface =  pygame.image.load(os.path.join(base_path,"../../assets/base.png")).convert()
floor_surface = pygame.transform.scale(floor_surface, (800, 150))
left_edge_of_floor = 0

bird_surface = pygame.image.load(os.path.join(base_path,"../../assets/bluebird-midflap.png")).convert_alpha()
bird_rect = bird_surface.get_rect(center = (90, 300))

pipe_surface = pygame.image.load(os.path.join(base_path,"../../assets/pipe-green.png")).convert()
pipe_surface = pygame.transform.scale(pipe_surface, (55, 600))

game_over_surface = (pygame.image.load(os.path.join(base_path,'../../assets/message.png')).convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (400,300))

pause_surface = pygame.image.load(os.path.join(base_path,"../../assets/pause2.png")).convert()
pause_surface = pygame.transform.scale(pause_surface, (60,30))
pause_rect = pause_surface.get_rect(center = (30,15))

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 200, 300, 500]


SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)


def moving_floor():
    screen.blit(floor_surface, (left_edge_of_floor,540))
    screen.blit(floor_surface, (left_edge_of_floor+800,540))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (900, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (900, random_pipe_pos - 200))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    global can_score
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            can_score = True
            return False
    
    if bird_rect.top <= -150 or bird_rect.bottom >= 580:
        can_score = True
        return False
    
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, bird_movement * 3, 1)
    return new_bird

def score_display(game_state, global_highscore, global_highscore_user):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center = (400, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
        score_rect = score_surface.get_rect(center = (400, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'Global High Score: {int(global_highscore)}', True, (255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (400, 500))
        screen.blit(high_score_surface, high_score_rect)

        user_high_score_surface = game_font.render(f'Username: {(global_highscore_user)}', True, (255,255,255))
        user_high_score_rect = high_score_surface.get_rect(center = (400, 520))
        screen.blit(user_high_score_surface, user_high_score_rect)

# def update_score(score, high_score):
#     if score > high_score:
#         high_score = score
#     return high_score

def pipe_score_check():
    global can_score, score
    if pipe_list:
        for pipe in pipe_list:
            if 87 < pipe.centerx < 93 and can_score:
                score += 1
                #score_sound.play()
                can_score = False
            if pipe.centerx < 0:
                can_score = True


def startGame(UpdateLocalHighScore,  UpdateGlobalHighScore, runningState):

    global gravity, bird_movement, game_active, score, high_score, can_score, pipe_list, left_edge_of_floor

    if not runningState: 
        gravity = 0.25
        bird_movement = 0
        game_active = True
        score = 0
        high_score = 0
        can_score = True

    score_updated = False

    while runningState:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = 0
                    bird_movement -= 7
                if event.type == pygame.KEYDOWN and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (90, 412)
                    bird_movement = 0
                    score = 0


            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())
            
            if event.type == MOUSEBUTTONDOWN:
                # Left click
                if event.button == 1:

                    click = True

        screen.blit(bg_surface, (0,0))
        screen.blit(pause_surface, (0,0))

        if game_active:
            #bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement 
            screen.blit(rotated_bird, bird_rect)
            game_active = check_collision(pipe_list)
            
            #pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            #Score
            pipe_score_check()
            score_display("main_game", 0, "")
        else:
            screen.blit(game_over_surface,game_over_rect)
            
            high_score = UpdateLocalHighScore(score)
            global_highscore_user, global_highscore = UpdateGlobalHighScore(high_score)
            
            score_display("game_over", global_highscore, global_highscore_user)
        
        
        #Cursor location
        mx, my = pygame.mouse.get_pos()
        # back pressed
        if pause_rect.collidepoint((mx, my)):
            if click:
                print("pause button pressed")
                return "pause"

        #floor
        left_edge_of_floor -= 1
        moving_floor()

        if left_edge_of_floor <= -500:
            left_edge_of_floor = 0
        pygame.display.update()
        clock.tick(120)
