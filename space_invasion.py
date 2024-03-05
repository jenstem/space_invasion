import sys
from time import sleep
import pygame

from settings import Settings

class SpaceInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Invasion")

        # Reset the game statistics.
        self.stats.reset_stats()
        self.sb.prep_ships()

    def _ship_hit(self):
        #Respond to the ship being hit by an alien
        if self.stats.ships_left > 0:
        # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

if __name__ == '__main__':
    ai = SpaceInvasion()
    ai.run_game()