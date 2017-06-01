import pygame

pygame.init()  # initializes pygame

display_width = 512
display_height = 512

black = (0, 0, 0)
white = (255, 255, 255)

display = pygame.display.set_mode((display_width, display_height))  # sets dimensions
clock = pygame.time.Clock()  # makes all functions operate under one clock


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():  # examples of events: mouse movement, key pressed
            if event.type == pygame.QUIT:  # when user clicks "x"
                game_exit = True

game_loop()
pygame.quit()  # quit pygame
quit()  # quits program
