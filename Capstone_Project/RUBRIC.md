# 🎓 Capstone Rubric: Space Salvage

This rubric defines the boundary between a "functional script" and a "stable product." Use this to self-assess your Capstone project.

## 🛑 PASS / FAIL GATE (Non-Negotiable)
If your project fails any of these criteria, it is considered **Incomplete**.
- [ ] **Technical Viability**: The code must run without crashing.
- [ ] **State Integrity**: The window must be closeable at any time via the standard 'X' button or Alt+F4.
- [ ] **Frame Control**: The game does not consume 100% CPU when idle; `Clock.tick()` must be implemented.
- [ ] **Game over State**: The game must have a terminal state (win or lose) from which the user can restart or quit.

---

## 🏗️ Core Competencies

### A. Architecture & Structure
- **❌ Fail**: Logic is written in the global scope; values are hardcoded everywhere.
- **⚠️ Meets Minimum**: Logic is wrapped in functions or a main class. Some use of shared state.
- **✅ Excellent**: Strict separation between the Game Loop, Update logic, and Rendering. Zero global state.

### B. Input & Events
- **❌ Fail**: Input handling blocks the loop (e.g., using `time.sleep`).
- **⚠️ Meets Minimum**: Uses `pygame.event.get()` for all events but mixes discrete triggers with polling logic incorrectly.
- **✅ Excellent**: Clear distinction between one-time events (Menu/Quit) and continuous polling (Movement).

### C. Timing & Discipline
- **❌ Fail**: Movement speed is tied to the CPU speed (faster CPU = faster player).
- **⚠️ Meets Minimum**: Uses `Clock.tick(60)` to cap frame rate, but lacks awareness of lag-spikes.
- **✅ Excellent**: Consistent 60 FPS target; logic is deterministic and ignores frame-count for physics.

### D. Collision & State Logic
- **❌ Fail**: Collisions are erratic or use incorrect Rect offsets.
- **⚠️ Meets Minimum**: Collisions work but rely on "Magic Numbers" for sizes or offsets.
- **✅ Excellent**: Uses Pygame `Rect` methods (like `colliderect` or `collidepoint`) and localized bounding boxes correctly.

### E. Code Clarity
- **❌ Fail**: Variables are named `p`, `x`, `y1`. No comments provided.
- **⚠️ Meets Minimum**: Variables are descriptive (e.g., `player_pos`). Comments explain *what* the code does.
- **✅ Excellent**: Variables explain *why* they exist. Comments explain architectural decisions and "why" complex logic was chosen.

---

## 🚩 Automatic Red Flags
The presence of any of these indicates a lack of fundamental discipline:
- **Nested `while True` loops** (Logic starvation).
- **Physics tied to Frame Rate** (No delta-time or fixed-tick awareness).
- **Hardcoded paths** (e.g., `C:\Users\Name\Desktop...`).
- **Unlabeled Constants** (Hex colors or coordinates without names).

## 🧠 Final Self-Assessment
1. If you had to add a "Second Level" to this game, how many files would you have to edit?
2. If the user’s computer runs at 144Hz, will your game break or speed up?
3. What is the single most fragile part of your code right now?

**Masters don't build perfect things; they build things they understand.**
