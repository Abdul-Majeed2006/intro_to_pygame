# 🚀 Capstone Project: Space Salvage

## Concept
You are the pilot of a deep-space salvage drone. Your mission is simple but dangerous: collect floating **Oxygen Tanks** while avoiding high-velocity **Meteors**. Your drone is fragile; too many impacts will cause a total system failure.

## Mandatory Features
- **Deterministic Loop**: The game must run at its target FPS (60) without logic variability.
- **8-Way Movement**: Responsive player movement using WASD or Arrow Keys.
- **Dynamic Spawning**: Oxygen and Meteors must spawn at random positions.
- **Boundary Clamping**: The player must be physically unable to leave the window.
- **Collision Feedback**: 
    - Collecting Oxygen increases the score and plays a sound.
    - Hitting a Meteor reduces "Hull Integrity" and plays an impact sound.
- **HUD (UI)**: Real-time display of Score and Health.
- **Game State Logic**: A "Game Over" screen that stops play and allows for a reset.

## Optional Challenges (Extra Credit)
- **Momentum**: Implement velocity accumulation so the ship has "weight" and slides.
- **Scaling Difficulty**: Spawning more meteors as the score increases.
- **Animated Sprites**: Rotate the player ship based on movement direction.

## Hard Constraints
- **Resolution**: 800x600 pixels.
- **No External Libraries**: Use only pure Pygame and Python Standard Library.
- **Code Standards**: Zero global spaghetti. All logic must be function or class-scoped.

---

**Proceed to [requirements.md](./requirements.md) for technical constraints.**
