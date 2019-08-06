import sys

import pygame


"""Stores functions provide game process"""


def check_events():
    # Tracking keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Update images on screeen and displays new screen"""
    # Each time loop pass, screen is redrawn
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Displaing last traced screen
    pygame.display.flip()
