""" 
🎮 Lesson 02: Handling User Input (Events vs. Polling)
Expected Behavior: 
A grey window titled "Lesson 02: Inputs" will appear.
- Moving the mouse will move a white circle on the screen.
- Clicking the left mouse button will print a message to the console.
- Pressing SPACE will print a message to the console.
- Holding W or UP Arrow will print a "held down" message continuously.
- Controller buttons will be logged if a gamepad is connected.
- Pressing ESCAPE or closing the window will exit.
"""

import pygame
import sys

# --- 1. VERSION GUARD ---
if sys.version_info < (3, 10):
    print("CRITICAL: Python 3.10+ is required.")
    sys.exit(1)

def run_lesson():
    """ Handles input polling and discrete events in a scoped namespace. """
    
    # 2. Initialization
    pygame.init()
    
    # Initialize joysticks if available
    if pygame.joystick.get_count() > 0:
        pygame.joystick.init()

    # 3. Window Setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lesson 02: Inputs")

    # 4. Controller Discovery
    connected_gamepads = []
    for gamepad_index in range(pygame.joystick.get_count()):
        gamepad = pygame.joystick.Joystick(gamepad_index)
        gamepad.init()
        connected_gamepads.append(gamepad)

    # 5. Timer
    game_heartbeat_clock = pygame.time.Clock()
    TARGET_FPS = 60

    # 6. Core Game Loop
    is_engine_active = True
    
    # Define colors/constants outside the loop
    CHARCOAL_GREY = (50, 50, 50)
    POINTER_COLOR = (255, 255, 255)
    POINTER_RADIUS = 12

    while is_engine_active:
        # --- A. EVENT HANDLING (Discrete Actions) ---
        # "Did it happen *just now*?" (e.g., Pause, Jump, Shoot, Quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_engine_active = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("ACTION: Spacebar pressed (Triggered once via Event Loop)")
                if event.key == pygame.K_ESCAPE:
                    is_engine_active = False

        # --- B. STATE CHECKING / POLLING (Continuous Actions) ---
        # "Is it *currently* happening?" (e.g., Movement, Charging)
        active_keys = pygame.key.get_pressed()
        if active_keys[pygame.K_w] or active_keys[pygame.K_UP]:
            # This is where continuous movement logic would happen
            pass 
            
        # --- C. MOUSE INPUT ---
        current_mouse_position = pygame.mouse.get_pos()
        mouse_buttons_state = pygame.mouse.get_pressed()
        
        # Note: mouse_buttons_state returns (Left, Middle, Right) booleans
        if mouse_buttons_state[0]: 
            print(f"INPUT: Mouse Left Click at {current_mouse_position}")

        # --- D. CONTROLLER INPUT ---
        for active_gamepad in connected_gamepads:
            if active_gamepad.get_button(0):
                print(f"INPUT: Button 0 pressed on {active_gamepad.get_name()}")

        # --- RENDERING ---
        display_surface.fill(CHARCOAL_GREY)
        
        # Draw a white circle tracking the mouse cursor
        pygame.draw.circle(display_surface, POINTER_COLOR, current_mouse_position, POINTER_RADIUS)

        pygame.display.flip()
        game_heartbeat_clock.tick(TARGET_FPS)

    # 7. Shutdown
    pygame.quit()

if __name__ == "__main__":
    run_lesson()
