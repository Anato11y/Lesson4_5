import pygame
import turtle
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Пинг-понг")

image = pygame.image.load(”название_изображения”)
image_rect = image.get.rect()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 34, 250))
    pygame.display.flip()

pygame.quit()

