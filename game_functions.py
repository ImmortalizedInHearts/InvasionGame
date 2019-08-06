import sys

import pygame


"""Stores functions provide game process"""


def check_events():
    # Tracking keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
