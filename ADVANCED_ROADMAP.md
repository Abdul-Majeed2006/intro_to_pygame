# ⚡ Advanced Pygame Roadmap: The Engineering Frontier

> "Beginners build features. Engineers build systems."

The core curriculum (01-04) teaches you how to use Pygame. This roadmap defines how you will master **Game Engineering**. You are not ready for these modules until you have completed the [Capstone Project](./Capstone_Project/).

## 🛑 Prerequisites for Entry

Do not open these files until you have:
1. Mastered the **Game Loop** (01).
2. Solved **Diagonal Speed Normalization** (02 Exercise).
3. Implemented a **Sprite-based Collision Group** (03).
4. Created a **Reactive UI with Audio Feedback** (04).
5. Built and deployed the **Space Salvage Capstone**.

---

## 🏗️ Upcoming Modules

### Module 06: Architecture & State Machines
- **The Concept**: Move away from monolithic `while True` loops.
- **Topics**: Game States (Menu, Play, Pause), Scene Management, and Decoupled Input Handling.
- **Payoff**: A game that can scale to thousands of lines without breaking.

### Module 07: Performance & Optimization
- **The Concept**: Frame-rate independence and pixel-efficiency.
- **Topics**: Dirty Rectangles (partial screen updates), Surface conversion optimization, and Python Profiling.
- **Payoff**: 60 FPS even on low-end hardware with hundreds of active entities.

### Module 08: Networking Concepts
- **The Concept**: The nightmare of latency and synchronization.
- **Topics**: Sockets (TCP/UDP), Client-Server architecture, and basic Dead Reckoning.
- **Payoff**: Your first "Hello World" over a local network.

### Module 09: Shader Experiments (Visual Excellence)
- **The Concept**: Beyond the CPU.
- **Topics**: Introduction to GLSL, post-processing effects, and integration with ModernGL.
- **Constraint**: Marked as "Non-Pygame Core" (advanced graphics theory).

---

## 🏛️ The Archive
Current work-in-progress materials and legacy experiments are stored in the [Advanced Archive](./Advanced_Archive/). Explore at your own risk; these do not yet adhere to the strict [Contributing Standards](./CONTRIBUTING.md).
