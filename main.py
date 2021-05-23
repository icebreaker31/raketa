import pygame
import math

pygame.init()

size = width, height = 1000, 500
speed = [2, 2]
black = 0, 0, 0
x, y = 100, 100
x1, y1 = 100, 100
x2, y2 = 500, 300
x3, y3 = 700, 100
pomerajX = 0
pomerajY = 0

screen = pygame.display.set_mode(size)
rocket = pygame.image.load('c:/Users/marko/Desktop/vre/rocket.png')

planet1 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet2 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet3 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')

x, y = rocket.get_size()
rx = width/x*10
ry = height/x*20
rocket = pygame.transform.scale(rocket, (int(rx), int(ry)))

rx1 = width/x*25
ry1 = height/x*50
planet1 = pygame.transform.scale(planet1, (int(rx1), int(ry1)))

rx2 = width/x*25
ry2 = height/x*50
planet2 = pygame.transform.scale(planet2, (int(rx2), int(ry2)))

rx3 = width/x*25
ry3 = height/x*50
planet3 = pygame.transform.scale(planet3, (int(rx3), int(ry3)))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT] and x >= 0:
        x -= 2
    if key_input[pygame.K_UP] and y >= 0:
        y -= 2
    if key_input[pygame.K_RIGHT] and x <= width:
        x += 2
    if key_input[pygame.K_DOWN] and y <= height:
        y += 2

    screen.fill(black)
    screen.blit(rocket, (x, y))
    screen.blit(planet1, (x1,y1))
    screen.blit(planet1, (x2,y2))
    screen.blit(planet1, (x3,y3))
    
    g = 0.05

    for i in range(1):
    
        if x < x1:
            pomerajX += g/(10/(x1 - x))
        if x > x1:
            pomerajX -= g/(10/(x - x1))

        if  y < y1:
            pomerajY += g/(10/(y1 - y))
        if y > y1:
            pomerajY -= g/(10/(y - y1))

    for i in range(1):
    
        if x < x2:
            pomerajX += g/(10/(x2 - x))
        if x > x1:
            pomerajX -= g/(10/(x - x2))

        if  y < y2:
            pomerajY += g/(10/(y2 - y))
        if y > y2:
            pomerajY -= g/(10/(y - y2))

    for i in range(1):
    
        if x < x3:
            pomerajX += g/(10/(x3 - x))
        if x > x1:
            pomerajX -= g/(10/(x - x3))

        if  y < y3:
            pomerajY += g/(10/(y3 - y))
        if y > y3:
            pomerajY -= g/(10/(y - y3))

    
    x += pomerajX*0.001
    y += pomerajY*0.001


    pygame.display.flip()
    #ovde će kolega Damjan da ubaci mehaniku kolizije (fail state za igricu)
    #dodatno ćemo unaprediti algoritam za gravitaciju i računanje pozicije
    #moguće je dodati još planeta LAKO

pygame.quit()