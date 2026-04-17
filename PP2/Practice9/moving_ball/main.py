import pygame
from ball import Ball
pygame.init()
width,height=600, 400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball Game")
running=True
white=(255,255,255)
clock=pygame.time.Clock()

# Create ball object of the Class Ball
ball=Ball(width//2,height//2)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    ball.move(keys, width, height)
    screen.fill(white)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()