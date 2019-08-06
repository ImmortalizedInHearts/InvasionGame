import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes game, settings creates screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))
    pygame.display.set_caption("Alien invasion")

    # Ship creation
    ship = Ship(screen)

    # Launch of the main game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
