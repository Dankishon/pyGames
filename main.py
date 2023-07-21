import pygame
from colors import *

WIDHT = 720
HEIGHT = 480

sr = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('Shada')
pygame.display.set_icon(pygame.image.load('37812.png'))

fps = 30
clock = pygame.time.Clock()

position_x = 20
position_y = 100
is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

while True: #open game window
    sr.fill(Black)
    for event in pygame.event.get(): #close game window
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                is_key_left = True
                position_x -= 20
            if event.key == pygame.K_d:
                is_key_right = True
                position_x += 20
            if event.key == pygame.K_w:
                is_key_top = True
                position_y -= 20
            if event.key == pygame.K_s:
                is_key_down = True
                position_y += 20

    pygame.draw.rect(sr, White, (position_x, position_y, 60, 60))
    pygame.display.update()
    clock.tick(fps)


