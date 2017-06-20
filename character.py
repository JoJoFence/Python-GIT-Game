import being
import pygame

class Human(being.Being):
    def __init__(self, health, attack, pic, name, x, y):
        being.Being.__init__(self, health, attack, pic, name, x, y)