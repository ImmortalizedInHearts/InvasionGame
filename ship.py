import pygame


class Ship():
    """Describes ship behavior"""

    def __init__(self, ai_settings, screen):
        """Initializes ship and it's first position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading ship image and getting a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new ship appears in screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Determination ship center coordinates(float)
        self.center = float(self.rect.centerx)
        # Moving flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship position due to flags"""
        # Updates center attribute, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updating rect attribute on the base of self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws ship in current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places ship in the center of the bottom"""
        self.center = self.screen_rect.centerx
