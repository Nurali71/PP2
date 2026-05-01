import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game Constants
BLOCK_SIZE = 20
GRID_SIZE = 20  # 20x20 blocks
WIDTH = BLOCK_SIZE * GRID_SIZE
HEIGHT = BLOCK_SIZE * GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
YELLOW = (255, 255, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - Practice 10 (Levels)')
clock = pygame.time.Clock()

# Font for score and level display
score_font = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    """Draws a subtle grid for better gameplay visualization"""
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (30, 30, 30), rect, 1)

class Snake:
    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def move(self, grow=False):
        # Prevent 180-degree turns
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Calculate new head position
        head = list(self.body[0])
        if self.direction == 'UP': head[1] -= BLOCK_SIZE
        if self.direction == 'DOWN': head[1] += BLOCK_SIZE
        if self.direction == 'LEFT': head[0] -= BLOCK_SIZE
        if self.direction == 'RIGHT': head[0] += BLOCK_SIZE

        self.body.insert(0, head)
        if not grow:
            self.body.pop()

    def check_collision(self):
        head = self.body[0]
        # Wall collision check
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        # Self collision check (collision with body)
        if head in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.pos = [random.randrange(0, GRID_SIZE) * BLOCK_SIZE,
                    random.randrange(0, GRID_SIZE) * BLOCK_SIZE]
        
        # Weighted random choice for food type
        choice = random.choices(['normal', 'silver', 'gold'], weights=[70, 20, 10])[0]
        
        if choice == 'normal':
            self.weight = 1
            self.color = RED
            self.lifetime = 8000  # 8 seconds
        elif choice == 'silver':
            self.weight = 2
            self.color = SILVER
            self.lifetime = 6000   # 6 seconds
        else:
            self.weight = 3
            self.color = GOLD
            self.lifetime = 4000   # 4 seconds
            
        self.spawn_time = pygame.time.get_ticks()

    def is_expired(self):
        
        return (pygame.time.get_ticks() - self.spawn_time) > self.lifetime

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], BLOCK_SIZE, BLOCK_SIZE))

# --- Game Variables ---
snake = Snake()
food = Food()
score = 0
level = 1
food_eaten = 0
speed = 7      # Starting speed
game_over = False

# Main Game Loop 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: snake.change_to = 'UP'
            if event.key == pygame.K_DOWN: snake.change_to = 'DOWN'
            if event.key == pygame.K_LEFT: snake.change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: snake.change_to = 'RIGHT'

    #  Respawn food if time is up
    if food.is_expired():
        food.spawn()

    # Move snake and check for eating
    is_eating = False
    if snake.body[0] == food.pos:
        score += food.weight
        food_eaten += 1
        is_eating = True
        food.spawn()

        #  Level System
        # Increase level every 3 food items eaten
        if food_eaten % 3 == 0:
            level += 1
            speed += 2 # Increase speed with level up

    snake.move(grow=is_eating)

    # Collision detection
    if snake.check_collision():
        game_over = True

    #  Rendering 
    screen.fill(BLACK)
    draw_grid()
    
    food.draw()
    
    
    for i, pos in enumerate(snake.body):
        color = GREEN if i == 0 else (0, 180, 0)
        pygame.draw.rect(screen, color, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Display score and level
    score_surf = score_font.render(f"Score: {score}", True, WHITE)
    level_surf = score_font.render(f"Level: {level}", True, YELLOW)
    screen.blit(score_surf, (10, 10))
    screen.blit(level_surf, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(speed) # Speed is controlled by current level

# Game Over Logic 
screen.fill(BLACK)
final_msg = score_font.render(f"Game Over! Final Score: {score}", True, RED)
screen.blit(final_msg, (WIDTH // 10, HEIGHT // 2))
pygame.display.flip()
time.sleep(3)
pygame.quit()