# Common Failures: Engineering Your Way Out

This document covers the "Why" behind common Pygame bugs. Do not look for a quick fix; seek to understand the underlying principle.

## 1. The Game Loop Illusion
**Pattern**: "My game is unresponsive, flickers, or runs at 1000% speed."

- **The Failure**: High-speed logic without a throttle.
- **The Rationale**: If you don't call `clock.tick(60)`, Python will run the loop as fast as the CPU allows. This wastes power and makes gameplay impossible.
- **The Reasoning**: Check if `pygame.event.get()` is called once per frame. If it isn't, the OS thinks the window is dead. Check if `clock.tick()` is inside the `while` loop, not outside.

## 2. Event Handling Misconceptions
**Pattern**: "I press space to jump once, but the player jumps five times."

- **The Failure**: Using **Polling** for **Trigger** actions.
- **The Rationale**: Polling (`get_pressed`) checks if a key is down *now*. A human press lasts multiple frames. Events (`KEYDOWN`) are messages sent once per physical act.
- **The Reasoning**: Ask yourself: "Should this happen once per press, or as long as the button is held?"

## 3. Rendering Order & State Confusion
**Pattern**: "I drew my sprite, but the screen is just black (or flickering)."

- **The Failure**: Drawing in the wrong order or forgetting to "flip" the buffer.
- **The Rationale**: Pygame uses double-buffering. You draw on a "hidden" canvas, then swap it with the visible one. If you `screen.fill()` *after* drawing your player, you just painted over your player.
- **The Reasoning**: Follow the discipline: **Clear (Fill) -> Draw (Blit) -> Update Display (Flip).**

## 4. Collision Logic Lies
**Pattern**: "My objects collide, but then they get stuck together."

- **The Failure**: Overlap detection without resolution.
- **The Rationale**: `colliderect` only tells you if rectangles are touching. If you move an object *into* another and keep detecting the collision, they will stick.
- **The Reasoning**: You must not only detect the hit but **undo** the movement that caused the overlap. This is why we use "Old Position" variables or `Rect.clamp`.

## 5. Magic Numbers & Scaling Debt
**Pattern**: "I changed my window size and everything broke."

- **The Failure**: Using hardcoded pixel values (e.g., `x = 400`).
- **The Rationale**: A professional game architects its positions relative to screen dimensions or game-world units. 
- **The Reasoning**: If you see a number like `300` in your logic without a name, it is a **Magic Number**. Replace it with `SCREEN_WIDTH // 2` or a constant.

---

## Debugging Discipline

If you are guessing what's wrong, you have already lost.

1. **Isolate**: Comment out everything except the failing component.
2. **Visualize**: Use `print()` to see the coordinates of your Rects or the value of your variables.
3. **Simplify**: If a complex Sprite Group is failing, test with one single Rect.

### The Debugger's Mantra
**"If you don't know what changed, you're guessing."**
