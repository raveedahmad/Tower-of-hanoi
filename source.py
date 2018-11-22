white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
c0=(253,228,200)
c1=(223,185,151)
c2=(72,61,139)
c3=(227,161,115)
c4=(135,206,250)
c5=(72,61,139)
c7=(204,132,67)
c6=(187,109,74)
c8=(165,57,50)
c9=(165,57,40)
c10=(68,20,20)

colors=[c0,c1,c3,c7,c6,c8,c9,c10]

high_score=[0,0,0,7,15,31,63,127,255]

sound="Mute"

mutex=1257
mutey=310

import pygame
import time

pygame.init()

font1=pygame.font.SysFont(None,100,italic=False)
font2=pygame.font.SysFont(None,40,italic=False)
font3=pygame.font.SysFont(None,50,italic=False)
font4=pygame.font.SysFont(None,100,italic=True)
font5=pygame.font.SysFont(None,30,italic=False)
font6=pygame.font.SysFont(None,30)
font7=pygame.font.SysFont(None,80,italic=False)

def message_to_screen(f1,msg,color,x,y):
    screen_text = f1.render(msg,True,color)
    gamedisplay.blit(screen_text, [x,y])
    
gamedisplay=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption("TOWER OF HANOI")

m1=pygame.mixer.music.load("preview-happy-people-city.ogg")
pygame.mixer.music.play(-1)

i1=pygame.image.load("unnamed.jpg")
i2=pygame.image.load("Cover_v2.png")

for i in range (0,3):
    text="Loading ."
    for j in range (0,3):
        gamedisplay.blit(i2,[0,0])
        message_to_screen(font4,text,c3,100,600)
        pygame.display.update()
        time.sleep(0.5)
        text+="."

gamedisplay.blit(i1,[0,0])
pygame.display.update()
time.sleep(2)

pygame.draw.rect(gamedisplay,c4,[183,84,1000,600])

pygame.display.update()

message_to_screen(font1,"TOWERS  OF  HANOI",c2,353,94)
message_to_screen(font1,"Instructions",c5,493,250)
message_to_screen(font3,"1. Move only one disk at a time.",c5,203,350)
message_to_screen(font3,"2. A larger disk may not be placed on top of a smaller disk.",c5,203,390)
message_to_screen(font3,"3. All disks, except the one being moved, must be on a peg.",c5,203,430)
pygame.display.update()
for i in range(9,-1,-1):
    message_to_screen(font3,"0"+str(i),c5,200,650)
    pygame.display.update()
    pygame.draw.rect(gamedisplay,c4,[183,640,200,44])
    time.sleep(1)

