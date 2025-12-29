# Contributing to the Pygame Masterclass

We aim for greatness, not "good enough." If you wish to contribute to this curriculum, you must adhere to our strict engineering and educational standards.

## 🛠️ Mandatory Chapter Structure

Every new module MUST follow the 4-file rule:
1. `lesson.md`: Theory, Implementation, and links to exercises.
2. `examples.py`: Fully functional, polished demonstration code.
3. `exercise.md`: 3-level difficulty challenges (Level 1: Logic, Level 2: Engineering, Level 3: Architecture).
4. `assets/`: (Optional) All media must be localized within the module folder. No floating assets in the root.

## 🐍 Python Style Guide

We do not write "scripts"; we build software.
- **Python Version**: 3.10+ is required.
- **Naming**: Use ultra-descriptive variables (e.g., `display_surface` instead of `screen`, `engine_tick_clock` instead of `clock`).
- **Comments**: Focus on the **Why**, not the **What**. Every major API call should have an engineering rationale comment.
- **Paths**: Use `os.path.abspath` logic for all asset loading to ensure examples run from any directory.

## ✅ Quality Assurance
- **Zero Broken Examples**: Every `examples.py` must run bug-free on a clean install.
- **Linting**: Markdown files must be free of common formatting errors (blanks around headings, trailing spaces).
- **Difficulty Curve**: Exercises must force the learner to think. No "copy-paste" tasks allowed.

## 📦 Pull Requests
- Keep PRs focused on a single module or feature.
- Use meaningful commit messages (e.g., `module_06: added vector math lesson`).
- Verify all links and asset paths before submitting.

Failure to follow these rules is an automatic rejection. We are building the best Pygame curriculum on the planet—help us keep it that way.
