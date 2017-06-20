import pygame, sys, time
from pygame.locals import *
import character

pygame.init()
width = 512
height = 512
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('game')
background = pygame.image.load('backround1.png')
FPS = 30
fpsClock = pygame.time.Clock()
UP = 'up'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
player1 = pygame.sprite.Sprite
player1.image = "playerbase.png"
direction = DOWN

def movementhandler(sprite1, sprite2):
    pygame.display.flip()
    print(str(sprite1.x) + ", " + str(sprite1.y))
    print(str(sprite2.x) + ", " + str(sprite2.y))




while True:
    DISPLAYSURF.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.sprite.DirtySprite.(player1)

    pygame.display.update()
    fpsClock.tick(FPS)