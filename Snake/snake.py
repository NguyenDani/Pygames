import pygame
import random
import time

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


running = True

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

    snake_position[0] += dir_x
    snake_position[1] += dir_y

    # QUIT
    if event.type == pygame.QUIT:
        running = False

    screen.fill(black)

    pygame.draw.rect(screen, snake_color, (snake_position[0], snake_position[1], snake_size, snake_size))

    clock.tick(snake_speed)

    pygame.display.update()