import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

from ship import Ship
from bullet import Bullet

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
        # Group that holds the bullets
        self.bullets = pygame.sprite.Group()

        # Start Space Invasion in an inactive state
        self.game_active = False

        # Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()

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

            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets
            self.bullets.empty()

            # Center the ship
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # Fire a bullet when the space bar is pressed
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _fire_bullet(self):
        # Add new bullets to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
            # Update bullet positions
            self.bullets.update()

            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _ship_hit(self):
        #Respond to the ship being hit by an alien
        if self.stats.ships_left > 0:
        # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets
            self.bullets.empty()

    def _update_screen(self):
        # Update images on the screen
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

if __name__ == '__main__':
    ai = SpaceInvasion()
    ai.run_game()