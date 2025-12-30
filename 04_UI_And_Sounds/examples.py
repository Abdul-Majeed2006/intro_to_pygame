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

# --- 1. VERSION GUARD ---
if sys.version_info < (3, 10):
    print("CRITICAL: Python 3.10+ is required.")
    sys.exit(1)

def run_lesson():
    """ 
    Orchestrates UI layout, event handling, and reactive audio.
    Encapsulation ensures resources are cleaned up correctly in order.
    """
    
    # 2. Initialization
    pygame.init()

    # Graceful Audio Initialization
    try:
        pygame.mixer.init()
    except pygame.error:
        print("Warning: Audio system failed. Running in silent mode.")

    # 3. Window Setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    main_display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lesson 04: UI and Sounds")

    # 4. Assets & Resources
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")

    # Fonts
    try:
        TITLE_FACE = pygame.font.SysFont("Verdana", 48, bold=True)
        BUTTON_FACE = pygame.font.SysFont("Verdana", 24)
    except Exception:
        TITLE_FACE = pygame.font.Font(None, 64)
        BUTTON_FACE = pygame.font.Font(None, 32)

    # Audio
    interaction_sfx = None
    sfx_path = os.path.join(ASSETS_DIR, "Audio", "footstep_carpet_000.ogg")
    if os.path.exists(sfx_path):
        try:
            interaction_sfx = pygame.mixer.Sound(sfx_path)
        except Exception as e:
            print(f"Warning: Audio error: {e}")

    # 5. UI Layout & State
    interaction_count = 0
    is_engine_active = True
    clock = pygame.time.Clock()

    BUTTON_RECT = pygame.Rect((SCREEN_WIDTH // 2) - 110, (SCREEN_HEIGHT // 2) - 30, 220, 60)

    # 6. Professional Palette (Defined once)
    MIDNIGHT = (20, 20, 25) 
    HIGHLIGHT = (255, 255, 0)
    IDLE_BROWN = (80, 80, 80)
    ACTIVE_BROWN = (120, 120, 120)

    # 7. Pre-Render Static UI (Performance Tip)
    # Don't render static text inside the game loop! It eats CPU unnecessarily.
    static_button_label = BUTTON_FACE.render("CLICK ME", True, (255, 255, 255))
    label_x = BUTTON_RECT.centerx - static_button_label.get_width() // 2
    label_y = BUTTON_RECT.centery - static_button_label.get_height() // 2

    while is_engine_active:
        mouse_pos = pygame.mouse.get_pos()
        
        # --- Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_engine_active = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and BUTTON_RECT.collidepoint(mouse_pos):
                    interaction_count += 1
                    if interaction_sfx: interaction_sfx.play()

        # --- Render ---
        main_display_surface.fill(MIDNIGHT)
        
        # Counter Overlay (Dynamic Text must be re-rendered)
        score_surf = TITLE_FACE.render(f"CLICKS: {interaction_count}", True, HIGHLIGHT)
        main_display_surface.blit(score_surf, (SCREEN_WIDTH // 2 - score_surf.get_width() // 2, 80))
        
        # Button Logic
        btn_color = ACTIVE_BROWN if BUTTON_RECT.collidepoint(mouse_pos) else IDLE_BROWN
        pygame.draw.rect(main_display_surface, btn_color, BUTTON_RECT, border_radius=10)
        
        # Use the pre-rendered label
        main_display_surface.blit(static_button_label, (label_x, label_y))

        pygame.display.flip()
        clock.tick(60)

    # 6. Cleanup
    pygame.quit()

if __name__ == "__main__":
    run_lesson()
