import pygame, sys
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

size= (800,500)
screen=pygame.display.set_mode(size)
clock= pygame.time.Clock()
coord_x= 10
coord_y= 10
x_speed= 0
y_speed=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed=-3
            if event.key == pygame.K_RIGHT:
                x_speed=3
            if event.key == pygame.K_UP:
                y_speed= -3
            if event.key == pygame.K_DOWN:
                y_speed= 3
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0


    if(coord_x>720 or coord_x<0):
        x_speed *=-1
    if(coord_y>420 or coord_y<0):
        y_speed *=-1
    screen.fill(white)
    coord_x+= x_speed
    coord_y += y_speed
    pygame.draw.rect(screen, red,(coord_x,coord_y,100,100))

    pygame.display.flip()
    clock.tick(200)