import pygame
import math

pygame.init()

size = width, height = 1000, 500
speed = [2, 2]
black = 0, 0, 0
x, y = 100, 100
x1, y1 = 500, 250
pomerajX = 0
pomerajY = 0

screen = pygame.display.set_mode(size)
rocket = pygame.image.load('c:/Users/marko/Desktop/vre/rocket.png')

planet1 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet2 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')

x, y = rocket.get_size()
rx = width/x*10
ry = height/x*20
rocket = pygame.transform.scale(rocket, (int(rx), int(ry)))

rx1 = width/x*25
ry1 = height/x*50
planet1 = pygame.transform.scale(planet1, (int(rx1), int(ry1)))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT] and x >= 0:
        x -= 1
    if key_input[pygame.K_UP] and y >= 0:
        y -= 1
    if key_input[pygame.K_RIGHT] and x <= width:
        x += 1
    if key_input[pygame.K_DOWN] and y <= height:
        y += 1

    screen.fill(black)
    screen.blit(rocket, (x, y))
    screen.blit(planet1, (x1,y1))
    
    for i in range(1):
    
        if x < x1:
            pomerajX += 1
        if x > x1:
            pomerajX -= 1

        if y < y1:
            pomerajY += 1
        if y > y1:
            pomerajY -= 1

    


    x += pomerajX*0.001
    y += pomerajY*0.001

    pygame.display.flip()

pygame.quit()