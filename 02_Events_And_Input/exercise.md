# 🛠️ Module 02 Exercise: Input & Constraint

## Goal: Bridge the gap between player intent and physical limits

### 📝 Level 1: The invisible Wall (Boundaries)

1. Open [examples.py](./examples.py).
2. Implement logic that prevents the white circle from leaving the screen.
3. **Constraint**: If `player_x < 0`, it should be set back to `0`. Repeat for all four edges.
4. **Why?**: In game dev, "clamping" is a universal skill.

### 📝 Level 2: The Perfect Diagonal

1. Currently, if a player holds UP and RIGHT, they move faster (Pythagorean theorem!).
2. Modify the movement code so that moving diagonally is the same speed as moving horizontally.
3. **Logic**: You will need to check if two keys are held at once and multiply the speed by `0.707`.

### 📝 Level 3: The Dash Mechanic

1. Implement a "Blink" or "Dash" ability.
2. When the spacebar is **pressed** (Event Handling), teleport the player 50 pixels in their current direction.
3. **Challenge**: Add a 2-second cooldown so they can't spam it.

**Check your progress**: If you can trap the player in a box, fix their speed, and give them a dash, you are ready for Module 03.
