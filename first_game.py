import pygame
import os
import math


pygame.init()
os.chdir("C:\\Users\\CBriggs\\Desktop\\pygame")
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("My App")

clock = pygame.time.Clock()

running = True

white = (255,255,255)

x_img = pygame.image.load('x.png')

o_img = pygame.image.load('o.png')


x = int((display_width - 80) * 0.5)
y = int((display_height - 80) * 0.5)

images = [x_img, o_img]
def imageCall(x,y):
    gameDisplay.blit(images[0], (x - 100,y))
    gameDisplay.blit(images[1], (x + 100,y))



while running:
    keys = pygame.key.get_pressed()
    print(pygame.event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5

    print(x,y)

    gameDisplay.fill(white)
    imageCall(x,y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()