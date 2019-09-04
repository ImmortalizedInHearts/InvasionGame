class Settings():
    """Stores all game settings"""

    def __init__(self):
        """Initializes static game settings"""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship parameters
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # Alien parameters
        self.fleet_drop_speed = 10

        # Game acceleration pace
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 moves right; -1 left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
