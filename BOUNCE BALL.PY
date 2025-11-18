import pygame
from typing import List
width=1200
height=800
#creating a game window
pygame.init()
gamescreen=pygame.display.set_mode((width,height))

pygame.mixer.init()
song=pygame.mixer.music.load(
"mixkit-cant-get-you-off-my-mind-1210.mp3"
)
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play()


bounce=pygame.mixer.Sound(
"mixkit-game-ball-tap-2073.wav"
)





radius=40

x_position=600

y_position=600
speedx=2
speedy=2

allbricks:List[pygame.Rect]=[]

def makebricks():
    for number in range(0,20):
        brick=pygame.Rect(0+60*number,0,50,50)
        allbricks.append(brick)

    for number in range(0,20):
        brick=pygame.Rect(0+60*number,60,50,50)
        allbricks.append(brick)

    for number in range(0,20):
        brick=pygame.Rect(0+60*number,120,50,50)
        allbricks.append(brick)



ballrect=pygame.Rect(x_position,y_position,radius,radius)


brickhit=None

paddlex_position=600
paddley_position=790


paddlerect=pygame.Rect(paddlex_position,paddley_position,160,20)

hearts=3


pygame.font.init()
my_font=pygame.font.SysFont('freesanbold.ttf',30)



score=0





makebricks()


while True:
    x_position+=speedx
    y_position+=speedy
    buttons=pygame.event.get()
    for button in buttons:
        if button.type==pygame.QUIT:
            exit()#stop our code
    if brickhit is not None:
        allbricks.remove (brickhit)
        score+=1
        brickhit=None

    print("hello")
    gamescreen.fill((160, 32, 240))

    text=my_font.render("lives:"+str(hearts),True,(0,0,0))   
    gamescreen.blit(text,(10,750))



    text=my_font.render("score:"+str(score),True,(0,0,0))  
    gamescreen.blit(text,(10,690))


    pygame.draw.rect(gamescreen,(0,0,0),paddlerect)
    for brick in allbricks:
        pygame.draw.rect( gamescreen,(0,0,0) ,brick)


    for brick in allbricks:
 
        answer= brick.colliderect(ballrect)
        if answer==True:
            bounce.play()
            speedy=-speedy
            y_position=brick.y+50+40
            brickhit=brick
        

    buttons=pygame.key.get_pressed()
    if buttons[pygame.K_LEFT]and paddlex_position>0:
        paddlex_position-=3
    elif buttons[pygame.K_RIGHT]and paddlex_position<1200:
        paddlex_position+=3
    paddlerect.centerx=paddlex_position

    ballrect=pygame.Rect(x_position-radius,y_position-radius,radius*2,radius*2)
    answer2= paddlerect.colliderect(ballrect)
    if answer2==True:
     speedy=-speedy

    pygame.draw.circle(gamescreen,(255, 192, 203),(x_position,y_position),radius)


    if y_position+radius>height:
        speedy=-speedy
        hearts-=1
    elif y_position-radius<0:
        speedy=-speedy

    elif x_position+radius>width:
        speedx=-speedx

    elif x_position-radius<0:
        speedx=-speedx



    if hearts<1 and buttons [pygame.K_r]:
        allbricks=[]
        makebricks()
        score=0
        hearts=3

    
    if hearts==0:
        allbricks=[]
        makebricks()
        score=0
        hearts=3

















    pygame.display.flip()








































































































































































