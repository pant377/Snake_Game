import pygame
game = True
pygame.init
clock = pygame.time.Clock()
display = pygame.display.set_mode((500,400))
pygame.display.update()
pygame.display.set_caption('Snake game')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
pygame.draw.rect(display,[0,0,255],[x1,y1,13,13])
pygame.display.update()
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
    if x1 < 0 or x1 >= 301 or y1 < 0 or y1 >= 301:
        game = False
    x1 += x1_change
    y1 += y1_change    
    display.fill(black)
    pygame.draw.rect(display,[0,0,255],[x1,y1,13,13])
    pygame.display.update()    
    clock.tick(10)
    
        
pygame.quit()
quit()