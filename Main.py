#https://www.youtube.com/watch?v=bfRwxS5d0SI&ab_channel=BroCode
#w3schools.com
#https://www.youtube.com/watch?v=M_npdRYD4K0&ab_channel=PatrickLoeber
#https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
#https://www.edureka.co/blog/snake-game-with-pygame/
#https://www.youtube.com/watch?v=_-KjEgCLQFw&ab_channel=CoderSpace

#importing libraries
import pygame
import turtle
import random

snake_speed = 12

#Screen
screenx = 820
screeny = 500

# colors in the game
blue = pygame.Color(0, 0, 0)
# background
red = pygame.Color(255,255,255)
# score and food
white = pygame.Color(225, 0, 0)
# outline of game
green = pygame.Color(0, 255, 0)
# end of game text color
black = pygame.Color(0, 0, 225)
# snake color

#initialixing pygame/ making border
pygame.init()
pygame.display.set_caption("Lil Cuzzys Snakes")
Border = pygame.display.set_mode((screenx, screeny))

# FPS for the text of the game
fps = pygame.time.Clock()

# Snake spawning position
Snake = [100, 50]

#snake spawning size
snake_length = [[100, 50], [90, 50], [80,50], [70, 50]]

# snakes random food placement around the map
Snakefood = [random.randrange(1, (screenx//10)) * 10, random.randrange(1, (screeny//10)) * 10]

# makes food spawn in
Snake_food_spawn = True

# setting default snake direction towards
direction = 'right'
direction_shift = direction

# initial score
score = 0

# displaying the score
def score_display(choice, color, font, size):
# creating font 
    font = pygame.font.SysFont(font, size)

    # this makes the display objct
    #
    back_score = font.render('score : ' + str(score), True, color)

    #backing for the score text
    #
    score_rect = back_score.get_rect()

    # display text
    Border.blit(back_score, score_rect)

# game over function
def RIP():

        # font of score and timer
        STfont = pygame.font.SysFont('Press Start 4p', 40)

        # score display format
        game_over_surface = STfont.render(
            'score :' + str(score), True, green)

        # area around text for score
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text 
        game_over_rect.midtop = (screenx/2, screeny/4)

        # blit drawing text 
        Border.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # deactivating pygame library
        pygame.quit()

        # quitting the program
        quit()


# game controls
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_shift = 'up'
            if event.key == pygame.K_DOWN:
                direction_shift = 'down'
            if event.key == pygame.K_LEFT:
                direction_shift = 'left'
            if event.key == pygame.K_RIGHT:
                direction_shift = 'right'

    # if 2 keys are pressed at the same time, the snake needs to only move in one direction, not 2
    #
    #
    if direction_shift == 'up' and direction != 'down':
        direction = 'up'
    if direction_shift == 'down' and direction != 'up':
        direction = 'down'
    if direction_shift == 'left' and direction != 'right':
        direction = 'left'
    if direction_shift == 'right' and direction != 'left':
        direction = 'right'

    # how the snake will move along the screen given the input given
    if direction == 'up':
        Snake[1] -= 10
    if direction == 'down':
        Snake[1] += 10
    if direction == 'right':
        Snake[0] += 10
    if direction == 'left':
        Snake[0] -=10

    # Makes snake grow
    snake_length.insert(0, list(Snake))
    if Snake[0] == Snakefood[0] and Snake[1] == Snakefood[1]:
        score += 10
        Snake_food_spawn = False
    else:
        snake_length.pop()

    if not Snake_food_spawn:
        Snakefood = [random.randrange(1, (screenx//10)) * 10,
                        random.randrange(1, (screeny//10)) * 10]
    
    Snake_food_spawn = True
    Border.fill(black)

    for pos in snake_length:
        pygame.draw.rect(Border, blue, 
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(Border, white, pygame.Rect(
        Snakefood[0], Snakefood[1], 10, 10))

     # ending game variables
    if Snake[0] < 0 or Snake[0] > screenx-10:
        RIP()
    if Snake[1] < 0 or Snake[1] > screeny-10:
        RIP()

    # die if impact with wall settings
    for block in snake_length[1:]:
        if Snake[0] == block[0] and Snake [1] == block[1]:
            RIP()

    # score display through the entire game
    score_display(1, white, 'Press Start 2p', 20)

    # Refreshing game screen
    pygame.display.update()

    # Frames Per Second of snake moving across screen
    fps.tick(snake_speed)