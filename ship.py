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

        # Moving flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship position due to flags"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draws ship in current position"""
        self.screen.blit(self.image, self.rect)
