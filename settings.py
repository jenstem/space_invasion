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
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        # Alien settings
        self.alien_speed = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Settings that change throughout the game
        self.ship_speed = 5
        self.bullet_speed = 3
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        # Increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)