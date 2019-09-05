import pygame.font


class Scoreboard():
    """Class of displaying game information"""
    def __init__(self, ai_settings, screen, stats):
        """Initializes scoring attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Source image preparation
        self.prep_score()

    def prep_score(self):
        """Converts current score into graphic image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Displaying score in right top corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displays score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
