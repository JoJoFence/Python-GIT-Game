#  defines a general inhabitant
import pygame
class Being(object):
    def __init__(self, health, attack, pic, name, x, y):
        self.health = health
        self.attack = attack
        self.pic = pic
        self.name = name
        self.x = x
        self.y = y