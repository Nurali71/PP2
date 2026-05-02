import pygame
import ui
import game
import db
import config

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
state = "menu"
username = ""
input_active = True
db.init_db()
snake = game.Snake()
food = game.Food()
score = 0
level = 1

while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#menu
        if state == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = ui.main_menu(screen)

                if buttons["play"].collidepoint(mouse):
                    state = "game"
                    player_id = db.get_or_create_player(username)

                elif buttons["leader"].collidepoint(mouse):
                    state = "leaderboard"


        elif state == "game":

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dir = (-1, 0)

                elif event.key == pygame.K_RIGHT:
                    snake.dir = (1, 0)

                elif event.key == pygame.K_UP:
                    snake.dir = (0, -1)

                elif event.key == pygame.K_DOWN:
                    snake.dir = (0, 1)

#game logic

    if state == "menu":
        ui.main_menu(screen)

    elif state == "game":

        screen.fill(config.BACKGROUND)
        snake.move()

        if snake.out_of_bounds(config.WIDTH, config.HEIGHT, config.GRID_SIZE):
            state = "game_over"

        if snake.collide_self():
            state = "game_over"

        if snake.body[0] == food.pos:
            snake.grow = True
            food.respawn()
            score += 1

        for b in snake.body:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (b[0] * config.GRID_SIZE,
                 b[1] * config.GRID_SIZE,
                 config.GRID_SIZE,
                 config.GRID_SIZE)
            )

        pygame.draw.rect(
            screen,
            (255, 200, 0),
            (food.pos[0] * config.GRID_SIZE,
             food.pos[1] * config.GRID_SIZE,
             config.GRID_SIZE,
             config.GRID_SIZE)
        )

        font = pygame.font.SysFont("Arial", 24)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(10)