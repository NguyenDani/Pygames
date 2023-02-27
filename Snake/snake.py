import pygame
import random
import time

# Display
window_x = 720
window_y = 480
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake")
pygame.display.flip()

# Snake
snake_color = pygame.Color(0, 255, 0)
snake_position = [window_x/2, window_y/2]
snake_body = [[window_x/2, window_y/2]]

running = True

# Run
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # QUIT
            if event.key == pygame.K_q:
                running = False

    # QUIT
    if event.type == pygame.QUIT:
        running = False

    pygame.display.update()