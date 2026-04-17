import pygame
from player import MusicPlayer
pygame.init()
width,height=600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Music Player")

font=pygame.font.SysFont(None,24)

playlist=[
    ("music/nevada_slowed.wav.mp3", "music/nevada_bg.jpg"),
]
player = MusicPlayer(playlist)
clock=pygame.time.Clock()
current_image=pygame.image.load(player.get_current_image())
current_image=pygame.transform.scale(current_image,(250,250))
running=True
while running:
    screen.fill((239, 210, 203))
    screen.blit(current_image,(175,120))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                player.play()
                current_image=pygame.image.load(player.get_current_image())
                current_image=pygame.transform.scale(current_image,(250,250))
            elif event.key==pygame.K_s:
                player.stop()
            elif event.key==pygame.K_n:
                player.next_track()
                current_image=pygame.image.load(player.get_current_image())
                current_image=pygame.transform.scale(current_image,(250,250))
            elif event.key==pygame.K_b:
                player.prev_track()
                current_image=pygame.image.load(player.get_current_image())
                current_image=pygame.transform.scale(current_image,(250,250))
            elif event.key==pygame.K_q:
                running=False
    
    #Showing current track
    track_text=font.render(
        f"Now Playing: {player.get_current_track().split('/')[-1]}",
        True,
        (66, 76, 85)
    )
    screen.blit(track_text,(50,85))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()