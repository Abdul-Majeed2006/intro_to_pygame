# 🦸 Lesson 03: Sprites and Collisions

In this lesson, we move from simple variables to **Professional Game Architecture**. We'll learn how to manage dozens of objects at once and handle interactions between them using Object-Oriented Programming (OOP).

## 1. The Theory: Why use Sprites?

As your game grows, keeping track of `player_x`, `player_y`, `enemy1_x`, `enemy2_x`, etc., becomes impossible.

- Classes: We bundle the image and the position (Rect) into a single object called a `Sprite`.
- Groups: We put all these objects into a "Magic Bag" (Sprite Group). Instead of updating 100 enemies individually, we tell the Bag to update everyone at once.

## 2. Implementation: The Sprite Class

Every game object should inherit from `pygame.sprite.Sprite`.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        # Every sprite MUST have an 'image' and a 'rect'
        self.image = pygame.image.load("assets/players/tile_0006.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
```

## 3. Sprite Groups: Batch Processing

Sprite Groups allow you to manage thousands of objects with single commands.

```python
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Add a sprite to a group
all_sprites.add(player)

# Inside Game Loop:
all_sprites.update() # Calls update() on every sprite
all_sprites.draw(screen) # Draws every sprite
```

## 4. Collision Detection 💥

How do we know when the player hits an enemy? Pygame provides highly optimized mathematical tools for this.

- Single Check: `spriteA.rect.colliderect(spriteB.rect)`
- Group Check: `pygame.sprite.spritecollide(player, enemies, True)`
  - The `True` parameter means "Kill the enemy sprite; remove it from all groups permanently."

---

## 🛠️ Action: Mini-Exercise

**Goal**: Create a score system that reacts to collisions.

1. Open [examples.py](file:///c:/Users/m287110/Desktop/Git/Personal_projects/Learning_python/intro_to_pygame/03_Sprites_And_Collisions/examples.py).
2. Create a variable `score = 0` before the game loop.
3. Inside the loop, capture the result of the collision check: `hits = pygame.sprite.spritecollide(...)`.
4. If `hits` contains any items, increment the `score` and `print(f"Current Score: {score}")`.
5. **Bonus**: Use a `for` loop to spawn 10 enemies instead of 5.

**Check your progress**: If you can "eat" enemies and see your score rise in the console, you've mastered game physics!
