import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes game, settings creates screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # "Play" button creation
    play_button = Button(ai_settings, screen, "Play")

    # Instance creation for storing game statistic
    stats = GameStats(ai_settings)

    # Ship and groups of bullets and aliens creation
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Aliens fleet creation
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Launch of the main game loop
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                        bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                         bullets, play_button)


run_game()
