import sys

import pygame

from bullet import Bullet


"""Stores functions provide game process"""


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reacts on key pushing"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    """Reacts to releasing keys"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # Tracking keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on screen and displays new screen"""
    # Each time loop pass, screen is redrawn
    screen.fill(ai_settings.bg_color)
    # All bullets displays behind images of ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Displaing last traced screen
    pygame.display.flip()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Creates new bullet instance and adds it to group "bullets"
        if max is not reached"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Updates bullets positions and deletes unnecessary bullets"""
    bullets.update()
    # Removing bullets that went beyond the edge of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
