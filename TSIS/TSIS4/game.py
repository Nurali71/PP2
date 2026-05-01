import pygame
import random

GRID_SIZE = 20 # Logical size of one cell

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)] # Initial segments
        self.dir = (1, 0) # Moving Right by default
        self.grow = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.dir[0], head[1] + self.dir[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def shorten(self):
        for _ in range(2):
            if len(self.body) > 0:
                self.body.pop()
        return len(self.body) <= 1 # Death condition from poison

class Food:
    def __init__(self, color=(255, 200, 0)):
        self.pos = (0, 0)
        self.color = color

    def respawn(self, snake_body, obstacles):
        while True:
            new_pos = (random.randint(0, 29), random.randint(0, 29))
            if new_pos not in snake_body and new_pos not in obstacles:
                self.pos = new_pos
                break

class Obstacle:
    def __init__(self, level, snake_body):
        self.blocks = []
        # Generate walls starting from Level 3
        if level >= 3:
            for _ in range(level * 2):
                pos = (random.randint(0, 29), random.randint(0, 29))
                if pos not in snake_body:
                    self.blocks.append(pos)