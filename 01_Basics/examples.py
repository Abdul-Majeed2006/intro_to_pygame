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
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 01: Basics")

# 3. The Clock
# This object helps us control the timing of our game loop.
engine_clock = pygame.time.Clock()
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

# 5. The Engine Heartbeat (Game Loop)
# A game is essentially an infinite loop that processes input, updates logic, and draws.
is_engine_running = True
while is_engine_running:
    # --- Step 1: Event Handling (Input) ---
    # We must constantly flush the event queue to prevent the OS from thinking the app has frozen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_engine_running = False

    # --- Step 2: Game Logic Update ---
    # (In later modules, this is where physics and AI will live)

    # --- Step 3: Rendering (Drawing) ---
    # We use a solid background color to clear the "trails" left by the previous frame.
    MIDNIGHT_BLUE = (25, 25, 112)
    display_surface.fill(MIDNIGHT_BLUE)

    # 'Blitting' is the technical term for copying pixels from an image to the screen.
    display_surface.blit(sand_tile_image, (0, 0))

    # We use .flip() to show the finished frame. This technique (Double Buffering) 
    # prevents the user from seeing the scene being drawn part-by-part, which causes flickering.
    pygame.display.flip()
    
    # Maintain a steady heartbeat. Without this, the game would run at 1000+ FPS,
    # consuming 100% of the CPU and moving logic too fast to see.
    engine_clock.tick(TARGET_FPS)

# 6. Graceful Shutdown
# This releases hardware resources (audio, video) back to the OS.
pygame.quit()
sys.exit()
