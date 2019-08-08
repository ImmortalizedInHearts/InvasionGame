import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullets control class"""

    def __init__(self, ai_settings, screen, ship):
        """Creates bullet object in current ship position"""
        super().__init__()
        self.screen = screen

        # Bullet creation in (0,0) position and necessary position assignment
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet position is stored in float format
        self.y = float(self.rect.y)

        # Determination of bullets color and speed
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
