import pygame
import sys
import db, game, config

# Setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
db.init_db()

# Global variables
state = "menu"
username = "Player"
player_id = None
score = 0
level = 1

# Initialize Game Objects
snake = game.Snake()
food = game.Food()
poison = game.Food(color=(150, 0, 0)) # Red color for poison
obstacles = game.Obstacle(level, snake.body)

def start_new_game():
    global snake, food, poison, obstacles, score, level, state
    snake = game.Snake()
    score = 0
    level = 1
    obstacles = game.Obstacle(level, snake.body)
    food.respawn(snake.body, obstacles.blocks)
    poison.respawn(snake.body, obstacles.blocks)
    state = "game"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        # Handle State: MENU (Username input)
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Press Enter to play
                    player_id = db.get_or_create_player(username)
                    start_new_game()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode # Add typed character to name

        # Handle State: GAME (Directional control)
        elif state == "game":
            if event.type == pygame.KEYDOWN:
                # Prevent 180-degree turns (cannot go Left if moving Right)
                if event.key == pygame.K_UP and snake.dir != (0, 1): snake.dir = (0, -1)
                if event.key == pygame.K_DOWN and snake.dir != (0, -1): snake.dir = (0, 1)
                if event.key == pygame.K_LEFT and snake.dir != (1, 0): snake.dir = (-1, 0)
                if event.key == pygame.K_RIGHT and snake.dir != (-1, 0): snake.dir = (1, 0)

    # --- STATE: GAME LOGIC ---
    if state == "game":
        screen.fill((30, 30, 30)) # Background
        snake.move()

        # 1. Collision with Borders or Itself
        if snake.body[0] in snake.body[1:] or \
           snake.body[0][0] < 0 or snake.body[0][0] >= 30 or \
           snake.body[0][1] < 0 or snake.body[0][1] >= 30:
            db.save_game(player_id, score, level)
            state = "menu"

        # 2. Collision with Obstacles (Walls)
        if snake.body[0] in obstacles.blocks:
            db.save_game(player_id, score, level)
            state = "menu"

        # 3. Eating Normal Food
        if snake.body[0] == food.pos:
            snake.grow = True
            score += 1
            food.respawn(snake.body, obstacles.blocks)
            if score % 5 == 0: # Level up every 5 points
                level += 1
                obstacles = game.Obstacle(level, snake.body)

        # 4. Eating Poison
        if snake.body[0] == poison.pos:
            if snake.shorten(): # If snake is too short -> Game Over
                db.save_game(player_id, score, level)
                state = "menu"
            poison.respawn(snake.body, obstacles.blocks)

        # --- DRAWING ---
        # Draw Walls
        for block in obstacles.blocks:
            pygame.draw.rect(screen, (100, 100, 100), (block[0]*20, block[1]*20, 20, 20))
        # Draw Snake
        for b in snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (b[0]*20, b[1]*20, 19, 19))
        # Draw Food & Poison
        pygame.draw.rect(screen, food.color, (food.pos[0]*20, food.pos[1]*20, 20, 20))
        pygame.draw.rect(screen, poison.color, (poison.pos[0]*20, poison.pos[1]*20, 20, 20))

    elif state == "menu":
        screen.fill((0, 0, 0))
        # (Draw your text "Press Enter to Play" and username here using ui.py)

    pygame.display.flip()
    clock.tick(10 + level) # Speed increases as level goes up