import pygame  
from time import *
from random import *
pygame.init()
screen=pygame.display.set_mode((1000,700))
screen.fill((255,215,0))
clock=pygame.time.Clock()

x1=20
y1=300

x2=980
y2=300

ttt=3

bx=4
by=4

ball_x=487.5
ball_y=337.5

move_s=False
move_w=False

move_l=False
move_o=False

while ttt<5:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_w:
                move_w=True
            if event.key==pygame.K_s:
                move_s=True

            if event.key==pygame.K_l:
                move_l=True
            if event.key==pygame.K_o:
                move_o=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                move_w=False
            if event.key==pygame.K_s:
                move_s=False
            
            if event.key==pygame.K_l:
                move_l=False
            if event.key==pygame.K_o:
                move_o=False
    
    ball_x+=bx
    ball_y+=by

    if ball_y>=675:
        by*=-1
    if ball_y<=0:
        by*=-1
    



    if move_s==True and y1 < 600:
        y1+=5
    if move_w==True and y1 >0:
        y1-=5

    if move_l==True and y2 < 600:
        y2+=5
    if move_o==True and y2 >0:
        y2-=5
    
    hero1=pygame.draw.rect(screen,((63,72,204)),pygame.Rect(x1,y1,10,100))
    hero2=pygame.draw.rect(screen,((0,128,0)),pygame.Rect(x2,y2,10,100))

    pole=pygame.draw.rect(screen,((255,255,255)),pygame.Rect(497.5,3,5,694))

    ball=pygame.draw.rect(screen,((255,0,0)),pygame.Rect(ball_x,ball_y,25,25))

    if ball.colliderect(hero2):
        bx*=-1
    if ball.colliderect(hero1):
        bx*=-1


    if ball_x<-25:
        ttt=6
        tim3=pygame.font.Font(None,80).render('Green Win',True,(0,120,0))
    if ball_x>1000:
        ttt=6
        tim3=pygame.font.Font(None,80).render('Blue Win',True,(0,0,120))
    
    pygame.display.update()
    clock.tick(60)

screen.fill((0,0,0))
screen.blit(tim3,(200,250))
for i in range(2000):
    pygame.display.update()