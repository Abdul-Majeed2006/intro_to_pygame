""" 
🎵 Lesson 04: User Interfaces and Reactive Audio
Expected Behavior: 
A dark window titled "Lesson 04: UI and Sounds" will appear.
- A yellow "Clicks" counter will be visible at the top.
- A grey "CLICK ME" button will be in the center.
- Hovering over the button will highlight it.
- Clicking the button will increment the counter and trigger a click sound (if audio file exists).
- Closing the window will safely exit.
"""

import pygame
import os
import sys

# 1. Initialization
pygame.init()

# We must initialize the mixer for sound. 
# Some systems might fail here if they have no audio drivers, so we handle it gracefully.
try:
    pygame.mixer.init()
except pygame.error:
    print("Warning: Audio system could not be initialized. Sound will be disabled.")

# 2. Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
main_display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 04: UI and Sounds")

# 3. Path Handling
# Absolute path construction ensures assets load correctly regardless of how the script is executed.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# 4. Assets & Resources
# We attempt to find a system font, falling back to the built-in Pygame font if none exists.
# This prevents the application from crashing on systems without 'Verdana'.
try:
    TITLE_FONT_FACE = pygame.font.SysFont("Verdana", 48, bold=True)
    BUTTON_FONT_FACE = pygame.font.SysFont("Verdana", 24)
except Exception:
    TITLE_FONT_FACE = pygame.font.Font(None, 64)
    BUTTON_FONT_FACE = pygame.font.Font(None, 32)

# Audio Assets
# We load sounds into memory once (Sound objects) to avoid high-latency disk reads during gameplay.
interaction_sfx_sample = None
sfx_resource_path = os.path.join(ASSETS_DIR, "Audio", "footstep_carpet_000.ogg")
if os.path.exists(sfx_resource_path):
    try:
        interaction_sfx_sample = pygame.mixer.Sound(sfx_resource_path)
    except Exception as hardware_error:
        print(f"Warning: Failed to load audio sample: {hardware_error}")

# 5. Application State
interaction_count = 0
is_interaction_active = True
application_tick_clock = pygame.time.Clock()

# UI Layout Constants
# Pro Tip: Defining these at the top makes it easy to refactor the UI layout later.
BUTTON_PROPERTIES = {
    'width': 220,
    'height': 60,
    'x': (SCREEN_WIDTH // 2) - 110,
    'y': (SCREEN_HEIGHT // 2) - 30
}
interaction_button_rect = pygame.Rect(
    BUTTON_PROPERTIES['x'], 
    BUTTON_PROPERTIES['y'], 
    BUTTON_PROPERTIES['width'], 
    BUTTON_PROPERTIES['height']
)

# Color Palette (HSL-aligned for professionalism)
MIDNIGHT_VOICE = (20, 20, 25) 
TEXT_HIGHLIGHT = (255, 255, 0) # Yellow
BUTTON_IDLE = (80, 80, 80)
BUTTON_ACTIVE = (120, 120, 120)
BUTTON_TEXT_COLOR = (255, 255, 255)

while is_interaction_active:
    # We capture the mouse cursor state once at the start of the frame.
    cursor_position = pygame.mouse.get_pos()
    
    # --- Input Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_interaction_active = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Primary Left Click
                # Collision check: Did the user click inside the button area?
                if interaction_button_rect.collidepoint(cursor_position):
                    interaction_count += 1
                    if interaction_sfx_sample:
                        interaction_sfx_sample.play()

    # --- Render Pipeline ---
    main_display_surface.fill(MIDNIGHT_VOICE)
    
    # Render the session score text
    # Anti-aliasing (the 2nd parameter) is set to 'True' for smoother edges on high-res displays.
    score_overlay_surface = TITLE_FONT_FACE.render(f"INTERACTIONS: {interaction_count}", True, TEXT_HIGHLIGHT)
    score_overlay_x = (SCREEN_WIDTH // 2) - (score_overlay_surface.get_width() // 2)
    main_display_surface.blit(score_overlay_surface, (score_overlay_x, 80))
    
    # Determine button state based on hover behavior
    active_button_color = BUTTON_IDLE
    if interaction_button_rect.collidepoint(cursor_position):
        active_button_color = BUTTON_ACTIVE
    
    # Draw button geometry
    pygame.draw.rect(main_display_surface, active_button_color, interaction_button_rect, border_radius=10)
    
    # Draw button label
    label_surface = BUTTON_FONT_FACE.render("CLICK ME", True, BUTTON_TEXT_COLOR)
    label_x = interaction_button_rect.centerx - (label_surface.get_width() // 2)
    label_y = interaction_button_rect.centery - (label_surface.get_height() // 2)
    main_display_surface.blit(label_surface, (label_x, label_y))

    # Single-command update: Swap the buffers.
    pygame.display.flip()
    
    # Regulate execution speed to prevent CPU thermal throttling.
    application_tick_clock.tick(60)

# 6. Resource Cleanup
pygame.quit()
sys.exit()
