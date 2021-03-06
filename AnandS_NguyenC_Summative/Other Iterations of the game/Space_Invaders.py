#Shashank Anand and Candace Nguyen
#June 14 2017
#SPACE INVADERS! - Summative
#ICS 2O1
#Ms. Strelkovska

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


ast1=pygame.image.load("newast.png").convert_alpha()
ast2=pygame.image.load("newast1.png").convert_alpha()
ast3=pygame.image.load("newast2.png").convert_alpha()
ast4=pygame.image.load("newast3.png").convert_alpha()

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
elstatus = []
listreset = "no"
asthp1 = 12
asthp2 = 12
asthp3 = 12
asthp4 = 12
shootmax = 998
lives = 3
immune = "no"


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

try:
    while keepGoing:
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second

        scoretext = font.render(("Score: " + str(score)), True, (255, 255, 255))
        leveltext = font.render(("Level " + str(level)), True, (255, 255, 255))
        livestext = font.render(("Lives: "), True, (255, 255, 255))

        screen.blit(background, (-1, -1))
        screen.blit(spaceship1, (x, y))

        #Blit the asteroids
        if asthp1 >= 10:
            screen.blit(ast1, (20, 330))
        elif asthp1 >=7 and asthp1 <= 9:
            screen.blit(ast2, (20, 330))
        elif asthp1 >= 4 and asthp1 <= 6:
            screen.blit(ast3, (20, 330))
        elif asthp1 >= 1 and asthp1 <= 3:
            screen.blit(ast4, (20, 330))

        if asthp2 >= 10:
            screen.blit(ast1, (198, 330))
        elif asthp2 >=7 and asthp2 <= 9:
            screen.blit(ast2, (198, 330))
        elif asthp2 >= 4 and asthp2 <= 6:
            screen.blit(ast3, (198, 330))
        elif asthp2 >= 1 and asthp2 <= 3:
            screen.blit(ast4, (198, 330))

        if asthp3 >= 10:
            screen.blit(ast1, (374, 330))
        elif asthp3 >=7 and asthp3 <= 9:
            screen.blit(ast2, (374, 330))
        elif asthp3 >= 4 and asthp3 <= 6:
            screen.blit(ast3, (374, 330))
        elif asthp3 >= 1 and asthp3 <= 3:
            screen.blit(ast4, (374, 330))

        if asthp4 >= 10:
            screen.blit(ast1, (536, 330))
        elif asthp4 >=7 and asthp4 <= 9:
            screen.blit(ast2, (536, 330))
        elif asthp4 >= 4 and asthp4 <= 6:
            screen.blit(ast3, (536, 330))
        elif asthp4 >= 1 and asthp4 <= 3:
            screen.blit(ast4, (536, 330))

        
        if count >= countmax:
            count = 0
        count += 1 

        if lcount < 30:
            lcount += 1

        #Making the enemies shoot at random times
        if listreset == "yes":
            listreset = "no"
            shootingx = 0
            shootingy = 0
            efront = []

            #Determining who will shoot the laser
            for i in range(len(estatus)):
                efront.append("no")
            #for i in range(10):
            maximumy = 0
            front = []
            for i in range(10):
                for j in range(i, 50, 10):
                    if estatus[j] == "alive":
                        front.append(j)
                        break
                    
            for i in front:
                efront[i] = "yes"

        #Actually shooting the laser                
        for i in range(len(estatus)):
            if estatus[i] == "alive" and efront[i] == "yes":
                firechance = random.randint(1, 1000)
                if firechance >= shootmax:
                    elaserx.append(ex[i]+11)
                    elasery.append(ey[i]+7)
                    elstatus.append("active")
                
        for i in range(len(elaserx)):
            if elstatus[i] == "active":
                screen.blit(laser2, (elaserx[i], elasery[i]))
            elasery[i] += 2
        
       #Spawning the UFO for bonus points
        ufospawn = random.randint(1, 100)
        ufospawn = 77
        if ufospawn == 77 and ufostatus == "despawned":
            ufostatus = "spawned"
        if ufostatus == "spawned":
            screen.blit(ufo, (ufox, ufoy))
        ufox += 1
        if ufox > 650:
            ufostatus = "despawned"
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

        #Draw the enemies
        for i in range(20):
            if estatus[i] == "alive":
                screen.blit(enemy1, (ex[i], ey[i]))
        for i in range(20, 40):
            if estatus[i] == "alive":
                screen.blit(enemy2, (ex[i], ey[i]))
        for i in range(40, 50):
            if estatus[i] == "alive":
                screen.blit(enemy3, (ex[i], ey[i]))

        #Check if friendly laser hits an enemy
        for i in range(len(ex)):
            for j in range(len(laserx)):
                if laserx[j] + 3.5 >= ex[i] and laserx[j] + 3.5 <= ex[i] + esizex and (lasery[j] <= ey[i] + esizey and lasery[j] >= ey[i]) and lstatus[j] == "active" and estatus[i] == "alive":
                    estatus[i] = "dead"
                    lstatus[j] = "inactive"
                    countmax -= 1
                    listreset = "yes"

                    if etype[i] == 1:
                        score += 10
                    elif etype[i] == 2:
                        score += 20
                    elif etype[i] == 3:
                        score += 40
