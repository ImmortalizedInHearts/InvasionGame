class Settings():
    """Stores all game settings"""

    def __init__(self):
        """Initializes game settings"""
        # Screen parameters
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

        # Ship parameters
        self.ship_speed_factor = 1.5
