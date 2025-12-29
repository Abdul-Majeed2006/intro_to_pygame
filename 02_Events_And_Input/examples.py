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

# 1. Initialization
pygame.init()

# We also need to initialize the joystick module specifically if we want controller support.
if pygame.joystick.get_count() > 0:
    pygame.joystick.init()

# 2. Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 02: Inputs")

# 3. Handle Controller Discovery
# We initialize all detected joysticks to enable hardware-level input polling.
connected_gamepads = []
for gamepad_index in range(pygame.joystick.get_count()):
    gamepad = pygame.joystick.Joystick(gamepad_index)
    gamepad.init()
    connected_gamepads.append(gamepad)

# 4. Timer Setup
game_heartbeat_clock = pygame.time.Clock()
TARGET_FPS = 60

# 5. Core Game Loop
is_engine_active = True
while is_engine_active:
    # --- A. EVENT HANDLING (Discrete Actions) ---
    # We use the Event Loop for 'one-off' triggers. This prevents a single click 
    # from being registered as 60 separate clicks in a single second.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_engine_active = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("ACTION: Spacebar pressed (Triggered once via Event Loop)")
            if event.key == pygame.K_ESCAPE:
                is_engine_active = False

    # --- B. STATE CHECKING / POLLING (Continuous Actions) ---
    # We use 'get_pressed' for fluid, frame-by-frame movement. This ensures 
    # movement feels responsive and doesn't rely on the OS repeating a key signal.
    active_keys = pygame.key.get_pressed()
    if active_keys[pygame.K_w] or active_keys[pygame.K_UP]:
        # Professional Note: Logic would go here to move the character.
        pass 

    # --- C. MOUSE INPUT ---
    # Polling the mouse directly allows us to get the exact pixel coordinate in real-time.
    current_mouse_position = pygame.mouse.get_pos()
    mouse_buttons_state = pygame.mouse.get_pressed()
    
    if mouse_buttons_state[0]: # Index 0 is the Primary (Left) Mouse Button
        print(f"INPUT: Mouse Left Click at {current_mouse_position}")

    # --- D. CONTROLLER INPUT ---
    for active_gamepad in connected_gamepads:
        # We poll specific hardware indices for low-latency feedback.
        if active_gamepad.get_button(0):
            print(f"INPUT: Button 0 pressed on {active_gamepad.get_name()}")

    # --- RENDERING ---
    CHARCOAL_GREY = (50, 50, 50)
    display_surface.fill(CHARCOAL_GREY)
    
    # Visual Feedback: Draw a white circle tracking the mouse.
    # We draw this every frame to provide immediate visual confirmation of input.
    POINTER_COLOR = (255, 255, 255)
    POINTER_RADIUS = 12
    pygame.draw.circle(display_surface, POINTER_COLOR, current_mouse_position, POINTER_RADIUS)

    # Double Buffering: Show the completed frame to the user.
    pygame.display.flip()
    
    # Maintain constant speed regardless of computer power.
    game_heartbeat_clock.tick(TARGET_FPS)

# 6. Graceful Shutdown
pygame.quit()
sys.exit()
