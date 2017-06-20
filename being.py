#  defines a general inhabitant
import pygame
class Being(pygame.sprite.Sprite):
    def __init__(self, color, width, height, health):
        pygame.sprite.Sprite.__init__(self)
        #define sprites color
        self.image = pygame.Surface([width, height])
        #color of player
        self.image.fill(color)
        #fetch rect then update it by changing x and y
        self.rect = self.image.get_rect()
        self.health = health
