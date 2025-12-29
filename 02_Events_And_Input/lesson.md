# 🎮 Lesson 02: Events and Input

Games are conversational. The player sends a command, and the game responds. In technical terms, we handle this through **Event Processing** and **State Polling**.

## 1. The Theory: Handling vs. Polling

There are two ways to read the player's mind:

1. Handling (Discrete): "Something just happened." Use this for one-time triggers like jumping, firing once, or clicking a menu button.
2. State Polling (Continuous): "What is the state right now?" Use this for continuous actions like walking, steering a car, or looking around.

## 2. Implementation: The Keyboard

### The Event Loop (Handling)

This captures a single "Ping" from the keyboard.

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Jump Triggered!")
```

### State Checking (Polling)

This checks if a key is held down during the current frame.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_w] or keys[pygame.K_UP]:
    player_y -= player_speed
```

## 3. Advanced Input: Mouse & Gamepads

### The Mouse 🐭

The mouse is reactive. You can track its `(x, y)` position or its button states.

- Position: `pygame.mouse.get_pos()`
- Click: `pygame.mouse.get_pressed()[0]` (Left Click)

### Gamepads (Joysticks) 🕹️

Using a controller requires initialization.

- Init: `pygame.joystick.init()`
- Check: `joy.get_button(0)` for the 'A' or 'Cross' button.

## 4. Engineering Tip: Input Abstraction

Don't write `if keys[pygame.K_LEFT]:`. Instead, define your controls at the top of your loop:

```python
is_moving_left = keys[pygame.K_LEFT] or controller.get_axis(0) < -0.5

if is_moving_left:
    player_rect.x -= player_speed
```

This lets you change controls in one place without breaking your game logic.

---

## 🛠️ Action: Mini-Exercise

**Goal**: Implement a "Sprint" mechanic.

1. Open [examples.py](file:///c:/Users/m287110/Desktop/Git/Personal_projects/Learning_python/intro_to_pygame/02_Events_And_Input/examples.py).
2. Create a variable `player_speed = 5`.
3. Check if `pygame.K_LSHIFT` is being held down.
4. If it is, set `player_speed = 10`. Otherwise, keep it at `5`.
5. Use this `player_speed` variable to change how the white circle moves in your console logs or on-screen.

**Check your progress**: If you can "sprint" by holding Shift, you've mastered state polling!
