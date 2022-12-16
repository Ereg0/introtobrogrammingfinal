#https://www.youtube.com/watch?v=bfRwxS5d0SI&ab_channel=BroCode
#w3schools.com
#https://www.youtube.com/watch?v=M_npdRYD4K0&ab_channel=PatrickLoeber
#https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
#https://www.edureka.co/blog/snake-game-with-pygame/
#https://www.youtube.com/watch?v=_-KjEgCLQFw&ab_channel=CoderSpace

# importing libraries
import pygame
import turtle
import random

snake_speed = 12

# Window size
Screenx = 820
Screeny = 580

# defining colors
blue = pygame.Color(0, 0, 0)
# background
red = pygame.Color(255, 255, 255)
# Score and food
white = pygame.Color(255, 0, 0)
# outline of game
green = pygame.Color(0, 255, 0) 
# end score text color
black = pygame.Color(0, 0, 255)
#snake

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Lil Cuzzys Snakes')
Border = pygame.display.set_mode((Screenx, Screeny))

# Frames per second of text
fps = pygame.time.Clock()

# defining snake default position
Snake = [100, 50]

# defining first 4 blocks of snake body
snake_length = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
Snakefood = [random.randrange(1, (Screenx//10)) * 10, random.randrange(1, (Screeny//10)) * 10]

#makes food spawn in
Snake_food_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
Direction_shift = direction

# initial score
score = 0

# displaying Score function
def score_display(choice, color, font, size):
# creating font object score_font
    font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    Back_Score = font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = Back_Score.get_rect()

    # displaying text
    Border.blit(Back_Score, score_rect)

# game over function
def RIP():

    # Choosing the font of the text of the score and timer
    my_font = pygame.font.SysFont('Press Start 4p', 40)

    # score display format
    game_over_surface = my_font.render(
        'Score :' + str(score), True, green)

    # area around text for score
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (Screenx/2, Screeny/4)

    # blit will draw the text on screen
    Border.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Game controls
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Direction_shift = 'UP'
            if event.key == pygame.K_DOWN:
                Direction_shift = 'DOWN'
            if event.key == pygame.K_LEFT:
                Direction_shift = 'LEFT'
            if event.key == pygame.K_RIGHT:
                Direction_shift = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if Direction_shift == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if Direction_shift == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if Direction_shift == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if Direction_shift == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        Snake[1] -= 10
    if direction == 'DOWN':
        Snake[1] += 10
    if direction == 'LEFT':
        Snake[0] -= 10
    if direction == 'RIGHT':
        Snake[0] += 10

    # makes snake grow
    snake_length.insert(0, list(Snake))
    if Snake[0] == Snakefood[0] and Snake[1] == Snakefood[1]:
        score += 10
        Snake_food_spawn = False
    else:
        snake_length.pop()

    if not Snake_food_spawn:
        Snakefood = [random.randrange(1, (Screenx//10)) * 10,
                          random.randrange(1, (Screeny//10)) * 10]

    Snake_food_spawn = True
    Border.fill(black)

    for pos in snake_length:
        pygame.draw.rect(Border, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(Border, white, pygame.Rect(
        Snakefood[0], Snakefood[1], 10, 10))

    # ending game variables
    if Snake[0] < 0 or Snake[0] > Screenx-10:
        RIP()
    if Snake[1] < 0 or Snake[1] > Screeny-10:
        RIP()

    # impact in wall game ovwe settings
    for block in snake_length[1:]:
        if Snake[0] == block[0] and Snake[1] == block[1]:
            RIP()

    # score display through the entire game
    score_display(1, white, 'Press Start 2p', 20)

    # Refreshing game screen
    pygame.display.update()

    # Frames Per Second of snake moving across screen
    fps.tick(snake_speed)