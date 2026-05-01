import pygame
import sys
from clock import MickeyClock

pygame.init()

# У тебя в коде 600x600, убедись, что картинка часов влезет
WIDTH, HEIGHT = 600, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# создаем объект часов
mickey = MickeyClock(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # обновление логики (время и углы)
    mickey.update()

    # рисование (фон и руки)
    mickey.draw()

    pygame.display.flip()
    clock.tick(60)