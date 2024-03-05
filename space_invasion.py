import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

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

        # Start Space Invasion in an inactive state
        self.game_active = False

        # Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # Start a new game when the player clicks Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()

    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

if __name__ == '__main__':
    ai = SpaceInvasion()
    ai.run_game()