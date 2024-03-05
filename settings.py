class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Black background
        self.bg_color = (0, 0, 0)
        # Limit the number of ships a player starts with
        self.ship_limit = 3

    def initialize_dynamic_settings(self):
        # Settings that change throughout the game
        self.ship_speed = 5