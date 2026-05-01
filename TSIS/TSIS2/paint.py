import pygame
import sys
import tools

pygame.init()
#screen
WIDTH, HEIGHT = 800, 600
UI_HEIGHT = 120
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App - TSIS2")
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
colors = [BLACK, RED, BLUE, GREEN]
current_color = BLACK

#state
tool = "brush"
thickness_levels = [2, 5, 10]
thickness_index = 1
thickness = thickness_levels[thickness_index]
drawing = False
start_pos = None
prev_pos = None
text_mode = False
text_input = ""
text_pos = (0, 0)
font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

#UI
def draw_ui():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, UI_HEIGHT))

    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (10 + i * 40, 10, 30, 30))

    tools_list = ["brush", "pencil", "line", "rect", "circle",
                  "eraser", "fill", "text", "square"]

    for i, t in enumerate(tools_list):
        text = font.render(t, True, BLACK)
        screen.blit(text, (10 + (i % 6) * 120, 50 + (i // 6) * 25))

    size_text = font.render(f"Size: {thickness}", True, BLACK)
    screen.blit(size_text, (10, 100))


while True:
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#tools display
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_y:
                tool = "square"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_f:
                tool = "fill"
            elif event.key == pygame.K_t:
                tool = "text"

            # size display
            elif event.key == pygame.K_1:
                thickness_index = 0
            elif event.key == pygame.K_2:
                thickness_index = 1
            elif event.key == pygame.K_3:
                thickness_index = 2
            thickness = thickness_levels[thickness_index]

            # save
            if event.key == pygame.K_s:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    tools.save_canvas(canvas)

            # text input
            if text_mode:
                if event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_input = ""

                elif event.key == pygame.K_RETURN:
                    render = font.render(text_input, True, current_color)
                    canvas.blit(render, text_pos)
                    text_mode = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        #MOUSEDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # color pick
            for i, col in enumerate(colors):
                if 10 + i * 40 <= x <= 40 + i * 40 and 10 <= y <= 40:
                    current_color = col

            if tool == "text":
                text_mode = True
                text_pos = event.pos

            elif tool == "fill":
                tools.flood_fill(canvas, x, y, current_color, WIDTH, HEIGHT)

            else:
                drawing = True
                start_pos = event.pos
                prev_pos = event.pos

        #MOUSEMOVE
        if event.type == pygame.MOUSEMOTION and drawing:

            if tool == "pencil":
                tools.draw_pencil(canvas, current_color, prev_pos, event.pos, thickness)
                prev_pos = event.pos

            elif tool == "brush":
                tools.draw_brush(canvas, current_color, event.pos, thickness)

            elif tool == "eraser":
                tools.draw_eraser(canvas, event.pos, thickness)

        #MOUSEUP
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "line":
                tools.draw_line(canvas, current_color, start_pos, end_pos, thickness)

            elif tool == "rect":
                tools.draw_rect(canvas, current_color, start_pos, end_pos, thickness)

            elif tool == "circle":
                tools.draw_circle(canvas, current_color, start_pos, end_pos, thickness)

            elif tool == "square":
                tools.draw_square(canvas, current_color, start_pos, end_pos, thickness)

    if text_mode:
        preview = font.render(text_input, True, current_color)
        screen.blit(preview, text_pos)

    draw_ui()
    pygame.display.flip()
    clock.tick(60)