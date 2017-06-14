
#Import & initialize the pygame module
import pygame
import random

#pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for events. #It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP
from pygame.locals import *  
# better use pygame.MOUSEMOTION


#This will allow us to name the colours to use rather than give a name  eg (255,0,0)
from pygame.color import THECOLORS
#c=(255,0,0) instead of THECOLORS['red']????


# initial library itself
pygame.init()  

#Just like python, we will use os and time????
import os, time

#this code is necessary for python to work on tdsb computers????
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Set-up the main screen display window and caption  in the 
size = (640,480)  
screen = pygame.display.set_mode(size)

pygame.font.init()
font_path = "PixelSplitter-Bold.ttf"
font_size = 25
fontObj = pygame.font.Font(font_path, font_size)

#Puts a caption in the bar at the top of the window
pygame.display.set_caption("SPACE INVADERS")
spaceship1 = pygame.image.load("Spaceship1.png").convert_alpha()
background = pygame.image.load("Background.png").convert()
enemy1 = pygame.image.load("enemy1.png").convert_alpha()
enemy2 = pygame.image.load("enemy2.png").convert_alpha()
enemy3 = pygame.image.load("enemy3.png").convert_alpha()
ufo = pygame.image.load("UFO.png").convert_alpha()
laser1 = pygame.image.load("GreenLaser.png").convert_alpha() #Friendly laser
laser2 = pygame.image.load("RedLaser.png").convert_alpha() #Enemy Laser

lasersfx = pygame.mixer.Sound('laser.wav')
bkgmusic = pygame.mixer.Sound('heartofeternity.wav')

ast=pygame.image.load("newast.png").convert_alpha()
ast1=pygame.image.load("newast1.png").convert_alpha()
ast2=pygame.image.load("newast2.png").convert_alpha()
ast3=pygame.image.load("newast3.png").convert_alpha()

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 20)

x = 0
y = 420
direction=4
esizex = 28
esizey = 23
lsizex = 7
lsizey = 16
score = 0
laserx = []
lasery = []
lstatus = []
exbase = 10
estatus=[]
efront = []
row=5
column=10
ex=[]
ey=[]
etype = []
times=5
edirect = "right"
count = 0
countmax = 50
down = "no"
prevdir = "right"
lcount = 30
ufox = -51
ufoy = 10
ufostatus = "despawned"
level = 1
bodycount = 0
respawn = "no"
elaserx = []
elasery = []
pause = False 

#Create the lists with the coordinates and stuff
for each in range(times):
    a=0
    for each in range(column):
        exx=exbase+a
        ex.append(exx)
        a+=56

for e in range(column):
    row1=250
    ey.append(row1)
for e in range(column):
    row2=200
    ey.append(row2)
for e in range(column):
    row3=150
    ey.append(row3)
for e in range(column):
    row4=100
    ey.append(row4)
for e in range(column):
    row5=50
    ey.append(row5)

for e in ex:
    estatus.append('alive')

for e in range(20):
    etype.append(1)
for e in range(20):
    etype.append(2)
for e in range(10):
    etype.append(3)

for e in range(10):
    efront.append("yes")
for e in range(40):
    efront.append("no")

        
#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

bkgmusic.play(-1)

unpausetext = fontObj.render(("Press U to Unpause"), True, (255, 255, 255))
quittext = fontObj.render(("Press Q to Quit"), True, (255, 255, 255))
menutext = fontObj.render(("Press M to return to the Menu"), True, (255, 255, 255))


