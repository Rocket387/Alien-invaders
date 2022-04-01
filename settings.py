class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #ship settings
        self.ship_speed = 0.5

        #alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        #fleet_direction of 1 resrepsents right; -1 represents left
        self.fleet_direction = -1