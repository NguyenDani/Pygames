import pygame
import random
import time

pygame.init()

# Display
window_x = 720
window_y = 480
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
#pygame.display.flip()
black = (0, 0, 0)

# Snake
snake_speed = 15
snake_color = pygame.Color(0, 255, 0)
snake_size = 10
snake_position = [window_x/2, window_y/2]
#snake_body = [[window_x/2, window_y/2]]
direction = "up"
k_change = "up"

# Game Over text
font = pygame.font.SysFont("Comic Sans MS", 32)
text = font.render("Game Over", True, snake_color)
textRect = text.get_rect()
textRect.center = (window_x/2, window_y/2)

running = True
gameover = False

# Run
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                k_change = "up"
            if event.key == pygame.K_DOWN:
                k_change = "down"
            if event.key == pygame.K_LEFT:
                k_change = "left"
            if event.key == pygame.K_RIGHT:
                k_change = "right"
            
            #restart
            if event.key == pygame.K_r and gameover == True:
                gameover = False
                snake_position = [window_x/2, window_y/2]
                snake_speed = 15

    # Key change and direction
    if k_change == "up" and direction != "down":
        direction = k_change
        dir_x = 0
        dir_y = -snake_size
    if k_change == "down" and direction != "up":
        direction = k_change
        dir_x = 0
        dir_y = snake_size
    if k_change == "left" and direction != "right":
        direction = k_change
        dir_x = -snake_size
        dir_y = 0
    if k_change == "right" and direction != "left":
        direction = k_change
        dir_x = snake_size
        dir_y = 0

    # Updating snake position
    snake_position[0] += dir_x
    snake_position[1] += dir_y

    # Game Over conditions
    if snake_position[0] >= window_x or snake_position[0] < 0 or snake_position[1] >= window_y or snake_position[1] < 0:
        gameover = True
        snake_speed = 0
        screen.blit(text, textRect)

    if gameover != True:
        screen.fill(black)

    pygame.draw.rect(screen, snake_color, (snake_position[0], snake_position[1], snake_size, snake_size))

    clock.tick(snake_speed)

    # QUIT
    if event.type == pygame.QUIT:
        running = False

    pygame.display.update()