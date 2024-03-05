class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Black background
        self.bg_color = (0, 0, 0)
        # Limit the number of ships a player starts with
        self.ship_limit = 3
        # Bullet settings - orange bullets
        self.bullet_speed = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 165, 0)
        # Limit the number of bullets at a time
        self.bullets_allowed = 10

    def initialize_dynamic_settings(self):
        # Settings that change throughout the game
        self.ship_speed = 5
        self.bullet_speed = 3

    def increase_speed(self):
        # Increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale