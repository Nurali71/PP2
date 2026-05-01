import pygame, sys
from pygame.locals import *
import random, time


pygame.init()

# Setting up FPS and Screen
FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")

# Colors
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SPEED = 5            
SCORE = 0           
COIN_SCORE = 0       
last_speed_boost = 0 # Helper variable to track speed progression

# Fonts for UI
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading Assets
background = pygame.image.load("AnimatedStreet.png")
BRONZE_IMG = pygame.image.load("coin_bronze.png")
SILVER_IMG = pygame.image.load("coin_silver.png")
GOLD_IMG   = pygame.image.load("coin_gold.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Spawning enemy at a random X position at the top
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # Constant downward movement
        if (self.rect.top > 600):    # Reset position if off-screen
            SCORE += 1               # Earn a point for dodging
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # Starting position
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Movement with screen boundary checks
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spawn()

    def spawn(self):
        # random coins 
        self.type = random.choices(['bronze', 'silver', 'gold'], weights=[60, 30, 10])[0]
        
        if self.type == 'bronze':
            self.weight = 1
            raw_image = BRONZE_IMG
            size = (30, 30)
        elif self.type == 'silver':
            self.weight = 2
            raw_image = SILVER_IMG
            size = (35, 35)
        elif self.type == 'gold':
            self.weight = 5
            raw_image = GOLD_IMG
            size = (40, 40)

        # Scale the image based on type and reset hit-box (rect)
        self.image = pygame.transform.scale(raw_image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.spawn()

# Creating Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite Groups for collision and rendering management
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Drawing static background
    DISPLAYSURF.blit(background, (0,0))
    
    # Rendering UI Scores
    scores_label = font_small.render(f"Cars: {SCORE}", True, BLACK)
    coin_label = font_small.render(f"Score: {COIN_SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores_label, (10,10))
    DISPLAYSURF.blit(coin_label, (SCREEN_WIDTH - 110, 10))

    # Move and Draw all entities
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Logic for collecting coins
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += C1.weight  # Increase score by coin's value
        C1.spawn()              # Respawn coin at top
        
        # TASK: Increase Enemy speed every N coins earned (threshold: 10 points)
        if COIN_SCORE // 10 > last_speed_boost:
            SPEED += 1          # Increase game difficulty
            last_speed_boost = COIN_SCORE // 10

    # Logic for hitting an enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        
        # Cleanup sprites before exiting
        for entity in all_sprites:
            entity.kill() 
            
        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)