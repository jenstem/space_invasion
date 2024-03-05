import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard

from ship import Ship

class SpaceInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Invasion")

        # Store game statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)

        # Reset the game statistics.
        self.stats.reset_stats()
        self.sb.prep_ships()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _ship_hit(self):
        #Respond to the ship being hit by an alien
        if self.stats.ships_left > 0:
        # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

    def _update_screen(self):
        # Update images on the screen
        self.screen.fill(self.settings.bg_color)

        # Draw the score information
        self.sb.show_score()

if __name__ == '__main__':
    ai = SpaceInvasion()
    ai.run_game()