import pygame,time,random
pygame.init()
w = 1080 # resolution width
h = 720 # resolution height
display = pygame.display.set_mode((w,h))
font = pygame.font.Font(None,25) #font size
#colours
red = [205,92,92]
white = [255,255,255]
black = [0,0,0]
yellow = [255,255,0]
#fill background
display.fill(yellow)
pygame.display.update()

#snake values
xpos =  w/2 #current position
ypos = h/2 #current position
xch = 0 #change to position
ych = 0 #change to position
b = 10 #movment block size
lenth = 1 #starting size 
snakelist = [] #list containing snakehaeds
snakehead = [] #list containing cordinates for head
#apple value
wa = random.randrange(1, w/10) * 10
ha = random.randrange(1 , h/10) * 10
thick = 10
#fps
FPS = 30
time = pygame.time.Clock()
#states
bye = False # start state
qutz = True #end state
hor = False #horizontal move
ver = False #vertical move
move = False #one move
#score
score = 0
#message function
def mess(mes,color,wid,hig):
    txt1 = font.render(mes,True,color)
    display.blit(txt1 , [wid,hig])
#snake function
def snake(b,snakelist):
    for i in snakelist:
        display.fill(red , rect = [i[0] , i[1] , b ,b ] )

while not bye:
    display.fill(yellow)#fill background
    for event in pygame.event.get():
        #quit handling x
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #movement handling 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ver == False and move  == False:
                ych = -b
                xch = 0
                ver = True
                hor = False
                move = True
            if event.key == pygame.K_s and ver == False and move == False:
                ych = b
                xch = 0
                ver = True
                hor = False
                move = True
            if event.key == pygame.K_d and hor == False and move == False:
                xch = b
                ych = 0
                hor = True
                ver = False
                move = True
            if event.key == pygame.K_a and hor == False and move == False:
                xch = -b
                ych = 0
                hor = True
                ver = False
                move = True
    #movment iniit
    xpos += xch
    ypos += ych
    #draw snake and apple
    snakehead = [] #list containing cordinates for head
    snakehead.append(xpos)
    snakehead.append(ypos)
    snakelist.append(snakehead) #list containing snakehaeds
    snake(b,snakelist) #snake
    display.fill(black , rect = [wa,ha,thick,thick]) #apple
    pygame.display.update()
    #apple snake collision
    if xpos == wa and ypos == ha:
        lenth += 5
        wa = random.randrange(1, w/10) * 10
        ha = random.randrange(1 , h/10) * 10
        score = score + 1
    # lenth conditoin for snake (needs to take place before snake eating himself - reason unkown) 
    if len(snakelist) > lenth:
            del snakelist [0]
    #snake boundaries
    if xpos == w - 10 or xpos == 0 or ypos == h - 10 or ypos == 0:
        display.fill(black)
        mess("You hit a wall your dead!",red,w/2-100,h/2 - 100)
        mess("You ate "+str(score)+" apples!",red,w/2 - 100, h/2)
        pygame.display.update()
        bye = True
        qutz = False 
        break 
    #snake eating himself
    for segm in snakelist [:-1]:
            if segm == snakehead:
                display.fill(white)
                pygame.display.update()
                xch = 0
                ych = 0
                display.fill(black)
                mess("You ate yourself!",red,w/2 - 100, h/2 - 100)
                mess("You ate "+str(score)+" apples!",red,w/2 - 100, h/2)
                pygame.display.update()
                bye = True
                qutz = False
                break
    #fps init
    time.tick(FPS)
    move = False 
#end handling
while not qutz:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
