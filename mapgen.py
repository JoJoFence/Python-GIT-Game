import pygame, sys, time
from pygame.locals import *
import character

pygame.init()
width = 512
height = 512
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Basically Tron')

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
drct1 = "D"
drct2 = "W"

def movementhandler():
    global drct1
    global drct2
    global player1
    global player2
    pygame.display.flip()
    if event.type == KEYDOWN:
        temp1 = [main.x, main.y]
        temp2 = [sec.x, sec.y]
        if temp1 not in player2 and temp1 not in player1[0:len(player1)-1]:
            if event.key == K_a:
                drct1 = "A"
            elif event.key == K_d:
                drct1 = "D"
            elif event.key == K_w:
                drct1 = "W"
            elif event.key == K_s:
                drct1 = "S"

        if temp2 not in player1 and temp2 not in player2[0:len(player2)-1]:
            if event.key == K_LEFT:
                drct2 = "A"
            elif event.key == K_RIGHT:
                drct2 = "D"
            elif event.key == K_UP:
                drct2 = "W"
            elif event.key == K_DOWN:
                drct2 = "S"


while True:
    DISPLAYSURF.blit(sprite2, (main.x, main.y))
    DISPLAYSURF.blit(sprite, (sec.x, sec.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        movementhandler()
    if ([main.x,main.y]) not in player2:
        if drct1 == "A":
            main.x -= 5
        elif drct1 == "D":
            main.x += 5
        elif drct1 == "W":
            main.y -= 5
        elif drct1 == "S":
            main.y += 5
    if ([sec.x, sec.y]) not in player1:
        if drct2 == "A":
            sec.x -= 5
        elif drct2 == "D":
            sec.x += 5
        elif drct2 == "W":
            sec.y -= 5
        elif drct2 == "S":
            sec.y += 5
    if ([main.x, main.y]) not in player1:
        player1.append([main.x, main.y])
    if ([sec.x, sec.y]) not in player2:
        player2.append([sec.x, sec.y])
    pygame.display.update()
    fpsClock.tick(FPS)