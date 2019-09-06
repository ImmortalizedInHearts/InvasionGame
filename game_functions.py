import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


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


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets):
    # Tracking keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """Starts new game when you press the play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game settings
        ai_settings.initialize_dynamic_settings()
        # Mouse pointer is hiding
        pygame.mouse.set_visible(False)
        """Reset game statistic"""
        stats.reset_stats()
        stats.game_active = True

    # Reset score and level images
    sb.prep_score()
    sb.prep_level()

    # Lists cleaning
    aliens.empty()
    bullets.empty()

    # New fleet creation and placement of the ship in center
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_fleet_edges(ai_settings, aliens):
    """Reacts to the alien reaching the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets):
    """Processing of collisions of bullets and aliens"""
    # Deleting of bullets and aliens  participating in collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Processing of collisions of aliens and bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # The same thing happens as in a collision with a ship
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """Checks high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_screen(ai_settings, screen, stats, sb, ship, aliens,
                  bullets, play_button):
    """Update images on screen and displays new screen"""
    # Each time loop pass, screen is redrawn
    screen.fill(ai_settings.bg_color)
    # All bullets displays behind images of ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Displays score
    sb.show_score()
    # "Play" button is displayed if game is inactive
    if not stats.game_active:
        play_button.draw_button()
    # Displaing last traced screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates bullets positions and deletes unnecessary bullets"""
    bullets.update()
    # Removing bullets that went beyond the edge of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  ship, aliens, bullets)

    if len(aliens) == 0:
        # Deleting existing bullets, speed increasing and creation new fleet
        bullets.empty()
        ai_settings.increase_speed()
        # Level increasing
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if the fleet has reached the edge of the screen
       Then updates positions of aliens fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # "Alien-ship" collision check
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculates quantity of aliens in line"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Defines necessary quantity of lines"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates alien and sets it in line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creates aliens fleet"""
    # Alien creation and calculation of aliens quantity in line
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Aliens fleet creation
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Creates new bullet instance and adds it to group "bullets"
        if max is not reached"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def change_fleet_direction(ai_settings, aliens):
    """Moves down fleet and changes it's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Alien/ship collision processing"""
    if stats.ships_left > 0:
        # Redusing 'ship_left'
        stats.ships_left -= 1

        # Lists cleaning
        aliens.empty()
        bullets.empty()

        # New fleet creation and placement of the ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
