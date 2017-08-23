import pygame, sys, time
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from random import random

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=700
height=500
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('bg.png')

def mistake():
    return random()*10 - 5 # between -5 and 5


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('down.png')
spritex=0
spritey=0
direction=DOWN


while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                spritex-=70 + mistake()
                # sprite=pygame.image.load('left.png')
            elif event.key == K_RIGHT:
                spritex+=70 + mistake()
                # sprite=pygame.image.load('right.png')
            elif event.key == K_UP:
                spritey-=50 + mistake()
                # sprite=pygame.image.load('up.png')
            elif event.key == K_DOWN:
                spritey+=50 + mistake()
                # sprite=pygame.image.load('down.png')

    pygame.display.update()
    fpsClock.tick(FPS)