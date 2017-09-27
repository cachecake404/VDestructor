#2player snake by sam :)
import time
import pygame ,pygame.mixer , sys
import random
pygame.init()
font = pygame.font.SysFont("Arial",15)
font1 = pygame.font.SysFont("Arial",10)
title = pygame.font.SysFont("Arial",90)
def mess(msg,color):
    screen_text = font.render(msg, True , color)
    display.blit(screen_text , [(w/2) - 200 , h/2] )
    
def mess1(color,msg,k,x):
    screen_text = font1.render(msg, True , color)
    display.blit(screen_text , [k , x] )
pygame.mixer.music.load("track.mp3")
pygame.mixer.music.play()
background = pygame.image.load('sback.jpg')
background2 = pygame.image.load('back.jpg')
score = 0
w = 800
h = 600
display = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
pygame.display.update()
pygame.display.init()
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
pink   = (255,0,255)
green =  (106,90,205)
bye = True #main
scr = False #menu
inst = True #instructions
crd = True #credits
crd2 = True #creditssecondaryexit
qutz = True
move = False
move1 = False
reset = True
xpos = w/2
ypos = h/2
xpos2 = (w/2) - 100
ypos2 = (h/2) - 100
xch  = 0
ych  = 0
xch2 = 0
ych2 = 0
b    = 10
c    = 10
thick = 20
wa = random.randrange(1,70)*10
ha = random.randrange(1,50)*10
time = pygame.time.Clock()
FPS = 10
up = False
side = False
up2 = False
side2 = False
lenth = 1
lenth2= 1
snakelist = []
snakelist2 = []
snakehead = []
snakehead2 = [2] #put a int here to skip first check of head = head
def snake(b,snakelist):
    for i in snakelist:
        display.fill(red , rect = [i[0] , i[1] , b ,b ] )

def snake2(c,snake2list):
    for i in snake2list:
        display.fill(pink , rect = [i[0] , i[1] , c ,c ] )         

