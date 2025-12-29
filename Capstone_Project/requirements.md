# 🚀 Capstone Project: Space Salvage

## Goal

You have been tasked with building a salvage drone in deep space. Your objective is to collect as many **Oxygen Tanks** as possible while avoiding lethal **Meteors**.

This is the final test of your Pygame fundamentals. If you can build this, you are ready for advanced engine architecture.

## 🛠️ Requirement Specification

### 1. The Environment

- **Resolution**: 800x600 pixels.
- **Background**: Use the provided `star_bg.png` and tile it or scale it to fit the screen.
- **Target FPS**: Strictly 60 FPS (Master the Delta Time concept).

### 2. The Pilot (Input & Movement)

- **Sprite**: Use `ship.png`.
- **Movement**: 8-way directional movement (WASD or Arrow keys).
- **The Twist**: Implement **Momentum**. The ship shouldn't stop instantly; it should slide slightly when keys are released.
- **Boundaries**: The ship must never leave the screen (Clamping).

### 3. The Hazard (Meteors)

- **Sprite**: Use `meteor.png`.
- **Behavior**: Meteors should spawn at random locations and drift across the screen.
- **Collision**: If a meteor hits the ship, play `hit.ogg` and subtract from a "Hull Integrity" percentage.

### 4. The Objective (Oxygen)

- **Sprite**: Use `oxygen.png`.
- **Behavior**: Spawn these at random intervals.
- **Collision**: If collected, play `collect.ogg` and increase the score.

### 5. The HUD (UI)

- **Display**: Show "Score" and "Hull Integrity" on screen using Pygame's Font module.
- **Game Over**: If Hull Integrity reaches 0%, display a "MISSION FAILED" message and allow the player to restart by pressing 'R'.

---

## 🏆 Success Criteria

- [ ] Game initializes without errors.
- [ ] Ship moves with a "weighty" slides feel.
- [ ] Collisions trigger sound effects.
- [ ] Score is tracked and visible.
- [ ] Game state flips to "Game Over" gracefully.

**Ready? Start with [starter_code.py](./starter_code.py)**
