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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lesson 02: Inputs")

# 3. Handle Controller Discovery
# We create a list of all detected joysticks and initialize them.
connected_joysticks = []
for i in range(pygame.joystick.get_count()):
    joy = pygame.joystick.Joystick(i)
    joy.init()
    connected_joysticks.append(joy)

# 4. Timer Setup
clock = pygame.time.Clock()
TARGET_FPS = 60

# 5. Core Game Loop
is_running = True
while is_running:
    # --- A. EVENT HANDLING (Discrete Actions) ---
    # Use the Event Loop for things that happen ONCE per press (e.g., Jumping, Pausing).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("ACTION: Spacebar pressed (Triggered once via Event Loop)")
            if event.key == pygame.K_ESCAPE:
                is_running = False

    # --- B. STATE CHECKING / POLLING (Continuous Actions) ---
    # Use get_pressed() for things that happen AS LONG AS a key is held (e.g., Running, Steering).
    keys_state = pygame.key.get_pressed()
    if keys_state[pygame.K_w] or keys_state[pygame.K_UP]:
        # Note: This will spam if left unchecked, usually you'd move a character here.
        pass 

    # --- C. MOUSE INPUT ---
    current_mouse_pos = pygame.mouse.get_pos()
    mouse_buttons_state = pygame.mouse.get_pressed()
    
    if mouse_buttons_state[0]: # Index 0 is the Left Mouse Button
        print(f"INPUT: Mouse Left Click at {current_mouse_pos}")

    # --- D. CONTROLLER INPUT ---
    for joystick in connected_joysticks:
        # Check basic buttons (usually button 0 is 'A' or 'Cross')
        if joystick.get_button(0):
            print(f"INPUT: Button 0 pressed on {joystick.get_name()}")

    # --- RENDERING ---
    BACKGROUND_COLOR = (50, 50, 50) # Dark Charcoal
    screen.fill(BACKGROUND_COLOR)
    
    # Visual Feedback: Draw a white circle tracking the mouse.
    POINTER_COLOR = (255, 255, 255)
    POINTER_RADIUS = 12
    pygame.draw.circle(screen, POINTER_COLOR, current_mouse_pos, POINTER_RADIUS)

    pygame.display.flip()
    
    # Maintain constant speed
    clock.tick(TARGET_FPS)

# 6. Clean Exit
pygame.quit()
sys.exit()
