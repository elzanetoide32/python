import pygame, sys
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
player_width= 15
player_heigh=90

size= (800,600)
screen=pygame.display.set_mode(size)

clock= pygame.time.Clock()
player1_x_coord=50
player1_y_coord=300-45
player1_y_speed=0

player2_x_coord=750- player_width
player2_y_coord=300-45
player2_y_speed=0

pelota_x=400
pelota_y=300
pelota_speed_x=3
pelota_speed_y=3

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            #jugador1
            if event.key==pygame.K_w:
                player1_y_speed= -3
            if event.key== pygame.K_s:
                player1_y_speed=3
            #jugador2
            if event.key==pygame.K_UP:
                player2_y_speed= -3
            if event.key== pygame.K_DOWN:
                player2_y_speed=3

        if event.type==pygame.KEYUP:
                #jugador1
            if event.key==pygame.K_w:
                player1_y_speed= 0
            if event.key== pygame.K_s:
                player1_y_speed=0
            #jugador2
            if event.key==pygame.K_UP:
                player2_y_speed= 0
            if event.key== pygame.K_DOWN:
                player2_y_speed=0

    

    if(player1_y_coord>520 or player1_y_coord<0):
        player1_y_speed *=-1

    if(player2_y_coord>520 or player2_y_coord<0):
        player2_y_speed *=-1

    if pelota_y>590 or pelota_y<10:
        pelota_speed_y*=-1

    if pelota_x>800:
        pelota_x=400
        pelota_y=300
        pelota_speed_x *=-1
        pelota_speed_y *=-1

    if pelota_x<0:
        pelota_x=400
        pelota_y=300
        pelota_speed_x *=-1
        pelota_speed_y *=-1


    player1_y_coord+=player1_y_speed
    player2_y_coord+=player2_y_speed

    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
        
    screen.fill(black)
    jugador1=pygame.draw.rect(screen, white,(player1_x_coord,player1_y_coord, player_width,player_heigh))
    jugador2=pygame.draw.rect(screen, white,(player2_x_coord,player2_y_coord, player_width,player_heigh))
    pelota=pygame.draw.circle(screen,white,(pelota_x, pelota_y),10)
    
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *=-1

    
    pygame.display.flip()
    clock.tick(80)



