import sys

import pygame


def run_game():
    # Initializes game and creates screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien invasion")

    # Setting up background color
    bg_color = (230, 230, 230)

    # Launch of the main game loop
    while True:
        # Tracking keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Each time the loop passes, the screen is redrawn
        screen.fill(bg_color)
        # Displaing last traced screen
        pygame.display.flip()

run_game()
