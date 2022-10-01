git remote add origin https://github.com/pierrsik/pgame-and-tkinter.git
git branch -M main
git push -u origin main
import pygame
from sys import exit
pygame.init()
fps=pygame.time.Clock()
screen=pygame.display.set_mode((1200,720))
surface= pygame.image.load("C:/Users/Admin/Desktop/2203_w026_n002_1490b_p1_1490.jpg").convert()
background = pygame.transform.scale(surface, (1024*1.2, 1024 * .8))
pygame.display.set_caption('hacko_project')
test_font=pygame.font.Font(None,80)
bulletimg= pygame.image.load("transbullet.png").convert()
bullet = pygame.transform.scale(bulletimg, (30*1, 60* .4))
bullet.set_colorkey("black")
opentime = 0
surface1=test_font.render("welcome to your quest",False,('white'))
    
quick_shot= pygame.image.load("C:/Users/Admin/Desktop/spreadsheet.png").convert_alpha()
question=['what is the HCF of 84 and 90?','if X+Y+Z=XYZ find X,Y,Z','what is the unit digit of 6*36*216','value os 2*4*8*16',]
op1=['6','4,1,1','2','128',]
op2=['7','1,2,3','1','256',]
op3= ['22','2,2,2','6','512']
op4=['3','1,3,1','8','1024',]
anskey=[0,1,2,3]
    
def get_sprite(sheet,frame,width,height,scale,color):
    image=pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0),((frame*width),0,width,height))
    image= pygame.transform.scale(image,(width*1,height*1))
    image.set_colorkey(color)
    return image
animation_list=[]
steps=5
cooldown=100
last_up=pygame.time.get_ticks()
def bulletgo(imageb,dist,pos):
    current_pos= pos
    if current_pos<dist:
            screen.blit(imageb,(current_pos,585))
    pos+=10
        
    
for x in range(0,steps):
    animation_list.append(get_sprite(quick_shot,x,100,143,4,'black'))
frame=0

#text box 1
imgt1= pygame.image.load("TEXT1.png").convert()
imgt1f = pygame.transform.scale(imgt1, (30*20, 60* 4))
imgt1f.set_colorkey("black")
#test box 2
imgt2= pygame.image.load("TEXT2.png").convert()
imgt2f = pygame.transform.scale(imgt2, (30*20, 60* 4))
imgt2f.set_colorkey("black")
#test box 3
imgt3= pygame.image.load("TEXT3.png").convert()
imgt3f = pygame.transform.scale(imgt3, (30*20, 60* 4))
imgt3f.set_colorkey("black")
#ghost
ghostp= pygame.image.load("ghost.png").convert()
ghost = pygame.transform.scale(ghostp, (30*10, 60* 4))
ghost.set_colorkey("black")
#travveler
travellerp= pygame.image.load("traveller.png").convert()
traveller = pygame.transform.scale(travellerp, (30*9, 60* 3.5))
traveller.set_colorkey("black")





x=0
while True:
    i=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    screen.blit(surface1,(225,40))
    if i<4:
        test_font=pygame.font.Font(None,35)
        surfaceq=test_font.render(question[i],False,('white'))
        surfaceo1=test_font.render(op1[i],False,('white'))
        surfaceo2=test_font.render(op2[i],False,('white'))
        surfaceo3=test_font.render(op3[i],False,('white'))
        surfaceo4=test_font.render(op4[i],False,('white'))
        #screen.blit(surfaceq,(200,220))
        # screen.blit(surfaceo1,(200,260))
        #screen.blit(surfaceo2,(200,300))
        #screen.blit(surfaceo3,(200,340))
        #screen.blit(surfaceo4,(200,380))
        
   # i+=1
    #c_time = pygame.time.get_ticks()



    #screen.blit(animation_list[frame],(145,440))

    screen.blit(ghost,(145,400))
    screen.blit(traveller,(800,400))
    if x<= 500:
        screen.blit(imgt1f,(95,250))
        x+=1
    elif x<=1000:
        screen.blit(imgt2f,(550,310))
        x+=1
    elif x<=1500:
        screen.blit(imgt3f,(95,300))
        x+=1
    else:
        pygame.quit()
        exit()
    pygame.display.update()
    fps.tick(60)
