import pygame
import datetime

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen

        self.bg = pygame.image.load("images/main-clock.png")
        self.hand_min = pygame.image.load("images/right-hand.png")
        self.hand_sec = pygame.image.load("images/left-hand.png")
        self.center = (300, 300) 

    def update(self):
        now = datetime.datetime.now()
        self.angle_sec = 90 - (now.second * 6)
        self.angle_min = 90 - (now.minute * 6)

    def draw(self):
        self.screen.fill((255, 255, 255))
        bg_res = pygame.transform.scale(self.bg, (600, 600))
        self.screen.blit(bg_res, (0, 0))

        self._draw_hand(self.hand_min, self.angle_min)
        self._draw_hand(self.hand_sec, self.angle_sec)

    def _draw_hand(self, image, angle):
        rotated_img = pygame.transform.rotate(image, angle)
        rect = rotated_img.get_rect(center=self.center)
        self.screen.blit(rotated_img, rect)