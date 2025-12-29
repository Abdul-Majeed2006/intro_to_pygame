# 🛠️ Module 01 Exercise: Mastering the Loop

## Goal: Break the static environment and introduce dynamic logic

### 📝 Level 1: The Infinite Desert (Tiling)

1. Open [examples.py](./examples.py).
2. Use a **Nested `for` loop** to fill the entire 800x600 screen with `sand_tile_image`.
3. **Constraint**: Do not hardcode the repetition count. Use `SCREEN_WIDTH // tile_width` to calculate it dynamically.

### 📝 Level 2: The Earth Tremor (Coordinate Offsets)

1. Create a variable `shake_offset = 0`.
2. Inside the loop, set `shake_offset` to a random number between -2 and 2 (use the `random` module).
3. Apply this offset to every image you draw.
4. **Verification**: If the screen "vibrates" slightly while running, you've mastered the concept of coordinate manipulation.

### 📝 Level 3: The Frame Warden (Performance Logic)

1. Every time the loop runs, increment a variable called `frame_count`.
2. Print the `frame_count` to the console, but **only once every 60 frames**.
3. **Hint**: Use the modulo operator `%`.

**Check your progress**: If you can tile the screen, shake the earth, and track performance, you've graduated from "Python Beginner" to "Game Loop Resident". Move to Module 02.
