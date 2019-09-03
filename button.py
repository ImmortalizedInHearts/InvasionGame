import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initializes button atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Assignment of sizes and properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Building 'rect' object of button and
        # alignment it on center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message will be create only one time
        self.prep_msg(msg)
