class Settings():
    """Stores all game settings"""

    def __init__(self):
        """Initializes game settings"""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship parameters
        self.ship_speed_factor = 1.5

        # Bullet parameters
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5