while True:
 
    while not scr:
     
        display.blit(background, [0, 0])
        screen_text = font.render("Press the keys for following :-" , True , black)
        display.blit(screen_text , [(w/2) -200 , h/2] )
        screen_text3 = font.render("S - Start  ,  I - Instruction  ,  C - Credits  " , True , black)
        display.blit(screen_text3 , [(w/2) -200 , h/2 + 50] )
        screen_text3 = font.render("Press X to Quit anytime during game!  " , True , black)
        display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
        screen_text2 = title.render("SNAKE WARS!", True , red)
        display.blit(screen_text2 , [(w/2) - 220 , (h/2) - 250] )
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    bye = False
                    scr = True
                    break
                if event.key == pygame.K_i:
                    scr = True
                    inst = False
                    break
                if event.key == pygame.K_c:
                    crd = False
                    scr = True
                    break
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
     
    while not inst:
        display.fill(white)
        screen_text = font.render("Rules : - Eat black box(apple) to gain length, player with longer length eats other player!" , True , black)
        display.blit(screen_text , [(w/2) -390 , h/2 - 200] )
        screen_text2 = font.render("             - If player try to eat each other at same length its a draw!" , True , black)
        display.blit(screen_text2 , [(w/2) -390 , h/2 - 170] )
        screen_text3 = font.render("             - If player trys to turn too fast , he ends up eating himself!" , True , black)
        display.blit(screen_text3 , [(w/2) -390 , h/2 - 150] )
        screen_text4 = font.render("Movments Player one(Red) :-  W - Up , S - Down , A - Left , D - Right " , True , red )
        display.blit(screen_text4 , [(w/2) -390 , h/2 - 100] )
        screen_text5 = font.render("Movments Player two(Pink) :-  I - Up , K - Down , J - Left , L - Right" , True , pink)
        display.blit(screen_text5 , [(w/2) -390 , h/2 - 50] )
        screen_text6 = font.render("Press B to go back to main menu! " , True , black)
        display.blit(screen_text6 , [(w/2) -390 , h/2 ] )
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    inst = True
                    scr = False
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
     
     
    while not crd:
        display.fill(white)
        screen_text = font.render("Created by Sam Thomas" , True , red)
        display.blit(screen_text , [(w/2) -200 , h/2] )
        screen_text2 = font.render("Press the B to go back to main menu!" , True , black)
        display.blit(screen_text2 , [(w/2) -200 , h/2 + 100] )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    crd = True
                    scr = False
                    break
            if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
     
    while not crd2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                        pygame.quit()
                        quit()
     
        display.fill(white)
        screen_text = font.render("Created by Sam Thomas , Go ahead Press X and quit now!" , True , red)
        display.blit(screen_text , [(w/2) - 200 , h/2] )
        pygame.display.update()
           
    while not bye:
       
        if snakehead == snakehead2 or snakehead2 == snakehead:
            if lenth2 > lenth and reset == True:
                xch = 0
                ych = 0
                display.fill(black)
                mess("Pink was bigger , ate red! Pink wins!",pink)
                screen_text3 = font.render("Press C to proceed to credits and  quit! " , True , pink)
                display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                screen_text = font.render("Press R to play again!", True , green)
                display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                pygame.display.update()
                xpos = w/2
                ypos = h/2
                xpos2 = (w/2) - 100
                ypos2 = (h/2) - 100
                bye = True
                qutz = False
                break
            if lenth > lenth2 and reset == True :
                xch = 0
                ych = 0
                display.fill(black)
                mess("Red was bigger , ate pink! Red wins!",red)
                screen_text3 = font.render("Press C to proceed to credits and  quit!  " , True , pink)
                display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                screen_text = font.render("Press R to play again!", True , green)
                display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                pygame.display.update()
                xpos = w/2
                ypos = h/2
                xpos2 = (w/2) - 100
                ypos2 = (h/2) - 100
                bye = True
                qutz = False
                break
            if lenth2 == lenth and reset ==  True:
                xch = 0
                ych = 0
                display.fill(black)
                mess("Both red and pink fought and both are now dead! Draw!",yellow)
                screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
                display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
                screen_text = font.render("Press R to play again!", True , green)
                display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                pygame.display.update()
                xpos = w/2
                ypos = h/2
                xpos2 = (w/2) - 100
                ypos2 = (h/2) - 100
                bye = True
                qutz = False
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and up == False and move == False:
                    ych = -b
                    xch = 0
                    up = True
                    side = False
                    move = True
                if event.key == pygame.K_s and up == False and move == False:
                    ych = +b
                    xch = 0
                    up = True
                    side = False
                    move = True
                if event.key ==pygame.K_d and side == False and move == False:
                    xch = +b
                    ych = 0
                    side = True
                    up = False
                    move = True
                    
                if event.key == pygame.K_a and side == False and move == False:
                    xch = -b
                    ych = 0
                    side = True
                    up = False
                    move = True
                if event.key == pygame.K_UP and up2 == False and move1 == False:
                    ych2 = -c
                    xch2 = 0
                    up2 = True
                    side2 = False
                    move1 = True
                if event.key == pygame.K_DOWN and up2 == False and move1 == False:
                    ych2 = +c
                    xch2 = 0
                    up2 = True
                    side2 = False
                    move1 = True
                if event.key ==pygame.K_RIGHT and side2 == False and move1 == False :
                    xch2 = +c
                    ych2 = 0
                    side2 = True
                    up2 = False
                    move1 = True
                    
                if event.key == pygame.K_LEFT and side2 == False and move1 == False:
                    xch2 = -c
                    ych2 = 0
                    side2 = True
                    up2 = False
                    move1 = True
                if event.key == pygame.K_x:
                   
                    pygame.quit()
                    quit()
     
                    
        if xpos >= wa  and ypos >= ha and xpos <= wa + thick and ypos <= ha + thick:
            
            wa = random.randrange(1,70)*10
            ha = random.randrange(1,50)*10
            lenth = lenth + 5
        if xpos2 >= wa  and ypos2 >= ha and xpos2 <= wa + thick and ypos2 <+ ha + thick:
            
            wa = random.randrange(1,70)*10
            ha = random.randrange(1,50)*10
            lenth2 = lenth2 + 5    
            
        if xpos == w - 10  or xpos == 0 or ypos == h - 10 or ypos == 0:
            xch = 0
            ych = 0
            display.fill(black)
            
            mess("You hit a wall , sucker! , Pink Wins ! " , pink)
            screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
            display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
            screen_text = font.render("Press R to play again!", True , green)
            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
            pygame.display.update()
            bye = True
            qutz = False
            break
        if xpos2 == w - 10  or xpos2 == 0 or ypos2 == h - 10 or ypos2 == 0:
            xch2 = 0
            ych2 = 0
            display.fill(black)
            mess("You hit a wall , sucker! Red Wins ! " , red)
            screen_text3 = font.render("Press C to proceed to credits an quit!  " , True , pink)
            display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
            screen_text = font.render("Press R to play again!", True , green)
            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
            bye = True
            qutz = False
            pygame.display.update()
            break
                    
        xpos = xpos + xch
        ypos = ypos + ych
        xpos2 = xpos2 +xch2
        ypos2 = ypos2 +ych2
        time.tick(FPS)
                    
        
        display.fill(white)
        display.blit(background2, [0, 0])
        snakehead = []
        snakehead.append(xpos)
        snakehead.append(ypos)
        snakelist.append(snakehead)
        snakehead2 = []
        snakehead2.append(xpos2)
        snakehead2.append(ypos2)
        snakelist2.append(snakehead2)
        
        if len(snakelist) > lenth:
            del snakelist [0]
        if len(snakelist2) > lenth2:
            del snakelist2 [0]
        
        snake(b,snakelist)
        snake2(c,snakelist2)
        mess1(green,"Red:"+str(lenth),4,4)
        mess1(green,"Pink"+str(lenth2),w-50,4)
        display.fill(black, rect=[wa,ha,thick,thick])  #food
        pygame.display.update()
        for segm in snakelist [:-1]:
            if segm == snakehead and reset == True:
                xch = 0
                ych = 0
                display.fill(black)
                
                mess("You ate yourself , stupid! Pink wins",pink)
                screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
                display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
                screen_text = font.render("Press R to play again!", True , green)
                display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                pygame.display.update()
                bye = True
                qutz = False
                break
        for segm2 in snakelist2 [:-1] :
                if segm2 == snakehead2 and reset == True:
                    xch2 = 0
                    ych2 = 0
                    display.fill(black)
                    mess("You ate yourself , stupid! Red wins",red)
                    screen_text = font.render("Press R to play again!", True , green)
                    display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                    screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
                    display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
                    pygame.display.update()
                    bye = True
                    qutz = False
                    break
        for seg in snakelist [:-1]:
            
            if snakehead2 == seg:
                        if lenth2 > lenth and reset == True:
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Pink was bigger , ate red! Pink wins!",pink)
                            screen_text3 = font.render("Press C to proceed to credits and  quit! " , True , pink)
                            display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
                        if lenth > lenth2 and reset == True :
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Red was bigger , ate pink! Red wins!",red)
                            screen_text3 = font.render("Press C to proceed to credits and  quit!  " , True , pink)
                            display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
                        if lenth2 == lenth and reset ==  True:
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Both red and pink fought and both are now dead! Draw!",yellow)
                            screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
                            display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
        for seg2 in snakelist2 [:-1]:
            
            if snakehead == seg2:
                        if lenth2 > lenth and reset == True:
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Pink was bigger , ate red! Pink wins!",pink)
                            screen_text3 = font.render("Press C to proceed to credits and  quit! " , True , pink)
                            display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
                        if lenth > lenth2 and reset == True :
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Red was bigger , ate pink! Red wins!",red)
                            screen_text3 = font.render("Press C to proceed to credits and  quit!  " , True , pink)
                            display.blit(screen_text3 , [(w/2) - 200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
                        if lenth2 == lenth and reset ==  True:
                            xch = 0
                            ych = 0
                            display.fill(black)
                            mess("Both red and pink fought and both are now dead! Draw!",yellow)
                            screen_text3 = font.render("Press C to proceed to credits and quit!  " , True , pink)
                            display.blit(screen_text3 , [(w/2) -200 , h/2 + 100] )
                            screen_text = font.render("Press R to play again!", True , green)
                            display.blit(screen_text , [(w/2) - 200 , h/2 + 200] )
                            pygame.display.update()
                            xpos = w/2
                            ypos = h/2
                            xpos2 = (w/2) - 100
                            ypos2 = (h/2) - 100
                            bye = True
                            qutz = False
                            break
        reset = True
        move = False
        move1 = False
                
    while not qutz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    qutz = True 
                    crd2 = False
                    bye = True 
                    break
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    lenth = 1
                    lenth2 = 1
                    qutz = True
                    bye = False
                    xpos = w/2
                    ypos = h/2
                    xpos2 = (w/2) - 100
                    ypos2 = (h/2) - 100
                    xch = 0
                    ych = 0
                    xch2 = 0
                    ych2 = 0
                    snakelist = []
                    snakehead = []
                    snakehead2 = [2]
                    snakelist2 = []
                    reset = False
                    up = False
                    side = False
                    up2 = False
                    side2 = False
                    break
                
     
