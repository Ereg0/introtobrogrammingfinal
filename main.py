#https://www.youtube.com/watch?v=bfRwxS5d0SI&ab_channel=BroCode
#w3schools.com
#https://www.youtube.com/watch?v=M_npdRYD4K0&ab_channel=PatrickLoeber
#https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/


# importing libraries
import pygame
import random

snake_speed = 15
 
# Window size
window_x = 820
window_y = 580

# defining colors
blue = pygame.Color(0, 0, 0)
red = pygame.Color(255, 255, 255)
white = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 255)

# initialise pygame
pygame.init()
 
# window around the game, more for decoration
pygame.display.set_caption('Lil Cuzzys Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
Snake = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
Snakefood = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

#makes food spawn in
fruit_spawn = True
 
# direction snake spawns in
direction = 'RIGHT'
change_to = direction
 
# score
score = 0
 
# the score on the top of the game
def show_score(choice, color, font, size):

# font and design of the score
    Font = pygame.font.SysFont(font, size)
    score_backing = Font.render('Score : ' + str(score), True, color)
    score_rect = score_backing.get_rect()
     
    # displaying text
    game_window.blit(score_backing, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    score.font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    gameoverback = score.font.render(
        'Your Score is : ' + str(score), True, green)
     
    # create a rectangular object for the text
    # surface object
    gameovermiddlesmall = gameoverback.get_rect()
     
    # setting position of the text
    gameovermiddlesmall.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(gameoverback, gameovermiddlesmall)
    pygame.display.flip()
     
    
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
   
 
 
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
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
 
    # code that makes the snake larger as it eats
    snake_body.insert(0, list(Snake))
    if Snake[0] == Snakefood[0] and Snake[1] == Snakefood[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        Snakefood[0], Snakefood[1], 10, 10))
 
    # Game Over conditions
    if Snake[0] < 0 or Snake[0] > window_x-10:
        game_over()
    if Snake[1] < 0 or Snake[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if Snake[0] == block[0] and Snake[1] == block[1]:
            game_over()
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
