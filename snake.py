import pygame
import time
import random
game = True
pygame.init
clock = pygame.time.Clock()
display = pygame.display.set_mode((500,400))
pygame.display.update()
pygame.display.set_caption('Snake game')
red = (255, 0, 0)
blue = (0,0,255)
lblue = (120, 110, 200)
green = (0,255,255)
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1
foodx = round(random.randrange(0, 490 - 13)/10.0)*10.0
foody = round(random.randrange(0, 392 - 13)/10.0)*10.0
kilx = round(random.randrange(0, 490 - 13)/10.0)*10.0
kily = round(random.randrange(0, 392 - 13)/10.0)*10.0
def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], 13, 13])
while game:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0       
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10     
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10    
    x1 += x1_change
    y1 += y1_change    
    display.fill(lblue)
    pygame.draw.rect(display,green,[foodx,foody,10,10])
    pygame.draw.rect(display,red,[kilx,kily,10,10])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_List.append(snake_head)
    if len(snake_List) > Length_of_snake:
            del snake_List[0]
    our_snake(snake_List)
    pygame.display.update()    
    for x in snake_List[:-2]:
            if x == snake_head:
                game = False
    if x1 == kilx and y1 == kily:
        game = False
    if x1 == foodx and y1 == foody:
            kilx = round(random.randrange(0, 490 - 13)/10.0)*10.0
            kily = round(random.randrange(0, 392 - 13)/10.0)*10.0
            foodx = round(random.randrange(0, 490 - 13)/10.0)*10.0
            foody = round(random.randrange(0, 392 - 13)/10.0)*10.0
            Length_of_snake += 1
    clock.tick(10)
    if x1 <= 0 or x1 >= 490 or y1 <= 0 or y1 >= 390:
        game = False

        
pygame.quit()
quit()