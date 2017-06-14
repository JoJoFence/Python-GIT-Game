import pygame, sys, time
from pygame.locals import *
import character

pygame.init()
width = 512
height = 512
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('game')

FPS = 30
fpsClock = pygame.time.Clock()
UP = 'up'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
main = character.Human(100, 100, "armorbase.png", "kason", 0, 0)
sec = character.Human(100, 100, "playerbase.png", "garry", 0, 0)
sprite = pygame.image.load(main.pic)
sprite2 = pygame.image.load(sec.pic)
cover = pygame.image.load("cover.png")
direction = DOWN
lel = 2
torf = True
player1 = []
player2 = []


def movementhandler(): 
    pygame.display.flip()
    if event.type == KEYDOWN:
        temp1 = [main.x, main.y]
        temp2 = [sec.x, sec.y]
        if temp1 not in player2 and temp1 not in player1[0:len(player1)-1]:
            if event.key == K_a:
                main.x -= 5
            elif event.key == K_d:
                main.x += 5
            elif event.key == K_w:
                main.y -= 5
            elif event.key == K_s:
                main.y += 5
            if not player1.__contains__([main.x, main.y]):
                player1.append([main.x, main.y])
            if len(player1) > 60:
                DISPLAYSURF.blit(cover, player1[0])
                player1.remove(player1[0])
        if temp2 not in player1 and temp2 not in player2[0:len(player2)-1]:
            if event.key == K_LEFT:
                sec.x -= 5
            elif event.key == K_RIGHT:
                sec.x += 5
            elif event.key == K_UP:
                sec.y -= 5
            elif event.key == K_DOWN:
                sec.y += 5
            if not player2.__contains__([sec.x, sec.y]):
                player2.append([sec.x, sec.y])
            if len(player2) > 60:
                DISPLAYSURF.blit(cover, player2[0])
                player2.remove(player2[0])


while True:
    DISPLAYSURF.blit(sprite2, (main.x, main.y))
    DISPLAYSURF.blit(sprite, (sec.x, sec.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        movementhandler()

    pygame.display.update()
    fpsClock.tick(FPS)
