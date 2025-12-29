# 🛠️ Module 03 Exercise: Advanced Sprites & Logic

## Goal: Transition from simple "hits" to complex game physics and entity AI

### 📝 Level 1: The Predator Mechanic

1. Open [examples.py](./examples.py).
2. Implement a "Power-Up" state for the player (e.g., hold 'P').
3. While powered up, change the player's color or scale.
4. **Challenge**: Modify the Enemy class so they move **away** from the player if the power-up is active.

### 📝 Level 2: Structural Integrity (Hit Points)

1. Give every Enemy a `self.health = 2` attribute.
2. When a collision occurs, do not kill the enemy immediately.
3. Instead, subtract 1 from their health and push them back 20 pixels.
4. Only use `.kill()` when `health <= 0`.

### 📝 Level 3: Particle Foundations

1. Create a `Particle` class that inherits from `pygame.sprite.Sprite`.
2. When an enemy is destroyed, spawn 5 small, random-colored particles at their location.
3. **Logic**: The particles should fly in random directions and disappear after 1 second.

**Check your progress**: If you have enemies that flee, survive hits, and explode into particles, you've mastered 2D Game Physics!
