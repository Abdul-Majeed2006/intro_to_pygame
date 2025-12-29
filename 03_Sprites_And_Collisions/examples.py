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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 03: Sprites and Collisions")

# 3. Path Handling
# We use a relative path to the local 'assets' folder to keep this chapter self-contained.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# 4. Classes (Object-Oriented Programming)
# Inheriting from pygame.sprite.Sprite gives us powerful group management tools.

class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        # Load and scale the player image
        image_path = os.path.join(ASSETS_DIR, "players", "tile_0006.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (64, 64))
        
        # The 'rect' is used for position and collision detection
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.movement_speed = 7

    def update(self):
        """Handle movement and screen boundaries."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  self.rect.x -= self.movement_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.rect.x += self.movement_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:    self.rect.y -= self.movement_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  self.rect.y += self.movement_speed
        
        # Clamp the player inside the window so they can't fly away!
        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.rect.clamp_ip(screen_rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load a different image for the enemy
        image_path = os.path.join(ASSETS_DIR, "players", "tile_0007.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (64, 64))
        
        # Randomize starting position
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

# 5. Sprite Management
# Putting sprites in Groups allows us to update and draw them with one line of code.
all_sprites_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Create the player instance
player_character = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites_group.add(player_character)

# Spawn a few enemies
INITIAL_ENEMY_COUNT = 5
for _ in range(INITIAL_ENEMY_COUNT):
    new_enemy = Enemy()
    all_sprites_group.add(new_enemy)
    enemies_group.add(new_enemy)

# 6. Core Game Loop
clock = pygame.time.Clock()
current_score = 0
is_game_running = True

while is_game_running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    # --- Update ---
    # This automatically calls update() on every sprite in the group.
    all_sprites_group.update()

    # --- Collision Detection ---
    # spritecollide checks if one sprite touches any sprite in a group.
    # The 'True' parameter means "delete the enemy from all groups if it's hit".
    collision_hits = pygame.sprite.spritecollide(player_character, enemies_group, True)
    
    for hit in collision_hits:
        current_score += 1
        print(f"COLLISION: Hit enemy! Current Score: {current_score}")

    # --- Rendering ---
    BACKGROUND_COLOR = (30, 30, 30) # Dark grey
    screen.fill(BACKGROUND_COLOR)
    
    # Draw all sprites at once
    all_sprites_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

# 7. Clean Exit
pygame.quit()
sys.exit()
