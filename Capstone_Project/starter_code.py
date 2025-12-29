"""
🚀 Capstone Project: Space Salvage - Starter Code
Follow the TODOs to build your first integrated game!
"""

import pygame
import random
import os

# --- 1. CONFIGURATION & SETUP ---
# Use absolute paths to ensure assets load correctly everywhere!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_FPS = 60

# Colors
SPACE_BLACK = (10, 10, 15)
NEON_GREEN = (57, 255, 20)
CRITICAL_RED = (255, 49, 49)

# --- 2. SPRITE CLASSES ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Load ship.png from ASSETS_DIR
        # TODO: Set self.image and self.rect
        # TODO: Initialize velocity variables for Momentum
        pass

    def update(self):
        # TODO: Implement 8-way movement logic
        # TODO: Apply Momentum logic (velocity)
        # TODO: Implement Screen Boundaries (Clamping)
        pass

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Load meteor.png
        # TODO: Randomize starting position and drift velocity
        pass

    def update(self):
        # TODO: Move the meteor
        # TODO: Kill the sprite if it leaves the screen
        pass

# --- 3. MAIN GAME CLASS ---

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Capstone: Space Salvage")
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.hazards = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()

        # TODO: Initialize Player and add to all_sprites
        
    def spawn_hazards(self):
        # TODO: Implement logic to spawn meteors at intervals
        pass

    def handle_collisions(self):
        # TODO: Check for Player vs Hazards
        # TODO: Check for Player vs Collectibles
        # TODO: Play sound effects on collision
        pass

    def run(self):
        while self.is_running:
            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            # 2. Update
            self.all_sprites.update()
            self.handle_collisions()
            self.spawn_hazards()

            # 3. Draw
            self.screen.fill(SPACE_BLACK)
            # TODO: Draw backgrounds, sprites, and HUD
            self.all_sprites.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(TARGET_FPS)

        pygame.quit()

# --- 4. EXECUTION ---
if __name__ == "__main__":
    # Create the engine instance and start the game
    # engine = GameEngine()
    # engine.run()
    print("Capstone Setup Complete. Ready to code!")
