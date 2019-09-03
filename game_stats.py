class GameStats():
    """Tracking statistics for the game Alien Invasion"""

    def __init__(self, ai_settings):
        """Initializes statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Game Alien Invasion starts up in inactive condition
        self.game_active = False

    def reset_stats(self):
        """Initializes statistic, witch changing during the game"""
        self.ships_left = self.ai_settings.ship_limit
