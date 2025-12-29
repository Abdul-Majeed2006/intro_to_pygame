# 🛠️ Module 04 Exercise: Juice & Polish

## Goal: Transform a functional UI into a satisfying user experience

### 📝 Level 1: Reactive Audio (Hover SFX)

1. Open [examples.py](./examples.py).
2. Currently, the sound only plays when the button is **clicked**.
3. Implement logic that plays a short, subtle sound (or prints "HOVER") the **moment** the mouse enters the button area.
4. **Constraint**: The sound should only play **once** per hover (don't spam it every frame).

### 📝 Level 2: Pulsing UI (Animation Logic)

1. Instead of a static button, make the button "pulse" or slightly increase in size every second.
2. **Logic**: Use `pygame.time.get_ticks()` and a sine wave (`math.sin`) to calculate a scale offset.
3. Apply this offset to the width and height of your `button_rect`.

### 📝 Level 3: Dynamic Typography

1. Create a "Score" text that follows the mouse cursor.
2. Every time the user clicks the button, the text should change color (e.g., from White to Red to Green).
3. **Challenge**: Make the text fade out slowly after 2 seconds if the button isn't clicked.

**Check your progress**: If your UI has audio feedback, pulsing animations, and reactive text, you've mastered "The Juice". Move to the Advanced labs!
