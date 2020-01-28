import pygame
import random
import sys

from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUNDCOLOR = (100,100,100)
pygame.init()
mainClock = pygame.time.Clock()
WINDOWWIDTH = 500
WINDOWHEIGHT = 300

BOXWIDTH = 20

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Snake')
head = pygame.Rect(100, 100, BOXWIDTH, BOXWIDTH)
pygame.draw.rect(windowSurface, (150, 150, 150), head)
pygame.draw.rect(windowSurface, BLACK, head, 2)

pygame.display.update()
box = pygame.Rect(100, 100, BOXWIDTH, BOXWIDTH)
def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for gameevent in pygame.event.get():
            if gameevent.type == QUIT:
                terminate()
            if gameevent.type == KEYDOWN:
                if gameevent.key == K_ESCAPE:  # Pressing ESC quits.
                    terminate()
                return


def drawFruit(body):
    while True:
        breakout = True
        apple = pygame.Rect(random.randint(0,WINDOWWIDTH/BOXWIDTH-1)*BOXWIDTH,random.randint(0,WINDOWHEIGHT/BOXWIDTH-1)*BOXWIDTH,BOXWIDTH,BOXWIDTH)
        if len(body) > 0:
            for b in body:
                if apple.colliderect(b):
                    breakout = False
        if breakout:
            break
    return apple

while True:
    head = pygame.Rect(int(WINDOWWIDTH/2/BOXWIDTH)*BOXWIDTH, int(WINDOWHEIGHT/2/BOXWIDTH)*BOXWIDTH , BOXWIDTH, BOXWIDTH)
    pygame.draw.rect(windowSurface, (150, 150, 150), head)
    pygame.draw.rect(windowSurface, BACKGROUNDCOLOR, head, 2)
    pygame.display.update()

    moveRight = False
    moveUp = False
    moveDown = False
    moveLeft = False
    yspeed = xspeed = 0
    prevX = prevY = 0
    body = []
    body.append(pygame.Rect(head.left - xspeed * BOXWIDTH, head.top - yspeed * BOXWIDTH, BOXWIDTH, BOXWIDTH))
    count = 1
    counter = -10
    createFruit = True
    fruit = []
    moving = False
    while True:
        breakOut = False
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and not moveRight and count == 1:
                    moveRight = False
                    moveUp = False
                    moveDown = False
                    moveLeft = True
                    count = 0
                if (event.key == K_RIGHT or event.key == K_d) and not moveLeft and count == 1:
                    moveLeft = False
                    moveUp = False
                    moveDown = False
                    moveRight = True
                    count = 0
                if (event.key == K_UP or event.key == K_w) and not moveDown and count == 1:
                    moveDown = False
                    moveRight = False
                    moveLeft = False
                    moveUp = True
                    count = 0
                if (event.key == K_DOWN or event.key == K_s) and not moveUp and count == 1:
                    moveUp = False
                    moveRight = False
                    moveLeft = False
                    moveDown = True
                    count = 0
        if moveDown or moveUp or moveLeft or moveRight:
            moving = True
        if moveDown:
            head.top += BOXWIDTH
            xspeed = 0
            yspeed = 1
            count = 1
        if moveUp:
            head.top -= BOXWIDTH
            xspeed = 0
            yspeed = -1
            count = 1
        if moveLeft:
            head.left -= BOXWIDTH
            xspeed = -1
            yspeed = 0
            count = 1
        if moveRight:
            head.left += BOXWIDTH
            xspeed = 1
            yspeed = 0
            count = 1
        windowSurface.fill(BACKGROUNDCOLOR)
        if createFruit:
            createFruit = False
            counter = 0
            fruit = drawFruit(body)
            if moving:
                for i in range(3):
                    body.append(pygame.Rect(head.left - xspeed*BOXWIDTH, head.top - yspeed*BOXWIDTH, BOXWIDTH, BOXWIDTH))
        if createFruit == False:
            pygame.draw.rect(windowSurface, (255, 0, 0), fruit)

        if len(body) > 0:
            body[0].left = head.left - xspeed*BOXWIDTH
            body[0].top = head.top - yspeed*BOXWIDTH
            prevX = body[0].left
            prevY = body[0].top
        if head.colliderect(fruit):
            createFruit = True
        for b in range(1,len(body)):
            prev2X = body[b].left
            prev2Y = body[b].top
            body[b].left = prevX
            body[b].top = prevY
            prevX = prev2X
            prevY = prev2Y
            pygame.draw.rect(windowSurface, (100, 180, 100), body[b])
            pygame.draw.rect(windowSurface, BACKGROUNDCOLOR, body[b], 2)
            if head.colliderect(body[b]):
                breakOut = True


        pygame.draw.rect(windowSurface, (150, 150, 150), head)
        pygame.draw.rect(windowSurface, BACKGROUNDCOLOR, head, 2)
        if head.right > WINDOWWIDTH or head.left < 0 or head.bottom > WINDOWHEIGHT or head.top < 0:
            breakOut = True
        if breakOut:
            waitForPlayerToPressKey()
            break
        pygame.display.update()

        mainClock.tick(10)
        counter += 1