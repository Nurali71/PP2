import pygame,random, time

#Some constants
WIDTH = 720
HEIGHT = 480

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255, 220, 0)  

#Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake_pos = [100,50]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                  random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
level = 1           
food_eaten = 0      
speed = 10          

def show_score(choice,color,font,size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

    level_surface = score_font.render('Level: ' + str(level), True, YELLOW)
    level_rect = level_surface.get_rect()
    level_rect.topleft = (0, 25)
    screen.blit(level_surface, level_rect)

def game_over():
    my_font = pygame.font.SysFont('Times New Roman', 50)
    gameover_surface = my_font.render('Your score is: ' + str(score), True, RED)
    gameover_rect = gameover_surface.get_rect()
    gameover_rect.midtop = (WIDTH/2, HEIGHT/2)

    screen.blit(gameover_surface, gameover_rect)
    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    #Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_position[0] and snake_pos[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
        food_eaten += 1  #Counting food

        if food_eaten % 3 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, 
                          random.randrange(1, (HEIGHT//10)) * 10]
        
    fruit_spawn = True
    screen.fill(BLACK)
    
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(screen, WHITE, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))

    #Boundaries
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()
    
    #Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    #Showing score
    show_score(1, WHITE, 'times new roman', 20)
    
    #Refreshing
    pygame.display.update()

    #FPS
    clock.tick(speed)  