import os


class GameStats():
    """Tracking statistics for the game Alien Invasion"""

    def __init__(self, ai_settings):
        """Initializes statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # High score should not be reset
        if os.path.isfile('./high_score.txt'):
            with open('high_score.txt', 'r', encoding='utf-8') as hs:
                self.high_score = int(hs.read())
        else:
            self.high_score = 0

        # Game Alien Invasion starts up in inactive condition
        self.game_active = False

    def reset_stats(self):
        """Initializes statistic, witch changing during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
