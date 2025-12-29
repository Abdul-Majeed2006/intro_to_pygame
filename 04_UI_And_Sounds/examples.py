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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 04: UI and Sounds")

# 3. Path Handling
# We use a relative path to the local 'assets' folder to keep this chapter self-contained.
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# 4. Assets & Resources
# Using a high-quality font. We'll fall back to default if needed.
try:
    TITLE_FONT = pygame.font.SysFont("Verdana", 48, bold=True)
    BUTTON_FONT = pygame.font.SysFont("Verdana", 24)
except Exception:
    TITLE_FONT = pygame.font.Font(None, 64)
    BUTTON_FONT = pygame.font.Font(None, 32)

# Load Sfx safely
click_sfx = None
sfx_path = os.path.join(ASSETS_DIR, "Audio", "footstep_carpet_000.ogg")
if os.path.exists(sfx_path):
    try:
        click_sfx = pygame.mixer.Sound(sfx_path)
    except Exception as e:
        print(f"Warning: Failed to load click sound: {e}")

# 5. Game State
click_count = 0
is_game_running = True
clock = pygame.time.Clock()

# UI Constants
BUTTON_WIDTH = 220
BUTTON_HEIGHT = 60
BUTTON_X = (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2)
BUTTON_Y = (SCREEN_HEIGHT // 2) - (BUTTON_HEIGHT // 2)
button_rect = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

# Colors
COLOR_BG = (20, 20, 25) # Dark blue-grey
COLOR_UI_TEXT = (255, 255, 0) # Yellow
COLOR_BTN_NORMAL = (80, 80, 80)
COLOR_BTN_HOVER = (120, 120, 120)
COLOR_BTN_TEXT = (255, 255, 255)

while is_game_running:
    # Get mouse state once per frame
    mouse_coords = pygame.mouse.get_pos()
    
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left Click
                # Check if we clicked the button
                if button_rect.collidepoint(mouse_coords):
                    click_count += 1
                    if click_sfx:
                        click_sfx.play()

    # --- Rendering ---
    screen.fill(COLOR_BG)
    
    # Render the counter text
    counter_surface = TITLE_FONT.render(f"CLICKS: {click_count}", True, COLOR_UI_TEXT)
    counter_x = (SCREEN_WIDTH // 2) - (counter_surface.get_width() // 2)
    screen.blit(counter_surface, (counter_x, 80))
    
    # Render the button
    current_btn_color = COLOR_BTN_NORMAL
    if button_rect.collidepoint(mouse_coords):
        current_btn_color = COLOR_BTN_HOVER
    
    # Draw button background
    pygame.draw.rect(screen, current_btn_color, button_rect, border_radius=10)
    
    # Draw button text (pre-rendered for efficiency if this were a large game)
    btn_text_surface = BUTTON_FONT.render("CLICK ME", True, COLOR_BTN_TEXT)
    btn_text_x = button_rect.centerx - (btn_text_surface.get_width() // 2)
    btn_text_y = button_rect.centery - (btn_text_surface.get_height() // 2)
    screen.blit(btn_text_surface, (btn_text_x, btn_text_y))

    # Update display
    pygame.display.flip()
    
    # Limit frame rate
    clock.tick(60)

# 6. Clean Exit
pygame.quit()
sys.exit()
