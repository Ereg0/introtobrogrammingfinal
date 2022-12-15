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

# Initialising pygame
pygame.init()
 
# Initialise game window
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
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
# creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, green)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
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
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(Snake))
    if Snake[0] == Snakefood[0] and Snake[1] == Snakefood[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        Snakefood = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
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
 
    # displaying score countinuously
    show_score(1, white, 'Press Start 2p', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
