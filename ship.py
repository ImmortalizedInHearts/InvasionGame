import pygame


class Ship():
    """Describes ship behavior"""

    def __init__(self, screen):
        """Initializes ship and it's first position"""
        self.screen = screen

        # Loading ship image and getting a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears in screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws ship in current position"""
        self.screen.blit(self.image, self.rect)
