import pygame
import math

pygame.init()

size = width, height = 1000, 500
speed = [2, 2]
black = 0, 0, 0
f = 10
x, y = 0, 0
x1, y1 = 35, 320
x2, y2 = 234, 30
x3, y3 = 478, 150
x4, y4 = 45, 123
x5, y5 = 600, 56
x6, y6 = 700, 250

screen = pygame.display.set_mode(size)
rocket = pygame.image.load('c:/Users/marko/Desktop/vre/rocket.png')

planet1 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet2 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet3 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet4 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet5 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')
planet6 = pygame.image.load('c:/Users/marko/Desktop/vre/planet.png')

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

rx4 = width/x*25
ry4 = height/x*50
planet4 = pygame.transform.scale(planet4, (int(rx4), int(ry4)))

rx5 = width/x*25
ry5 = height/x*50
planet5 = pygame.transform.scale(planet5, (int(rx5), int(ry5)))

rx6 = width/x*25
ry6 = height/x*50
planet6 = pygame.transform.scale(planet6, (int(rx6), int(ry6)))

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
    screen.blit(planet2, (x2,y2))
    screen.blit(planet3, (x3,y3))
    screen.blit(planet4, (x4,y4))
    screen.blit(planet5, (x5,y5))
    screen.blit(planet6, (x6,y6))

    #def calculateDistance(x1,y1,x2,y2):
    #dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #return dist.

    for i in range(1):
        ravno = x1 - x
        uspravno = y1 - y
        if ravno < 0:
            x -= 0.2
        if ravno > 0:
            x += 0.2
        if ravno < 50:
            x -= 0.1
        if ravno > 50:
            x += 0.1
        if ravno < 100:
            x -= 0.01
        if ravno > 100:
            x += 0.01
        if uspravno < 0:
            y -= 0.2
        if uspravno > 0:
            y += 0.2 
        if uspravno < 50:
            y -= 0.1
        if uspravno > 50:
            y += 0.1
        if uspravno < 100:
            y -= 0.01
        if uspravno > 100:
            y += 0.01  
    

    
    pygame.display.flip()

pygame.quit()