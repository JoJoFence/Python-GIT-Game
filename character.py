#  defines the player character and is based off the Being class
import being


class Human(being.Being):
    def __init__(self, health, attack):
        being.Being.__init__(self, health, attack)
     
