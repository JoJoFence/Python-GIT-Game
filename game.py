import pygame, sys, time
from pygame.locals import *
import being
import random

pygame.init()
width = 512
height = 512
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('game')
FPS = 30
fpsClock = pygame.time.Clock()
BACKGROUND_COLOR = (55, 5, 5)

# players grouping and creation
players = pygame.sprite.Group()
player = being.Being((0, 123, 123), 8, 8, 100)
player2 = being.Being((123, 123, 123), 8, 8, 100)
player.add(players)
player2.add(players)
playerscore = [0, 0]

# bad guy group eggy clucks
bad_guys = pygame.sprite.Group()
for i in range(30):
    guy = being.Being((255, i, 0), 16, 16, 20)
    bad_guys.add(guy)


# player one movement
def player1move():
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player.rect.x -= 5
    if keys[K_d]:
        player.rect.x += 5
    if keys[K_w]:
        player.rect.y -= 5
    if keys[K_s]:
        player.rect.y += 5
    if keys[K_e]:
        find_guy(player, bad_guys, 6)
    if keys[K_j]:
        player2.rect.x -= 5
    if keys[K_l]:
        player2.rect.x += 5
    if keys[K_i]:
        player2.rect.y -= 5
    if keys[K_k]:
        player2.rect.y += 5
    if keys[K_o]:
        find_guy(player2, bad_guys, 6)

#wall group
walls = pygame.sprite.Group()
wall1 = being.Being((255, i, 0), 512, 8, 20)
wall1.add(walls)
wall2 = being.Being((255, i, 0), 8, 512, 20)
wall2.add(walls)
wall3 = being.Being((255, i, 0), 512, 8, 20)
wall3.add(walls)
wall3.rect.x = 0
wall3.rect.y = 504
wall4 = being.Being((255, i, 0), 8, 512, 20)
wall4.add(walls)
wall4.rect.x = 504
wall4.rect.y = 0


def badguyplacement():
    for men in bad_guys:
        men.rect.x = random.randint(5, 500)
        men.rect.y = random.randint(5, 500)


def find_guy(playerC, group, lengthofbeam):
    for guys in group:
        if pygame.sprite.collide_rect_ratio.__call__(pygame.sprite.collide_rect_ratio(lengthofbeam), playerC, guys):
            pygame.draw.line(DISPLAYSURF, (255, 4, 4), (playerC.rect.centerx, playerC.rect.centery), (guys.rect.centerx, guys.rect.centery))
            guys.health -= 1



def checkdeadorwall():
    for playerC in players:
        for wall in walls:
            if pygame.sprite.collide_rect_ratio.__call__(pygame.sprite.collide_rect_ratio(1), playerC, wall):
                playerC.rect.x = 512/2
                playerC.rect.y = 512/2
    for guys in bad_guys:
        if guys.health <= 0:
            guys.rect.x = -200
            guys.rect.y = -200
            guys.kill()
    for playerC in players:
        if playerC.health <= 0:
            playerC.rect.x = -500
            playerC.rect.y = -50
            playerC.kill()

badguyplacement()
x = 0

while True:
    if x % 233 == 0:
        badguyplacement()
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == QUIT or x == 1000 or len(players) == 0 or len(bad_guys) == 0:
            if len(players) > 0:
                print("Winner is the good guys.")
            else:
                print("Winner is bad guys.")

            pygame.quit()
            sys.exit()
    player1move()
    for guys in bad_guys:
        find_guy(guys, players, 3)
    walls.update()
    walls.draw(DISPLAYSURF)
    bad_guys.update()
    bad_guys.draw(DISPLAYSURF)
    players.update()
    players.draw(DISPLAYSURF)
    checkdeadorwall()
    x += 1


