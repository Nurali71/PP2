import pygame
import sys
pygame.init()
#Screen
WIDTH, HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint App")
#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

colors=[BLACK,RED,BLUE,GREEN]
current_color=BLACK
#Tools
tool='brush'
thickness=5
clock=pygame.time.Clock()
drawing=False
start_pos=None
screen.fill(WHITE)
def draw_ui():
    #UI
    pygame.draw.rect(screen, WHITE, (0,0, WIDTH, 120))
    #Draw color pallete
    for i, col in enumerate(colors):
        pygame.draw.rect(screen,col,(10+i*40, 10,30,30))
    #Draw tool labels
    font=pygame.font.SysFont(None,24)
    tools=['brush', 'rect', 'circle', 'eraser', 'square', 'rtriangle', 'etriangle', 'rhombus']
    for i, t in enumerate(tools):
        text=font.render(t, True, BLACK)
        screen.blit(text,(10+i*80, 50))
    #thickness display
    font=pygame.font.SysFont(None,24)
    text=font.render(f"Thickness: {thickness}", True, BLACK)
    screen.blit(text,(10,80))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Mouse down
        if event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            start_pos=event.pos

            x,y=event.pos
            #Check color selection
            for i, col in enumerate(colors):
                if 10+i*40<=x<=40+i*40 and 10<=y<=40:
                    current_color=col
        #Tool selection (keys)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_b:
                tool='brush'
            elif event.key==pygame.K_r:
                tool='rect'
            elif event.key==pygame.K_c:
                tool='circle'
            elif event.key==pygame.K_e:
                tool='eraser'
            elif event.key==pygame.K_s:
                tool='square'
            elif event.key==pygame.K_t:
                tool='rtriangle'
            elif event.key==pygame.K_y:
                tool='etriangle'
            elif event.key==pygame.K_h:
                tool='rhombus'
            #thickness control
            elif event.key==pygame.K_UP:
                thickness+=1
            elif event.key==pygame.K_DOWN:
                thickness=max(1, thickness-1)
        #Mouse up
        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            end_pos=event.pos
            x1,y1=start_pos
            x2,y2=end_pos
            width=x2-x1
            height=y2-y1
            if tool=='rect':
                rect=pygame.Rect(start_pos,(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen,current_color,rect,thickness)
            elif tool=='circle':
                radius=int(((end_pos[0]-start_pos[0])**2+(end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen,current_color, start_pos, radius, thickness)
            elif tool=='square':
                #Make width=height(smallest side)
                side=min(abs(width), abs(height))
                rect=pygame.Rect(x1,y1,side,side)
                pygame.draw.rect(screen, current_color, rect, thickness)
            elif tool=='rtriangle':
                points=[
                    (x1,y1), #start
                    (x1,y2), #vertical end
                    (x2,y2) #horizontal end
                ]
                pygame.draw.polygon(screen, current_color, points, thickness)
            elif tool=='etriangle':
                #side length based on drag distance
                side=((width)**2+(height)**2)**0.5
                #height of eq. traingle
                h=side*(3**0.5/2)
                points=[
                    (x1,y1), 
                    (x1+side,y1),
                    (x1+side/2,y1-h)
                ]
                pygame.draw.polygon(screen,current_color,points,thickness)
            elif tool=='rhombus':
                #center
                cx=(x1+x2)//2
                cy=(y1+y2)//2
                #half widths
                dx=abs(x2-x1)//2
                dy=abs(y2-y1)//2
                points=[
                    (cx,cy-dy), #top
                    (cx+dx,cy), #right
                    (cx, cy+dy), #bottom
                    (cx-dx,cy) #left
                ]
                pygame.draw.polygon(screen, current_color,points, thickness)
    #Drawing while moving
    if drawing:
        mouse_pos=pygame.mouse.get_pos()
        if tool=='brush':
            pygame.draw.circle(screen, current_color, mouse_pos, thickness)
        elif tool=='eraser':
            pygame.draw.circle(screen, WHITE, mouse_pos, thickness)
    draw_ui()
    pygame.display.flip()
    clock.tick(60)