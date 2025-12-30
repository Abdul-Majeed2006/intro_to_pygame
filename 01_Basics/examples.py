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

# --- 1. VERSION GUARD ---
# We enforce Python 3.10+ for modern features like structural pattern matching.
if sys.version_info < (3, 10):
    print("CRITICAL: Python 3.10 or higher is required to run this lesson.")
    sys.exit(1)

def run_lesson():
    """ 
    The Main Entry Point for Lesson 01.
    Encapsulating logic in a function prevents 'Global Spaghetti' and keeps the namespace clean.
    """
    
    # 2. Initialization
    pygame.init()

    # 3. Window Setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lesson 01: Basics")

    # 4. The Clock
    engine_clock = pygame.time.Clock()
    TARGET_FPS = 60

    # 5. Asset Loading
    # Absolute path construction ensures the script runs from any directory.
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")

    try:
        sand_tile_path = os.path.join(ASSETS_DIR, "bg", "tile_0055.png")
        sand_tile_image = pygame.image.load(sand_tile_path).convert_alpha()
    except FileNotFoundError:
        print(f"Error: Could not find assets in {ASSETS_DIR}.")
        pygame.quit()
        return

    # 6. The Engine Heartbeat (Game Loop)
    is_engine_running = True
    
    # Define colors outside the loop to avoid re-creation every frame.
    MIDNIGHT_BLUE = (25, 25, 112)

    while is_engine_running:
        # --- Step 1: Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_engine_running = False

        # --- Step 2: Rendering ---
        # Wipe the screen clean every frame (Painter's Algorithm)
        display_surface.fill(MIDNIGHT_BLUE)

        # Draw the tile at coordinate (0, 0)
        display_surface.blit(sand_tile_image, (0, 0))

        # Show the finished frame (Double Buffering)
        # We draw to a back buffer, then flip it to the front to avoid partial rendering artifacts.
        pygame.display.flip()
        
        # Maintain steady heartbeat
        # This prevents the game from running too fast (burning CPU) or too variable.
        engine_clock.tick(TARGET_FPS)

    # 7. Graceful Shutdown
    pygame.quit()

if __name__ == "__main__":
    run_lesson()
