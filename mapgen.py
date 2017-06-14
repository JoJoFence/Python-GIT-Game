import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock=pygame.time.Clock()

width= 512
height= 512
DISPLAYSURF = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('game')
background=pygame.image.load('unnamed.png')


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('unnamed.png')
spritex=200
spritey=130
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
                spritex-=5

            elif event.key == K_RIGHT:
                spritex+=5

            elif event.key == K_UP:
                spritey-=5
            elif event.key == K_DOWN:
                spritey+=5

    pygame.display.update()
    fpsClock.tick(FPS)