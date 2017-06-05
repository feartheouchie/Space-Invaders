
#Import & initialize the pygame module
import pygame

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
laser1 = pygame.image.load("GreenLaser.png").convert_alpha() #Friendly laser
laser2 = pygame.image.load("RedLaser.png").convert_alpha() #Enemy Laser


ast=pygame.image.load("asteroid.png").convert_alpha()
ast1=pygame.image.load("asteroid1.png").convert_alpha()
ast2=pygame.image.load("asteroid2.png").convert_alpha()
ast3=pygame.image.load("asteroid3.png").convert_alpha()

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display
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
row=5
column=10
ex=[]
ey=[]
times=5
edirect = "right"
count = 0
countmax = 50
down = "no"

for each in range(times):
    a=0
    for each in range(column):
        exx=exbase+a
        ex.append(exx)
        a+=56
        
for x in range(column):
    row1=250
    ey.append(row1)
for x in range(column):
    row2=200
    ey.append(row2)
for x in range(column):
    row3=150
    ey.append(row3)
for x in range(column):
    row4=100
    ey.append(row4)
for x in range(column):
    row5=50
    ey.append(row5)

for x in ex:
    estatus.append('alive')

##def moveenemies(edirect):
##    global ex, ey, exbase, estatus
##    down = "no"
##    
##    if down == "yes":
##        for ind in range(len(ex)):
##            ey[ind] += 23
##
##        down = "no"
##
##    elif edirect == "right":
##        for ind in range(len(ex)):
##            ex[ind] += 4.5
##    elif edirect == "left":
##        for ind in range(len(ex)):
##            ex[ind] -= 4.5
##                    
##    for e in range(len(estatus)):
##        if estatus[e] == "alive":
##            if ex[e] + 28 >= 630:
##                down="yes"
##                edirect = "left"
##                break
##            elif ex[e] <= 10:
##                down="yes"
##                edirect = "right"
##                break
##
##            
##    '''if switched == "yes" and edirect == "right":
##        edirect = "left"
##        for e in range(len(estatus)):
##            for e in range(len(ey)):
##                if estatus[e] == "alive":
##                    #ey[e] += 23'''
##                    
##    '''if switched == "yes" and edirect == "left":
##        edirect = "right"
##
##        for e in range(len(estatus)):
##            for e in range(len(ey)):
##                if estatus[e] == "alive":
##                    #ey[e] += 23
##           '''         
        
                
                        
        

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

try:
    while keepGoing:
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second
        if count == countmax:
            count = 0
        count += 1
        screen.blit(background, (-1, -1))
        screen.blit(spaceship1, (x, y))
        screen.blit(ast, (20, 350))

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
            for j in range(len(laserx)):
                if laserx[j] + 3.5 >= ex[i] and laserx[j] + 3.5 <= ex[i] + esizex and (lasery[j] <= ey[i] + esizey and lasery[j] >= ey[i]) and lstatus[j] == "active" and estatus[i] == "alive":
                    estatus[i] = "dead"
                    lstatus[j] = "inactive"
                    countmax -= 1
                    #lstatus

        #laser coordinates
        for i in range(len(laserx)):
            if lstatus[i] == 'active':
                screen.blit(laser1, (laserx[i], lasery[i]))
            lasery[i] -= 2
            #Maybe later find a way to remove things after the laser gets far from the screen to save some space, possibly use [-1]
       
        #move the ship
        if direction==1 and x > 0:
            x=x-2.5
        elif direction==2 and x+55<640:
            x=x+2.5
        
        if count==countmax:
##            moveenemies(edirect)
            ##    down = "no"
    
            if down == "yes":
                for ind in range(len(ex)):
                    ey[ind] += 23

                down = "no"

            elif edirect == "right":
                for ind in range(len(ex)):
                    ex[ind] += 4.5
            elif edirect == "left":
                for ind in range(len(ex)):
                    ex[ind] -= 4.5
                            
            for e in range(len(estatus)):
                if estatus[e] == "alive":
                    if ex[e] + 28 >= 630:
                        down="yes"
                        edirect = "left"
                        break
                    elif ex[e] <= 10:
                        down="yes"
                        edirect = "right"
                        break
            
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                keepGoing = False
            if ev.type == pygame.KEYDOWN: #Key Presses
                if ev.key == K_LEFT:    #  left is pressed
                    direction=1
                if ev.key == K_RIGHT:   # right is pressed
                    direction=2
                if ev.key == K_SPACE:
                    laserx.append(x + 23)
                    lasery.append(y - 15)
                    lstatus.append('active')
            
            elif ev.type == KEYUP: #When you let go of the key, to stop it and not interfere with other keys
                if direction == 1:
                    if ev.key == K_LEFT:
                        direction = 4
                if direction == 2:
                    if ev.key == K_RIGHT:
                        direction = 4

           
        pygame.display.flip()
finally:
    pygame.quit()  # Kseep this IDLE friendly 
