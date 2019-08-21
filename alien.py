import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Describes alien behavior"""

    def __init__(self, ai_settings, screen):
        """Initializes alien and it's first position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading alien image and getting a rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the top left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Determination of alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Displays alien in current position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True, if alien touched screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves alien to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
