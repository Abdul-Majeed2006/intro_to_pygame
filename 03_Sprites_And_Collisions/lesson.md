# 🦸 Lesson 03: Sprites and Collisions

## 🧠 The Rationale: Why this exists
As your game grows, keeping track of `player_x`, `player_y`, `enemy1_x`, etc., becomes impossible. We move from simple variables to **Professional Game Architecture** by using Object-Oriented Programming (OOP). This allows us to manage dozens of objects with shared behaviors and handle complex physics interaction with a single line of code.

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

## 5. Screen Boundaries (Clamping)

To prevent your player from walking off the screen, we use the `Rect.clamp` method. It forces one rectangle to stay inside another.

```python
screen_rect = pygame.Rect(0, 0, 800, 600)
player_sprite.rect.clamp_ip(screen_rect) # 'ip' means 'In Place'
```

## ⚠️ The Pitfalls: Common Beginner Mistakes
- **Scaling without `convert_alpha()`**: If you scale or load images without converting them, your game's performance will drop as the CPU works harder to redraw them.
- **Confusing Sprite vs. Rect**: A Sprite *contains* a Rect. The Sprite is the object; the Rect is its physical presence in the world. You move the Rect, not the Sprite.

## 🎯 The Definition of Mastery
You have mastered this concept when you can implement a "Group Collision" where hitting one object triggers a chain reaction in another group, all without using long `if/else` ladders.

## 🔋 What this unlocks next
Mastering Sprites unlocks the ability to manage complex entities like projectiles, inventory items, and multi-part bosses without code rot.

---

---

## 🛠️ Action: Mini-Exercise

Ready to handle real interactions? Go to the [Module 03 Exercise](./exercise.md) to build a collision-based score system.

