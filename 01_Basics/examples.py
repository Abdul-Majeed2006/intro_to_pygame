""" 
🚀 Lesson 01: The Heartbeat of a Game (The Game Loop)
Expected Behavior: 
A window titled "Lesson 01: Basics" will appear with a midnight blue background. 
A single sand tile will be drawn in the top-left corner.
Closing the window will safely terminate the program.
"""

import pygame
import os
import sys

# 1. Initialization
# We must initialize pygame to use its modules (graphics, sound, etc.)
pygame.init()

# 2. Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 01: Basics")

# 3. The Clock
# This object helps us control the speed of our game.
clock = pygame.time.Clock()
TARGET_FPS = 60

# 4. Asset Loading
# We use a relative path to the local 'assets' folder.
# This makes the chapter self-contained.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

try:
    sand_tile_image = pygame.image.load(os.path.join(ASSETS_DIR, "bg", "tile_0055.png")).convert_alpha()
except FileNotFoundError:
    print(f"Error: Could not find assets in {ASSETS_DIR}.")
    pygame.quit()
    sys.exit()

# 5. Core Game Loop
# A game is essentially an infinite loop that processes input, updates logic, and draws.
is_game_running = True
while is_game_running:
    # --- Event Processing ---
    # We must listen for "Events" (like clicking the 'X' to quit).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    # --- Game Logic Update ---
    # (This is where movement and physics calculations would happen)

    # --- Rendering (Drawing) ---
    # We always clear the screen first.
    BACKGROUND_COLOR = (25, 25, 112) # Midnight Blue
    screen.fill(BACKGROUND_COLOR)

    # Draw our image at the top-left (0, 0)
    screen.blit(sand_tile_image, (0, 0))

    # CHALLENGE FOR YOU: 
    # Use a nested 'for' loop to fill the entire screen with sand_tile_image!
    # Hint: Get the image size with sand_tile_image.get_width() and loop through SCREEN_WIDTH.

    # After drawing everything, we "flip" the display to show the new frame.
    pygame.display.flip()
    
    # Maintain a steady heartbeat (60 frames per second).
    clock.tick(TARGET_FPS)

# 6. Clean Exit
pygame.quit()
sys.exit()
