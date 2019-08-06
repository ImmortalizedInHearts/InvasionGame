import sys

import pygame


"""Stores functions provide game process"""


def check_events(ship):
    # Tracking keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on screeen and displays new screen"""
    # Each time loop pass, screen is redrawn
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Displaing last traced screen
    pygame.display.flip()
