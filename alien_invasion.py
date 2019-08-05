import sys

import pygame

from settings import Settings


def run_game():
    # Initializes game, settings creates screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))
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
        screen.fill(ai_settings.bg_color)
        # Displaing last traced screen
        pygame.display.flip()

run_game()
