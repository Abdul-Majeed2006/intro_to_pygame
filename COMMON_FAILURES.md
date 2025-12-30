# 🛑 Common Failures (The Wall of Shame)

> **"Mistakes are the best teachers, but only if you actually learn from them. If you make these mistakes, I will be very disappointed."**  
> — Your Instructor

This document lists the most frequent, project-killing mistakes that beginner Pygame developers make. **Read this before asking for help.**

---

## 1. The "Infinite Loop of Death"
**Symptom:** The window freezes, becomes unresponsive, and you have to Force Quit python.  
**Cause:** You forgot to handle the `pygame.QUIT` event or update the loop variable.  
**The Fix:**
```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # <--- DO NOT FORGET THIS
```

## 2. The "Invisible Sprite"
**Symptom:** You created a player, but the screen is empty.  
**Causes (Check in this order):**
1.  **You didn't draw it:** Did you call `display_surface.blit()` or `your_group.draw()` *inside* the loop?
2.  **You drew it, but didn't `.flip()`:** Did you call `pygame.display.flip()` at the end of the loop?
3.  **The Painter's Algorithm Fail:** Did you `draw()` the sprite first, and then `fill()` the screen with black *on top* of it? (Always `fill` first, `draw` second).
4.  **Off-Screen Coordinates:** Is your sprite at `(10000, 10000)`? Print `sprite.rect` to check.

## 3. The "Laggy Mess"
**Symptom:** The game runs at 2 FPS and your computer fan screams.  
**Cause:** **LOADING ASSETS INSIDE THE LOOP.**  
**The Fix:**
NEVER do this:
```python
while running:
    # ❌ WRONG! This reads the hard drive 60 times a second.
    image = pygame.image.load("player.png") 
    screen.blit(image, (0,0))
```
ALWAYS do this:
```python
# ✅ CORRECT! Load once at startup.
image = pygame.image.load("player.png").convert_alpha() 

while running:
    # Blit the already-loaded image
    screen.blit(image, (0,0))
```

## 4. "Global Variable Spaghetti"
**Symptom:** You can't track why 'score' resets randomly, or why players teleport.  
**Cause:** Using `global` variables everywhere instead of passing arguments or using Classes.  
**The Rule:** If you type `global`, you are probably doing it wrong. Use a Class.

## 5. "The Ghost Inputs"
**Symptom:** You tap spacebar once to jump, but the player double-jumps or flies away.  
**Cause:** confusing `pygame.key.get_pressed()` (continuous polling) with `pygame.KEYDOWN` (discrete event).  
**The Rule:**
- **Jumping/Shooting/UI Clicks?** Use the **Event Loop** (`if event.type == KEYDOWN`).
- **Walking/Driving/Flying?** Use **Polling** (`pygame.key.get_pressed()`).

---

**Commit these to memory. Good luck.**
