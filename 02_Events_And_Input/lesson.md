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

## ⚠️ The Pitfalls: Common Beginner Mistakes
- **Polling for Everything**: If you poll the 'SPACE' key for jumping, one button press might trigger 5 jumps because the key was held down for 5 frames. Use **Events** for triggers.
- **Ignoring the Mouse Position**: Beginners often forget that `get_pos()` returns a coordinate relative to the *window*, not the whole world.

## 🎯 The Definition of Mastery
You have mastered this concept when you can justify the choice between `pygame.event` and `pygame.key.get_pressed()` for any given game mechanic.

## 🔋 What this unlocks next
Input handling is the gateway to **Entity Management**. Once you control one object, you'll soon want to control hundreds.

---

## 🛠️ Action: Mini-Exercise

Time to build some gameplay! Check out the [Module 02 Exercise](./exercise.md) to implement a professional "Sprint" mechanic.

