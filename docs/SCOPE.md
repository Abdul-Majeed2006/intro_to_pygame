# 🎯 v1.0 Scope & Boundary

To maintain high educational standards and prevent "tutorial bloat," this repository adheres to a strict scope. We focus on the **Fundamentals of 2D Game Engineering**.

## ✅ What is INCLUDED
The v1.0 curriculum is complete when the learner masters:
1. **The Deterministic Game Loop**: Management of time and frame rates.
2. **Event Polling & Handling**: Mastering user interaction patterns.
3. **The Rectangle (Rect)**: Clamping, collisions, and layout logic.
4. **Sprite-Based Architecture**: Transitioning from scripts to OOP systems.
5. **Basic State Machines**: Managing menus, play states, and game overs.

## 🚫 What is NOT Included
The following topics are explicitly excluded from the v1.x core:
- **Artificial Intelligence**: No pathfinding (A*) or complex NPC behaviors.
- **3D Graphics**: No Raycasting, Z-buffering, or OpenGL interop.
- **Networking**: No Sockets/Multiplayer (relegated to `pygame_advanced_systems`).
- **Advanced Shaders**: No GLSL or GPU-specific optimizations.

## ❓ Why the Freeze?
Mastery requires focus. Introducing high-level concepts (like networking) before a learner can properly clamp a `Rect` to a screen creates "fragile knowledge." This repository builds unbreakable foundations. Everything beyond these boundaries is distraction.
