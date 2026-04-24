import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Paint')
    clock = pygame.time.Clock()

    radius = 15
    mode = 'pen'        # pen / rect / circle / eraser
    color = (100, 100, 255)
    points = []


    shape_start = None

    
    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))

    font = pygame.font.SysFont('Arial', 14)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                #Instruments
                if event.key == pygame.K_p: mode = 'pen'
                if event.key == pygame.K_r: mode = 'rect'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_e: mode = 'eraser'

                #Colors
                if event.key == pygame.K_1: color = (255, 255, 255)  #white
                if event.key == pygame.K_2: color = (255, 0,   0  )  #red
                if event.key == pygame.K_3: color = (0,   255, 0  )  #green
                if event.key == pygame.K_4: color = (100, 100, 255)  #blue
                if event.key == pygame.K_5: color = (255, 255, 0  )  #yellow
                if event.key == pygame.K_6: color = (255, 165, 0  )  #orange

                #Size
                if event.key == pygame.K_UP:   radius = min(60, radius + 2)
                if event.key == pygame.K_DOWN: radius = max(1,  radius - 2)

                #Deleting
                if event.key == pygame.K_DELETE:
                    canvas.fill((0, 0, 0))

            #Remembering start pos.
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shape_start = event.pos
                points = [event.pos]

            #Mouse unbuttoning 
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if shape_start:
                    ex, ey = event.pos
                    sx, sy = shape_start

                    if mode == 'rect':
                        x = min(sx, ex)
                        y = min(sy, ey)
                        w = abs(ex - sx)
                        h = abs(ey - sy)
                        pygame.draw.rect(canvas, color, (x, y, w, h), 3)

                    elif mode == 'circle':
                        cx = (sx + ex) // 2
                        cy = (sy + ey) // 2
                        r  = max(abs(ex - sx), abs(ey - sy)) // 2
                        pygame.draw.circle(canvas, color, (cx, cy), r, 3)

                shape_start = None
                points = []

            #Mouse motion
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  #LMB
                    points.append(event.pos)

                    if mode == 'pen' and len(points) >= 2:
                        drawLineBetween(canvas, points[-2], points[-1], radius, color)

                    elif mode == 'eraser':
                        pygame.draw.circle(canvas, (0, 0, 0), event.pos, radius * 2)

      
        screen.blit(canvas, (0, 0))

        hints = [
            f'Mode: {mode}  (P/R/C/E)',
            f'Color: 1-6',
            f'Size: {radius}  (UP/DOWN)',
            'DEL - clear',
        ]
        for i, text in enumerate(hints):
            surf = font.render(text, True, (200, 200, 200))
            screen.blit(surf, (5, 5 + i * 18))

        pygame.display.flip()
        clock.tick(60)

#Function from NerdParadise
def drawLineBetween(screen, start, end, width, color):
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(max(iterations, 1)):
        progress = 1.0 * i / max(iterations, 1)
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()