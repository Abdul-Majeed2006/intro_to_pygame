# 🛠️ Module 04 Exercise: State Toggles

## Goal: Implement a "Pause Toggle".

### 📝 Instructions

1. Open [examples.py](./examples.py).
2. Create a variable `game_paused = False`.
3. In the Event Loop, check for `pygame.KEYDOWN` of `pygame.K_ESCAPE`.
4. When pressed, toggle the variable: `game_paused = not game_paused`.
5. In the rendering section, if `game_paused` is True, draw a semi-transparent dark rectangle over the whole screen and render the word "PAUSED" in the center.

**Check your progress**: If you can press ESC to freeze the visual state and see a pause overlay, you've mastered the basics of State Machines!
