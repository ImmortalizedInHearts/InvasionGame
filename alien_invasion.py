import sys

import pygame


def run_game():
    # Initializes game and creates screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien invasion")

    # Launch of the main game loop
    while True:
        # Tracking keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Displaing last traced screen
        pygame.display.flip()

run_game()
