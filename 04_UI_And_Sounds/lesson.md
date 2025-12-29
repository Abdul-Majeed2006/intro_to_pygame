# 🎵 Lesson 04: UI and Sounds

A game that looks good but feels "empty" is missing the **Juice**. In this lesson, we add audio feedback and user interfaces to transform a project into a professional product.

## 1. The Theory: State Machines

How does a game know to show the "Main Menu" instead of the "Game Over" screen? We use a **State Machine**.

A State Machine is just a way to manage the current "Mode" of your game.

- Initial State: `playing = False`, `menu = True`.
- Trigger: User clicks "Start".
- New State: `playing = True`, `menu = False`.

By checking `if current_state == "PLAYING":`, you decide exactly which update and draw logic to run.

## 2. Implementation: Audio Feedback 🎧

Pygame's `mixer` module handles everything from background music to sound effects.

```python
# Initialization (usually done once at the top)
pygame.mixer.init()

# Sound Effects (Small files, played often)
jump_sfx = pygame.mixer.Sound("assets/Audio/jump.ogg")
jump_sfx.play()

# Music (Large files, streamed)
pygame.mixer.music.load("assets/Audio/background.mp3")
pygame.mixer.music.play(-1) # -1 means loop forever
```

## 3. Dynamic UI and Fonts ✍️

User Interfaces (UIs) communicate information like scores, health, and menus.

```python
# 1. Load a font
font = pygame.font.SysFont("Verdana", 32)

# 2. Render text into an image (Surface)
text_surface = font.render(f"Score: {score}", True, (255, 255, 255))

# 3. Blit onto screen
screen.blit(text_surface, (20, 20))
```

## 4. UI Interaction: Buttons

A professional button isn't just an image; it's a `Rect` that reacts to the mouse.

```python
button_rect = pygame.Rect(300, 250, 200, 50)

# Check for hover
if button_rect.collidepoint(pygame.mouse.get_pos()):
    draw_color = (255, 0, 0) # Highlight red
```

---

---

## 🛠️ Action: Mini-Exercise

Add the final "Juice" to your game! Head to the [Module 04 Exercise](./exercise.md) to implement a pause menu.