def gameloop():

    global sound
    global mutex
    global mutey
    
    min_moves=0
    
    pygame.draw.rect(gamedisplay,c4,[183,150,1000,534])

    pygame.draw.rect(gamedisplay,c5,[318,584,230,50])
    pygame.draw.rect(gamedisplay,c5,[568,584,230,50])
    pygame.draw.rect(gamedisplay,c5,[818,584,230,50])

    message_to_screen(font7,"1",c4,419,585)
    message_to_screen(font7,"2",c4,669,585)
    message_to_screen(font7,"3",c4,919,585)

    pygame.draw.rect(gamedisplay,c5,[423,334,20,250])
    pygame.draw.rect(gamedisplay,c5,[673,334,20,250])
    pygame.draw.rect(gamedisplay,c5,[923,334,20,250])

    gameExit=False
    truth=False
    truth2=True
    truth3=False
    truth4=False
    
    nod=0
    
    input1=0
    input2=0
    
    l1=[0]*9
    l2=[0]*9
    l3=[0]*9
    l4=[1,2,3,4,5,6,7,8]
    goal=[]
    pygame.draw.rect(gamedisplay,c4,[183,84,169,70])
    moves=0
    message_to_screen(font2,"Enter the number of disks from \"3\" to \"8\"",black,421,214)

    pygame.display.update()
    
    while not gameExit:
        
        if min_moves>0:
            message_to_screen(font2,"Min ="+str(min_moves),c5,186,100)
        for event in pygame.event.get():
            if l1==[0]*9 and truth2 and not truth4:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        nod=3
                    elif event.key == pygame.K_4:
                        nod=4
                    elif event.key == pygame.K_5:
                        nod=5
                    elif event.key == pygame.K_6:
                        nod=6
                    elif event.key == pygame.K_7:
                        nod=7
                    elif event.key == pygame.K_8:
                        nod=8
                if nod:
                    message_to_screen(font2,"Press Space",red,403,264)
                    ab=40
                    min_moves=high_score[nod]
                    for bc in l4[-nod:]:
                        l1[bc]+=ab
                        ab+=20
                    goal=l1[:]
                    truth2=False

            if input1==0 and not truth2 and not truth4:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        truth3=True
                    if truth3:
                        pygame.draw.rect(gamedisplay,c4,[183,204,1000,120])
                        message_to_screen(font2,"Enter the swap",black,403,204)
                        message_to_screen(font2,"From tower: ",black,403,244)

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                input1=1
                                truth3=False
                                message_to_screen(font2,"Press Space",red,403,284)
                            elif event.key == pygame.K_2:
                                input1=2
                                truth3=False
                                message_to_screen(font2,"Press Space",red,403,284)
                            elif event.key == pygame.K_3:
                                input1=3
                                truth3=False
                                message_to_screen(font2,"Press Space",red,403,284)

            if input1 and (not(input2) or input2==input1) and not truth4:
                message_to_screen(font2,str(input1),red,583,244)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        truth=True
                        pygame.draw.rect(gamedisplay,c4,[183,274,1000,50])
                    if truth:
                        message_to_screen(font2,"To Tower: ",black,683,244)
                        if event.key == pygame.K_1:
                            input2=1
                        elif event.key == pygame.K_2:
                            input2=2
                        elif event.key == pygame.K_3:
                            input2=3
                    if input2 and input1!=input2:
                        message_to_screen(font2,str(input2),red,833,244)
                        truth=False
                        message_to_screen(font2,"Press Space",red,403,284)
        
            pygame.display.update()
            
        if input1 and input2 and input1!=input2 and not truth4:
            input1=int(input1)
            input2=int(input2)
            first=input1
            if input1==1 and l1.count(0)!=len(l1):
                input1=l1
            elif input1==2 and l2.count(0)!=len(l2):
                input1=l2
            elif input1==3 and l3.count(0)!=len(l3):
                input1=l3
            second=input2
            if input2==1:
                input2=l1
            elif input2==2:
                input2=l2
            elif input2==3:
                input2=l3
            if first!=input1 and second!=input2:
                a=input1.count(0)
                b=input2.count(0)
                if b!=len(input2):
                    if input2[b]>input1[a]:
                        input2[b-1]=input1[a]
                        moves+=1
                        pygame.draw.rect(gamedisplay,c4,[183,84,169,70])
                        message_to_screen(font2,"Moves ="+str(moves),c5,183,129)
                    else:
                        input1=0
                        input2=0
                        message_to_screen(font2,"Invalid Move",red,193,284)
                        continue
                else:
                    input2[b-1]=input1[a]
                    moves+=1
                    pygame.draw.rect(gamedisplay,c4,[183,84,169,70])
                    message_to_screen(font2,"Moves ="+str(moves),c5,183,129)
            else:
                input1=0
                input2=0
                message_to_screen(font2,"Invalid Move",red,193,284)
                continue
            if first==1:
                pygame.draw.rect(gamedisplay,c4,[x1,y1+17,(input1[a]-20)/2,15])
                pygame.draw.rect(gamedisplay,c5,[x1+(input1[a]-20)/2,y1+17,20,15])
                pygame.draw.rect(gamedisplay,c4,[x1+(input1[a]-20)/2+20,y1+17,input1[a]/2,15])

                l1=input1
                input1[a]=0
            elif first==2:
                pygame.draw.rect(gamedisplay,c4,[x2,y2+17,(input1[a]-20)/2,15])
                pygame.draw.rect(gamedisplay,c5,[x2+(input1[a]-20)/2,y2+17,20,15])
                pygame.draw.rect(gamedisplay,c4,[x2+(input1[a]-20)/2+20,y2+17,input1[a]/2,15])

                l2=input1
                input1[a]=0
            elif first==3:
                pygame.draw.rect(gamedisplay,c4,[x3,y3+17,(input1[a]-20)/2,15])
                pygame.draw.rect(gamedisplay,c5,[x3+(input1[a]-20)/2,y3+17,20,15])
                pygame.draw.rect(gamedisplay,c4,[x3+(input1[a]-20)/2+20,y3+17,input1[a]/2,15])

                l3=input1
                input1[a]=0
            if second==1:
                l1=input2
            elif second==2:
                l2=input2
            elif second==3:
                l3=input2
            if l1==[0]*9:
                input1=0
                input2=0
                continue

            input1=0
            input2=0

        if l1!=[0]*9 and not truth4:
            y1=564
            k=7
            for j in range (1,9):
                i=l1[-j]
                if i!=0:
                    x1=433-i/2                    
                    pygame.draw.rect(gamedisplay,colors[int((i-20)/20-1)],[x1,y1,i,15])
                    y1-=17
                    k-=1

        if l2!=[0]*9 and not truth4:
            y2=564
            for j in range (1,9):
                i=l2[-j]
                if i!=0:
                    x2=683-i/2                    
                    pygame.draw.rect(gamedisplay,colors[int((i-20)/20-1)],[x2,y2,i,15])
                    y2-=17

        if l3!=[0]*9 and not truth4:
            y3=564
            for j in range (1,9):
                i=l3[-j]
                if i!=0:
                    x3=933-i/2                    
                    pygame.draw.rect(gamedisplay,colors[int((i-20)/20-1)],[x3,y3,i,15])
                    y3-=17

        pygame.display.update()

        cur=pygame.mouse.get_pos()
        
        if 1230<cur[0]<1330 and 250<cur[1]<285:
            pygame.draw.rect(gamedisplay,c4,[1230,250,100,35])
            message_to_screen(font6,"Reset",c5,1255,260)
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(gamedisplay,c4,[183,184,1000,140])
                time.sleep(0.3)
                gameloop()
        else:
            pygame.draw.rect(gamedisplay,c5,[1230,250,100,35])
            message_to_screen(font6,"Reset",c4,1255,260)
        
        if 1230<cur[0]<1330 and 300<cur[1]<335:
            pygame.draw.rect(gamedisplay,c4,[1230,300,100,35])
            if sound=="Mute":
                message_to_screen(font6,sound,c5,mutex,mutey)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.pause()
                    sound="Unmute"
                    mutex=1243
                    time.sleep(0.3)
            else:
                message_to_screen(font6,sound,c5,mutex,mutey)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.unpause()
                    sound="Mute"
                    mutex=1257
                    time.sleep(0.3)
        else:
            pygame.draw.rect(gamedisplay,c5,[1230,300,100,35])
            message_to_screen(font6,sound,c4,mutex,mutey)

        if 1230<cur[0]<1330 and 350<cur[1]<385:
            pygame.draw.rect(gamedisplay,c4,[1230,350,100,35])
            message_to_screen(font6,"Quit",c5,1255,360)
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(gamedisplay,c4,[183,184,1000,500])
                message_to_screen(font1,"Bye Bye!",c5,540,344)
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gamedisplay,c5,[1230,350,100,35])
            message_to_screen(font6,"Quit",c4,1255,360)
        pygame.display.update()

        if l2==goal or l3==goal:
            pygame.draw.rect(gamedisplay,c4,[183,184,1000,140])
            pygame.display.update()
            time.sleep(1)
            pygame.draw.rect(gamedisplay,c4,[183,184,1000,500])
            message_to_screen(font1,"Mubarakaan",black,493,350)
            pygame.display.update()
            time.sleep(2)
            gameloop()
        pygame.display.update()
gameloop()

