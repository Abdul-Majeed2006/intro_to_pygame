# 🛠️ Module 03 Exercise: Score Systems

## Goal: Create a score system that reacts to collisions.

### 📝 Instructions

1. Open [examples.py](./examples.py).
2. Create a variable `score = 0` before the game loop.
3. Inside the loop, capture the result of the collision check: `hits = pygame.sprite.spritecollide(...)`.
4. If `hits` contains any items, increment the `score` and `print(f"Current Score: {score}")`.
5. **Bonus**: Use a `for` loop to spawn 10 enemies instead of 5.

**Check your progress**: If you can "eat" enemies and see your score rise in the console, you've mastered game physics!
