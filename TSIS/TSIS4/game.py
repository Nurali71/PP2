import pygame
import random
import config

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.dir = (1, 0)
        self.grow = False

    def out_of_bounds(self, width, height, grid_size):
        head_x, head_y = self.body[0]

        if head_x < 0 or head_y < 0:
            return True
        if head_x >= width // grid_size or head_y >= height // grid_size:
            return True

        return False

    def collide_self(self):
        return self.body[0] in self.body[1:]

    def move(self):
        head = self.body[0]
        new = (head[0] + self.dir[0], head[1] + self.dir[1])

        self.body.insert(0, new)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def collide_self(self):
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self):
        self.pos = (random.randint(0, 29), random.randint(0, 29))
        self.type = "normal"

    def respawn(self):
        self.pos = (random.randint(0, 29), random.randint(0, 29))

class Poison(Food):
    def __init__(self):
        super().__init__()
        self.type = "poison"