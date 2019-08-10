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
