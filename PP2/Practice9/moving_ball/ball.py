import pygame
class Ball:
    def __init__(self,x,y, radius=25, speed=20):
        self.x=x
        self.y=y
        self.radius=radius
        self.speed=speed
    def move(self, keys, width, height):
        #boundary cheeeck
        if keys[pygame.K_LEFT]:
            if self.x-self.radius-self.speed>=0:
                self.x-=self.speed
        if keys[pygame.K_RIGHT]:
            if self.x+self.radius+self.speed<=width:
                self.x+=self.speed
        if keys[pygame.K_UP]:
            if self.y-self.radius-self.speed>=0:
                self.y-=self.speed
        if keys[pygame.K_DOWN]:
            if self.y+self.radius+self.speed<=height:
                self.y+=self.speed
    def draw(self, screen):
        pygame.draw.circle(screen,(254,0,0), (self.x, self.y), self.radius)