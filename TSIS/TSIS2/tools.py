import pygame
from datetime import datetime
from collections import deque

#flood fill
def flood_fill(surface, x, y, fill_color, width, height):
    try:
        target_color = surface.get_at((x, y))
    except:
        return

    if target_color == fill_color:
        return

    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        if cx < 0 or cy < 0 or cx >= width or cy >= height:
            continue

        if surface.get_at((cx, cy)) != target_color:
            continue

        surface.set_at((cx, cy), fill_color)

        q.append((cx + 1, cy))
        q.append((cx - 1, cy))
        q.append((cx, cy + 1))
        q.append((cx, cy - 1))

#save
def save_canvas(surface):
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"paint_{time}.png"
    pygame.image.save(surface, filename)
    print("Saved:", filename)

#draw helpers
def draw_line(surface, color, start, end, thickness):
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.rect(surface, color,
                     pygame.Rect(start, (x2 - x1, y2 - y1)),
                     thickness)

def draw_circle(surface, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, thickness)

def draw_square(surface, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surface, color,
                     pygame.Rect(x1, y1, side, side),
                     thickness)

def draw_eraser(surface, pos, thickness):
    pygame.draw.circle(surface, (255, 255, 255), pos, thickness)

def draw_brush(surface, color, pos, thickness):
    pygame.draw.circle(surface, color, pos, thickness)

def draw_pencil(surface, color, prev, current, thickness):
    pygame.draw.line(surface, color, prev, current, thickness)