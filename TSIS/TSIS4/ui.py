import pygame
import config

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 28)
BIG = pygame.font.SysFont("Arial", 48)


def draw_text(screen, text, x, y, font=FONT, color=config.TEXT_COLOR):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def button(screen, text, x, y, w, h, mouse):
    rect = pygame.Rect(x, y, w, h)
    color = config.BUTTON_HOVER if rect.collidepoint(mouse) else config.BUTTON_COLOR

    pygame.draw.rect(screen, color, rect, border_radius=10)
    draw_text(screen, text, x + 20, y + 10)

    return rect


def main_menu(screen):
    screen.fill(config.BACKGROUND)
    draw_text(screen, "SNAKE GAME", 180, 100, BIG)

    mouse = pygame.mouse.get_pos()

    return {
        "play": button(screen, "Play", 220, 200, 160, 50, mouse),
        "leader": button(screen, "Leaderboard", 220, 270, 160, 50, mouse),
        "settings": button(screen, "Settings", 220, 340, 160, 50, mouse),
        "quit": button(screen, "Quit", 220, 410, 160, 50, mouse)
    }


def game_over(screen, score, level):
    screen.fill((30, 0, 0))
    draw_text(screen, "GAME OVER", 180, 120, BIG)
    draw_text(screen, f"Score: {score}", 200, 200)
    draw_text(screen, f"Level: {level}", 200, 240)