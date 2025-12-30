# 🏆 Capstone Project Rubric

> **"In the real world, 'it works on my machine' is not an excuse. It either runs perfectly, or it's broken."**

### ❌ AUTOMATIC FAILURE CONDITIONS (0%)
If your submission has any of these, **do not bother submitting.**
1.  **Crash on Launch:** The script crashes immediately upon execution.
2.  **Missing Assets:** You didn't include the `/assets` folder or used absolute paths (e.g., `C:/Users/You/Desktop...`).
3.  **Infinite Loop:** The window freezes and cannot be closed normally.
4.  **Plagiarism:** Copy-pasting code from the examples without modification or understanding.

---

### 🟢 PASSING CRITERIA (100 Points Total)

#### 1. Engineering Standards (30 Points)
- **[10pts] Clean Loop:** Game loop is separated into clear Input, Update, and Draw phases.
- **[10pts] No Globals:** Uses `def main():` or a `Game` class. No code running in the global scope.
- **[10pts] Asset Management:** Images/Sounds loaded *once* before the loop, not every frame.

#### 2. Gameplay & Mechanics (30 Points)
- **[10pts] Controls:** Movement is smooth (using `dt` or proper frame limiting). Input response is snappy.
- **[10pts] Win/Loss State:** The game can actually end (Game Over screen) and optionally restart.
- **[10pts] Fairness:** Hitboxes are reasonably accurate (no dying when not touching anything).

#### 3. User Experience (20 Points)
- **[10pts] Clarity:** Is it obvious how to play? (Instructions or intuitive design).
- **[10pts] Feedback:** Visual/Audio confirmation when things happen (e.g., sound on jump, flash on hit).

#### 4. Code Quality (20 Points)
- **[10pts] Readability:** Variable names make sense (`player_velocity`, not `pv`).
- **[10pts] Comments:** Complex logic is explained. "Teacher's Voice" style comments are a bonus.

---

### 🌟 BONUS (Distinction)
- **[+5pts] Polish:** Menus, pause screens, or high-score saving.
- **[+5pts] "Juice":** Screen shake, particle effects, or dynamic lighting.

---

**Final Grade:** ______ / 100
