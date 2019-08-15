import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Initializes game, settings creates screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))
    pygame.display.set_caption("Alien invasion")

    # Ship creation
    ship = Ship(ai_settings, screen)

    # Creating a group for storing bullets
    bullets = Group()

    # Alien creation
    alien = Alien(ai_settings, screen)

    # Launch of the main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
