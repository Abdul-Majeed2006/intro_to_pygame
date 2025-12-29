# 🌵 Lesson 01: The Game Engine Foundation

Building a game is different from building a standard app. In a normal app, the computer waits for you to do something. In a game, the world keeps moving even if you stand still. This is powered by the **Game Loop**.

## 1. The Theory: What is a Game Engine?

At its core, a game engine is an infinite loop that runs as fast as possible (usually 60 times per second).

- **The Heartbeat (FPS)**: Frames Per Second. If your game runs at 60 FPS, the entire game state is calculated and redrawn every 16.6 milliseconds.
- **The Surface**: Think of the game window as a digital canvas. We don't "move" objects; we erase the whole canvas and redraw everything in new positions.

## 2. Implementation: Setting the Stage

To start, we initialize Pygame and create our canvas (the `screen`).

```python
import pygame

# Initialize all pygame modules (audio, display, etc.)
pygame.init()

# Create the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game! 🚀")

# The Clock controls our "heartbeat"
clock = pygame.time.Clock()
```

## 3. The Game Loop: Input -> Update -> Draw

Every professional game loop follows this 3-step rhythm:

1. Handle Events: Read inputs from the user (keyboard, mouse, quit).
2. Update Logic: Calculate where objects should move.
3. Draw (Render): Paint the new frame onto the screen.

```python
running = True
while running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update Logic (Movement/Physics goes here)

    # 3. Drawing
    screen.fill((25, 25, 112)) # Erase screen with Midnight Blue
    
    # After drawing, we MUST "flip" the display to show the new frame
    pygame.display.flip()

    # Maintain a steady 60 FPS
    clock.tick(60)

pygame.quit()
```

## 4. Drawing and "Blitting"

"Blitting" (Block Image Transfer) is the technical term for copying pixels from an image file onto your screen.

> [!NOTE]
> **Coordinate System**: In Pygame, `(0, 0)` is the **Top-Left**. Increasing `y` moves an object **DOWN**, not up.

### Loading & Positioning

We use **Rects** (Rectangles) to handle positioning. Instead of doing complex math, we tell the Rect where its `center` or `topleft` should be.

```python
# Load image and optimize it for the display
image = pygame.image.load("assets/bg/tile_0055.png").convert_alpha()

# Get the bounding box (Rect)
rect = image.get_rect()
rect.center = (400, 300) # Snap to middle of screen
```

---

## 🛠️ Action: Mini-Exercise

**Goal**: Transform a blank screen into a textured environment.

1. Open [examples.py](file:///c:/Users/m287110/Desktop/Git/Personal_projects/Learning_python/intro_to_pygame/01_Basics/examples.py).
2. Inside the drawing section, implement a **Nested Loop** that tiles the entire screen with the `sand_tile_image`.
3. **Bonus**: Change the `TARGET_FPS` to `10` and then `120`. Observe how the "smoothness" of the window changes.

**Check your progress**: Once you can see a full desert floor, you're ready for Module 02.
