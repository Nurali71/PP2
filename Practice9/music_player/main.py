import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Easy Music Player")
font = pygame.font.SysFont("Arial", 20, bold=True)

playlist = [
    "music/nevada.mp3",
    "music/lowcortisolmusic.mp3",
    "music/outside.mp3"
]

player = MusicPlayer(playlist)

try:
    bg = pygame.image.load("music/nevada.jpg")
    bg = pygame.transform.scale(bg, (250, 250))
except:
    bg = pygame.Surface((250, 250)) # Если нет картинки, будет серый квадрат
    bg.fill((100, 100, 100))

running = True
while running:
    screen.fill((255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            print(f"{pygame.key.name(event.key)}")
            
            if event.key == pygame.K_p: player.play()
            if event.key == pygame.K_s: player.stop()
            if event.key == pygame.K_n: player.next()
            if event.key == pygame.K_b: player.prev()
            if event.key == pygame.K_q: running = False


    name = player.current_track_name().split('/')[-1]
    name_txt = font.render(f"Track: {name}", True, (50, 50, 50))
    screen.blit(name_txt, (20, 20))
    

    hint = font.render("P - Play | S - Stop | N - Next | B - Back | Q - Quit", True, (0, 0, 0))
    screen.blit(hint, (110, 350))

    pygame.display.flip()

pygame.quit()