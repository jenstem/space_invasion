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

if __name__ == '__main__':
    ai = SpaceInvasion()
    ai.run_game()