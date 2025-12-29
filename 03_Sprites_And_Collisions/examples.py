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

# --- 1. VERSION GUARD ---
if sys.version_info < (3, 10):
    print("CRITICAL: Python 3.10+ is required.")
    sys.exit(1)

# 2. Entities (Object-Oriented Programming)
class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, assets_dir, screen_width, screen_height):
        super().__init__()
        image_path = os.path.join(assets_dir, "players", "tile_0006.png")
        raw_image_data = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image_data, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.movement_speed = 7
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        active_keys = pygame.key.get_pressed()
        if active_keys[pygame.K_LEFT] or active_keys[pygame.K_a]:  self.rect.x -= self.movement_speed
        if active_keys[pygame.K_RIGHT] or active_keys[pygame.K_d]: self.rect.x += self.movement_speed
        if active_keys[pygame.K_UP] or active_keys[pygame.K_w]:    self.rect.y -= self.movement_speed
        if active_keys[pygame.K_DOWN] or active_keys[pygame.K_s]:  self.rect.y += self.movement_speed
        
        boundary_area = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.rect.clamp_ip(boundary_area)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, assets_dir, screen_width, screen_height):
        super().__init__()
        image_path = os.path.join(assets_dir, "players", "tile_0007.png")
        raw_image_data = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image_data, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)

def run_lesson():
    """ Orchestrates sprite-based entity management and collision detection. """
    
    # 3. Initialization
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lesson 03: Sprites and Collisions")

    # 4. Path Handling
    ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

    # 5. Layer Management
    active_entities_layer = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()

    hero_sprite = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, ASSETS_DIR, SCREEN_WIDTH, SCREEN_HEIGHT)
    active_entities_layer.add(hero_sprite)

    for _ in range(5):
        mob = Enemy(ASSETS_DIR, SCREEN_WIDTH, SCREEN_HEIGHT)
        active_entities_layer.add(mob)
        enemies_group.add(mob)

    # 6. Simulation Heartbeat
    frame_rate_manager = pygame.time.Clock()
    current_session_score = 0
    is_simulation_active = True

    while is_simulation_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_simulation_active = False

        active_entities_layer.update()

        # Hit Detection
        detected_collisions = pygame.sprite.spritecollide(hero_sprite, enemies_group, True)
        for collision_hit in detected_collisions:
            current_session_score += 1
            print(f"COLLISION: Entity absorbed! Current Score: {current_session_score}")

        # Rendering
        BACKGROUND_DARK = (30, 30, 30)
        game_window.fill(BACKGROUND_DARK)
        active_entities_layer.draw(game_window)
        
        pygame.display.flip()
        frame_rate_manager.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_lesson()
