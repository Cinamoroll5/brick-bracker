
import pygame

width=400
height=400
#creating a game window
pygame.init()
gamescreen=pygame.display.set_mode((width,height))

radius=40

x_position=200

y_position=200

speedx=0
speedy=1


while True:
    x_position+=speedx
    y_position+=speedy
    buttons=pygame.event.get()
    for button in buttons:
        if button.type==pygame.QUIT:
            exit()#stop our code

    
    print("hello")
    gamescreen.fill((160, 32, 240))

    pygame.draw.circle(gamescreen,(255, 192, 203),(x_position,y_position),radius)


    if y_position>400:
        speedy=-speedy

    elif y_position<0:
        speedy=-speedy

    elif x_position<400:
        speedx=-speedx

    elif x_position<0:
        speedx=-speedx

    pygame.display.flip()



























































































































































































