try:
    while keepGoing:
    
        
            
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second
        if not pause:
         
            
            scoretext = font.render(("Score: " + str(score)), True, (255, 255, 255))
            leveltext = font.render(("Level " + str(level)), True, (255, 255, 255))
            livestext = font.render(("Lives: "), True, (255, 255, 255))

            screen.blit(background, (-1, -1))
            screen.blit(spaceship1, (x, y))
            screen.blit(ast, (20, 350))
            
            if count >= countmax:
                count = 0
            count += 1 

            if lcount < 30:
                lcount += 1

            #Making the enemies shoot at random times
            maximumy = 0
            efront = []
            for i in range(len(estatus)):
                efront.append("no")
            for i in range(len(estatus)):
                eylist = []
                jlist = []
                listmax = 0
                listmin = 0
                front = ""
                if estatus[i] == "alive":
                      if ey[i] >= maximumy:
                          maximumy = ey[i]
            for i in range(len(estatus)):
                if estatus[i] == "alive":
                    if ey[i]== maximumy:
                        efront[i] = "yes"
                
                        
            for i in range(len(estatus)):
                if estatus == "alive" and efront[i] == "yes":
                    firechance = random.randint(1, 100)
                    if firechance >= 50:
                        print(len(ex))
                        elaserx.append(ex[i]+23)
                        elasery.append(ex[i]+5)
                    
            for i in range(len(elaserx)):
                screen.blit(laser2, (ex[i], ey[i]))

     
        

            
           #Spawning the UFO for bonus points
            #ufospawn = random.randint(1, 100)
    ##        ufospawn = 77
    ##        if ufospawn == 77 and ufostatus == "despawned":
    ##            ufostatus = "spawned"
    ##        if ufostatus == "spawned":
            screen.blit(ufo, (ufox, ufoy))
            ufox += 1
            if ufox > 650:
    ##            ufostatus = "despawned"
                ufox = -51
                ufoy = 10



            #A E S T H E T I C
            if respawn == "yes":
                time.sleep(0.5)
                for e in range(20):
                    screen.blit(enemy1, (ex[e], ey[e]))
                    pygame.display.flip()
                time.sleep(0.1)
                for e in range(20, 40):
                    screen.blit(enemy2, (ex[e], ey[e]))
                    pygame.display.flip()
                time.sleep(0.1)
                for e in range(40, 50):
                    screen.blit(enemy3, (ex[e], ey[e]))
                    pygame.display.flip()
                time.sleep(0.1)
                respawn = "no"


            for i in range(20):
                if estatus[i] == "alive":
                    screen.blit(enemy1, (ex[i], ey[i]))
            for i in range(20, 40):
                if estatus[i] == "alive":
                    screen.blit(enemy2, (ex[i], ey[i]))
            for i in range(40, 50):
                if estatus[i] == "alive":
                    screen.blit(enemy3, (ex[i], ey[i]))

            #Check if a laser hits an enemy
            for i in range(len(ex)):
                bodycount = 0
                for j in range(len(laserx)):
                    if laserx[j] + 3.5 >= ex[i] and laserx[j] + 3.5 <= ex[i] + esizex and (lasery[j] <= ey[i] + esizey and lasery[j] >= ey[i]) and lstatus[j] == "active" and estatus[i] == "alive":
                        estatus[i] = "dead"
                        lstatus[j] = "inactive"
                        countmax -= 1

                        if etype[i] == 1:
                            score += 10
                        elif etype[i] == 2:
                            score += 20
                        elif etype[i] == 3:
                            score += 40
                            
            bodycount = 0
            for i in estatus:
                if i == "dead":
                    bodycount += 1
                    
            #reset variables after a level
            if bodycount >= 50:
                level += 1
                ex = []
                ey = []
                estatus = []
                countmax = 50
                edirect = "right"
                prevdir = "right"
                lstatus = []
                laserx = []
                lasery = []
                for each in range(times):
                    a=0
                    for each in range(column):
                        exx=exbase+a
                        ex.append(exx)
                        a+=56
                
                for e in range(column):
                    row1=250
                    ey.append(row1)
                for e in range(column):
                    row2=200
                    ey.append(row2)
                for e in range(column):
                    row3=150
                    ey.append(row3)
                for e in range(column):
                    row4=100
                    ey.append(row4)
                for e in range(column):
                    row5=50
                    ey.append(row5)

                for e in ex:
                    estatus.append('alive')
                respawn = "yes"
                
            #laser coordinates
            for i in range(len(laserx)):
                #Move the lasers
                if lstatus[i] == 'active':
                    screen.blit(laser1, (laserx[i], lasery[i]))
                lasery[i] -= 4

                #Delete the lasers from the list
                if lasery[i] >= 1000:
                    del lasery[i-1]
                    del laserx[i-1]
                    del lstatus[i-1]
                
                    lasery.pop(lasery[i])
                    laserx.pop(laserx[i])
                    lstatus.pop(lstatus[i])
                    #Neither of these work lmao

            #move the ship
            if direction==1 and x > 0:
                x=x-2.5
            elif direction==2 and x+31<640:
                x=x+2.5

            #Move the Enemies
            if count>=countmax:
    ##            moveenemies(edirect)
                
                if edirect == "down" and prevdir != "down":
                    for ind in range(len(ex)):
                        ey[ind] += 15
                    prevdir = edirect
                        
                elif edirect == "right":
                    for ind in range(len(ex)):
                        ex[ind] += 4.5
                    prevdir = edirect
                    
                elif edirect == "left":
                    for ind in range(len(ex)):
                        ex[ind] -= 4.5
                    prevdir = edirect
                    
                for e in range(len(estatus)):
                    if estatus[e] == "alive":
                        if ex[e] + 28 >= 630 and prevdir != "down":
                            edirect = "down"
                            break
                        elif ex[e] + 28 >= 630 and prevdir == "down":
                            edirect = "left"
                            break
                            
                        elif ex[e] <= 10 and prevdir != "down":
                            edirect = "down"
                            break
                        elif ex[e] <= 10 and prevdir == "down":
                            edirect = "right"
                            break

            #Score Bar
            pygame.draw.rect(screen, THECOLORS["black"], (0, 450, 640, 30))
            screen.blit(scoretext, (10, 450))
            screen.blit(leveltext, (200, 450))
            screen.blit(livestext, (300, 450))
            
                
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                    keepGoing = False
                if ev.type == pygame.KEYDOWN: #Key Presses
                    if ev.key == K_LEFT:    #  left is pressed
                        direction=1
                    if ev.key == K_RIGHT:   # right is pressed
                        direction=2
                    if ev.key == K_SPACE and lcount == 30:
                        laserx.append(x + 11.5)
                        lasery.append(y - 12.5)
                        lasersfx.play()
                        lstatus.append('active')
                        lcount = 0
                    if ev.key == K_p:
                        pause = True
                   
                elif ev.type == KEYUP: #When you let go of the key, to stop it and not interfere with other keys
                    if direction == 1:
                        if ev.key == K_LEFT:
                            direction = 4
                    if direction == 2:
                        if ev.key == K_RIGHT:
                            direction = 4
        else:
            screen.blit(unpausetext, (150, 150))
            screen.blit(menutext, (150, 225))
            screen.blit(quittext, (150, 300))
            
            
            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN: 
                    if ev.key == K_u:
                        pause = False
                    if ev.key == K_m:
                        state="menu"
                        print("menu")
                    if ev.key == K_q:
                        pygame.quit()

        pygame.display.flip()
finally:
    pygame.quit()  # Keep this IDLE friendly 
