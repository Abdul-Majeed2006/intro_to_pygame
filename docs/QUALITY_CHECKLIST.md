# ✅ Quality Checklist

To maintain professional standards, every lesson and example must pass these checks.

## 🐍 Code Quality
- [ ] **Zero Global Spaghetti**: All logic is wrapped in `run_lesson()` or a class.
- [ ] **Version Guard**: Every script includes a `sys.version_info` check for Python 3.10+.
- [ ] **No Magic Numbers**: Colors, screen sizes, and speeds must be defined as variables or constants with descriptive names.
- [ ] **Descriptive Naming**: No `p`, `x`, `c`. Use `player_rectangle`, `current_coordinate`, `engine_clock`.

## 📚 Educational Quality
- [ ] **The 4-File Rule**: Every module contains `lesson.md`, `examples.py`, `exercise.md`, and local `assets/`.
- [ ] **Prerequisite Alignment**: Lessons never use a concept (e.g., Clamping) without explaining it first.
- [ ] **Stand-alone Examples**: Every `examples.py` must run bug-free on a clean install.
- [ ] **Challenging Exercises**: No "Copy-Paste" tasks. Exercises must involve logic jumps.

## 📁 Repository Standards
- [ ] **Localized Assets**: No floating assets in the root. Everything is localized to its module.
- [ ] **Absolute Pathing**: Use `os.path.abspath` logic for asset loading to ensure cross-directory compatibility.
- [ ] **Lint Clean**: Markdown files must be free of blank-line and trailing-space errors.
