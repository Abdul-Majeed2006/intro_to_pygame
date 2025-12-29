""" 
🦸 Lesson 03: Sprites, Groups, and Collisions
Expected Behavior: 
A dark window titled "Lesson 03: Sprites and Collisions" will appear.
- Use ARROW KEYS or WASD to move the player (blue character).
- 5 enemies (green characters) will appear at random locations.
- When the player touches an enemy, the enemy disappears and a message is printed.
- The player cannot leave the window boundaries.
"""

import pygame
import os
import random
import sys

# 1. Initialization
pygame.init()

# 2. Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 03: Sprites and Collisions")

# 3. Path Handling
# We use an absolute base for assets to ensure the script runs regardless of the CWD.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# 4. Entities (Object-Oriented Programming)
# Inheriting from pygame.sprite.Sprite gives us 'Group' capabilities for batch processing.

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        # Load and scale the player image
        # We .convert_alpha() to ensure per-pixel transparency is optimized for the blit.
        image_path = os.path.join(ASSETS_DIR, "players", "tile_0006.png")
        raw_image_data = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image_data, (64, 64))
        
        # The 'rect' (Rectangle) handles our collision box and window position.
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.movement_speed = 7

    def update(self):
        """Handle movement logic and screen boundary clamping."""
        active_keys = pygame.key.get_pressed()
        if active_keys[pygame.K_LEFT] or active_keys[pygame.K_a]:  self.rect.x -= self.movement_speed
        if active_keys[pygame.K_RIGHT] or active_keys[pygame.K_d]: self.rect.x += self.movement_speed
        if active_keys[pygame.K_UP] or active_keys[pygame.K_w]:    self.rect.y -= self.movement_speed
        if active_keys[pygame.K_DOWN] or active_keys[pygame.K_s]:  self.rect.y += self.movement_speed
        
        # Prevent the player's 'rect' from leaving the display boundaries.
        boundary_area = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.rect.clamp_ip(boundary_area)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load enemy asset
        image_path = os.path.join(ASSETS_DIR, "players", "tile_0007.png")
        raw_image_data = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image_data, (64, 64))
        
        # Randomize start coordinates within the window limits.
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

# 5. Layer Management
# Sprites are more efficient when managed in Groups; we can update/draw 1000 items in 1 line.
active_entities_layer = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Create the hero instance
hero_sprite = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
active_entities_layer.add(hero_sprite)

# Populate world with enemies
INITIAL_ENEMY_STRENGTH = 5
for _ in range(INITIAL_ENEMY_STRENGTH):
    mob = Enemy()
    active_entities_layer.add(mob)
    enemies_group.add(mob)

# 6. Simulation Heartbeat
frame_rate_manager = pygame.time.Clock()
current_session_score = 0
is_simulation_active = True

while is_simulation_active:
    # --- Input Capture ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_simulation_active = False

    # --- Logic Synchronization ---
    # This triggers the update() method of every sprite in the layer.
    active_entities_layer.update()

    # --- Hit Detection ---
    # A 'collision' in Pygame is simply the overlapping of two 'Rect' objects.
    # We use spritecollide with 'dokill=True' to remove enemies from all groups on impact.
    detected_collisions = pygame.sprite.spritecollide(hero_sprite, enemies_group, True)
    
    for collision_hit in detected_collisions:
        current_session_score += 1
        print(f"COLLISION: Entity absorbed! Current Score: {current_session_score}")

    # --- Rendering Pipeline ---
    BACKGROUND_DARK = (30, 30, 30)
    game_window.fill(BACKGROUND_DARK)
    
    # Draw every entity onto the window surface in their current positions.
    active_entities_layer.draw(game_window)
    
    pygame.display.flip()
    frame_rate_manager.tick(60)

# 7. Hardware Release
pygame.quit()
sys.exit()