##
##        for i in range(len(ex)):
##            if elaserx[i] + 3.5 >= 20 and elaserx[i] + 3.5 <= 105 and elasery[i] + 21 >= 330 and elasery[i] + 21 <= 407 and elstatus[i] == "active" and asthp1 > 0:
##                asthp1 -= 1
##                elstatus[i] = "inactive"

        #Check if enemy laser hits anything
        for i in range(len(elaserx)):
            #Check if it hits a player
            if elaserx[i] + 3.5 >= x and elaserx[i] + 3.5 <= x + 31 and (elasery[i] + 21 >= y and elasery[i] + 21 <= y + 25) and elstatus[i] == "active":
                lives -= 1
                pygame.draw.rect(screen, THECOLORS['blue'], (x, y, 30, 30))
                elstatus[i] = "inactive"

            #Check if it hits an asteroid
                
            #Asteroid 1
            if elaserx[i] + 3.5 >= 20 and elaserx[i] + 3.5 <= 105 and elasery[i] + 21 >= 330 and elasery[i] + 21 <= 407 and elstatus[i] == "active" and asthp1 > 0:
                asthp1 -= 1
                elstatus[i] = "inactive"

            #Asteroid 2
            if elaserx[i] + 3.5 >= 198 and elaserx[i] + 3.5 <= 283 and elasery[i] + 21 >= 330 and elasery[i] + 21 <= 407 and elstatus[i] == "active" and asthp2 > 0:
                asthp2 -= 1
                elstatus[i] = "inactive"

            #Asteroid 3
            if elaserx[i] + 3.5 >= 374 and elaserx[i] + 3.5 <= 459 and elasery[i] + 21 >= 330 and elasery[i] + 21 <= 407 and elstatus[i]== "active" and asthp3 > 0:
                asthp3 -= 1
                elstatus[i] = "inactive"

            #Asteroid 4
            if elaserx[i] + 3.5 >= 536 and elaserx[i] + 3.5 <= 621 and elasery[i] + 21 >= 330 and elasery[i] + 21 <= 407 and elstatus[i] == "active" and asthp4 > 0:
                asthp4 -= 1
                elstatus[i] = "inactive"



        #Check if everyone's dead                        
        bodycount = 0
        for i in estatus:
            if i == "dead":
                bodycount += 1
                
        #reset variables after a level
        if bodycount >= 50:
            level += 1
            shootmax -= 2
            ex = []
            ey = []
            estatus = []
            countmax = 50
            edirect = "right"
            prevdir = "right"
            lstatus = []
            laserx = []
            lasery = []
            asthp1 = 12
            asthp2 = 12
            asthp3 = 12
            asthp4 = 12
            x = 0
            
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

        if len(lasery) > 0:
            if lasery[-1] < -100:
                del lasery[-1]
                del laserx[-1]
                del lstatus[-1]

        if len(elasery) > 0:
            if elasery[-1] > 500:
                del elasery[-1]
                del elaserx[-1]
                del elstatus[-1]

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
                    lstatus.append('active')
                    lcount = 0
            
            elif ev.type == KEYUP: #When you let go of the key, to stop it and not interfere with other keys
                if direction == 1:
                    if ev.key == K_LEFT:
                        direction = 4
                if direction == 2:
                    if ev.key == K_RIGHT:
                        direction = 4


        pygame.display.flip()
finally:
    pygame.quit()  # Keep this IDLE friendly 
