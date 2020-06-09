
#Shashank Anand and Candace Nguyen
#June 14 2017
#SPACE INVADERS! - Summative
#ICS 2O1
#Ms. Strelkovska

import pygame
import random
from pygame.locals import *  

from pygame.color import THECOLORS

pygame.init()
pygame.mixer.init()

import os, time

import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
size = (640,480)  
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SPACE INVADERS")

spaceship1 = pygame.image.load("Spaceship1.png").convert_alpha()
gamebackground = pygame.image.load("Background.png").convert()
background = pygame.image.load("background\menu1.jpg").convert()
background2= pygame.image.load("background\menu2.jpg").convert()
instructbkg1= pygame.image.load("instructbkg1.jpg").convert()
instructbkg2 = pygame.image.load("instructbkg2.jpg").convert()
enemy1 = pygame.image.load("enemy1.png").convert_alpha()
enemy2 = pygame.image.load("enemy2.png").convert_alpha()
enemy3 = pygame.image.load("enemy3.png").convert_alpha()
ufo = pygame.image.load("UFO.png").convert_alpha()
laser1 = pygame.image.load("GreenLaser.png").convert_alpha() #Friendly laser
laser2 = pygame.image.load("RedLaser.png").convert_alpha() #Enemy Laser

#enemies
orangeenemy=pygame.image.load("enemy1.png").convert_alpha()
blueenemy=pygame.image.load("enemy2.png").convert_alpha()
greenenemy=pygame.image.load("enemy3.png").convert_alpha()

#asteroids
ast1=pygame.image.load("newast.png").convert_alpha()
ast2=pygame.image.load("newast1.png").convert_alpha()
ast3=pygame.image.load("newast2.png").convert_alpha()
ast4=pygame.image.load("newast3.png").convert_alpha()

#sound
mute=pygame.image.load("volume\mute.png").convert_alpha()
sound=pygame.image.load("volume\sound.png").convert_alpha()
mute2=pygame.image.load("volume\mute2.png").convert_alpha()
sound2=pygame.image.load("volume\sound2.png").convert_alpha()

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

#fonts
pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 20)

pygame.font.init()
font_path = "PixelSplitter-Bold.ttf"
font_size = 10
font_size2 = 20
font_size3 = 50
fontObj = pygame.font.Font(font_path, font_size)
fontObj2 = pygame.font.Font(font_path, font_size2)
fontObj3 = pygame.font.Font(font_path, font_size3)

#text
credit = fontObj.render(('Credits'), True, (255,255,255))
credittext1 = fontObj.render(('Game Designer'), True, (255,255,255))
credittext2 = fontObj.render(('Software Engineer'), True, (255,255,255))
credittext11 = fontObj.render(('Candace Nguyen'), True, (255,255,255))
credittext22 = fontObj.render(('Shashank Anand'), True, (255,255,255))
musictext = fontObj.render(('Music'), True, (255,255,255))
musictextt = fontObj.render(('Heart of Eternity - Revolt Production'), True, (255,255,255))

enemies=fontObj2.render(('Enemies'), True, (255,255,255))
ufotext=fontObj2.render(('UFO'), True, (255,255,255))
asteroidtext=fontObj2.render(('Asteroids'), True, (255,255,255))
how2pause = fontObj2.render(("Press p to pause and go back to the menu"), True, (255, 255, 255))

gameovertext = fontObj3.render(("GAME OVER!"), True, (255, 255, 255))

instructionstext1 = fontObj.render(('Use arrow keys to move your spaceship'), True, (255,255,255))
instructionstext2 = fontObj.render(('Press spacebar to shoot'), True, (255,255,255))
instructionstext3 = fontObj.render(('Dodge lasers by hiding behind the asteroids'), True, (255,255,255))
instructionstext4 = fontObj.render(('Press P to Pause during the game'), True, (255,255,255))
instructionstext5 = fontObj.render(('You lose if you die or the enemies advance too far. Good Luck!'), True, (255,255,255))

hp=fontObj.render(('12 HP'), True, (0,245,46))
orange=fontObj.render(('10 pts'), True, (0,245,46))
blue=fontObj.render(('20 pts'), True, (0,245,46))
green=fontObj.render(('40 pts'), True, (0,245,46))
ufopts=fontObj.render(('??? pts'), True, (0,245,46))

#buttons
btnStart=pygame.image.load("start\startbutt1.png").convert_alpha()
btnInstruct=pygame.image.load("instru\instrubutt1.png").convert_alpha()
btnExit=pygame.image.load("exit\exit1.png").convert_alpha()
btnBack1=pygame.image.load("back\\back1.png").convert_alpha()

credit2 = fontObj.render(('Credits'), True, (0,245,46))
btnStart2=pygame.image.load("start\startbutt2.png").convert_alpha()
btnInstruct2=pygame.image.load("instru\instrubutt2.png").convert_alpha()
btnExit2=pygame.image.load("exit\exit2.png").convert_alpha()
btnBack2=pygame.image.load("back\\back2.png").convert_alpha()


#variables
state="menu"
volume="sound"
music = "start"

#blit sound
m=screen.blit(mute, (600, 450))
s=screen.blit(sound, (600, 450))
def blitsound():
    if volume=="sound":
        s=screen.blit(sound, (600, 450))
    if volume=="mute":
        m=screen.blit(mute, (600, 450))

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition
        
bkgmusic = pygame.mixer.Sound('heartofeternity.wav')
lasersfx = pygame.mixer.Sound('laser.wav')
        
try:
    while keepGoing:
        clock.tick(60)
        screen.blit(background, (0, 0))
        
        if state=="menu":
            blitsound()
                
            a=pygame.mouse.get_pos()
        
            bn=screen.blit(btnStart,(265,200))    
            bi=screen.blit(btnInstruct,(265,250))    
            be=screen.blit(btnExit,(265,300))

            c=screen.blit(credit, (25, 450))

            if bn.collidepoint(a):
                screen.blit(background2, (0, 0))
                blitsound()
                bn=screen.blit(btnStart2,(265,200))    
                bi=screen.blit(btnInstruct,(265,250))    
                be=screen.blit(btnExit,(265,300))
                screen.blit(credit, (25, 450))
                
            if bi.collidepoint(a):
                screen.blit(background2, (0, 0))
                blitsound()
                bn=screen.blit(btnStart,(265,200))    
                bi=screen.blit(btnInstruct2,(265,250))    
                be=screen.blit(btnExit,(265,300))
                screen.blit(credit, (25, 450))

            if be.collidepoint(a):
                screen.blit(background2, (0, 0))
                blitsound()
                bn=screen.blit(btnStart,(265,200))    
                bi=screen.blit(btnInstruct,(265,250))    
                be=screen.blit(btnExit2,(265,300))
                screen.blit(credit, (25, 450))

            if c.collidepoint(a):
                screen.blit(background2, (0, 0))
                blitsound()
                bn=screen.blit(btnStart,(265,200))    
                bi=screen.blit(btnInstruct,(265,250))    
                be=screen.blit(btnExit,(265,300))
                screen.blit(credit2, (25, 450))
                
            if s.collidepoint(a) and volume!="mute":
                screen.blit(sound2, (600, 450))

            if music == "start" and volume == "sound":
                bkgmusic.play(-1)
                music = "playing"
            elif volume == "mute":
                pygame.mixer.pause()
                music = "stopped"
                if m.collidepoint(a):
                    screen.blit(mute2, (600, 450))
            elif music == "stopped" and volume == "sound":
                pygame.mixer.unpause()
                music = "playing"
                if s.collidepoint(a):
                    screen.blit(sound2, (600, 450))
                
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    if bn.collidepoint(a):
                        state="game"
                        varreset = "yes"
                    elif bi.collidepoint(a):
                        state="instructions"
                    elif be.collidepoint(a):
                        keepGoing = False
                    elif c.collidepoint(a):
                        state="credits"
                    else:
                         if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"
    
        if state=="game":
            #Reset the game variables
            if varreset == "yes":
                varreset = "no"
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
                shootmax = 999
                lives = 3
                pause = False
                gameover = False

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
                
            if not pause:  
                
                scoretext = font.render(("Score: " + str(score)), True, (255, 255, 255))
                leveltext = font.render(("Level " + str(level)), True, (255, 255, 255))
                livestext = font.render(("Life: " + str(lives)), True, (255, 255, 255))
                unpausetext = fontObj.render(("Press U to Unpause"), True, (255, 255, 255))
                quittext = fontObj.render(("Press Q to Quit"), True, (255, 255, 255))
                menutext = fontObj.render(("Press M to return to the Menu"), True, (255, 255, 255))
                finalscore = fontObj2.render("Your final score was: " + str(score), True, (255, 255, 255))
                                              
                screen.blit(gamebackground, (-1, -1))
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
                ufospawn = random.randint(1, 500)
                if ufospawn == 77 and ufostatus == "despawned":
                    ufostatus = "spawned"
                if ufostatus == "spawned":
                    screen.blit(ufo, (ufox, ufoy))
                    ufox += 2
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

                #Check if friendly laser hits an asteroid
                
                #Asteroid 1
                for i in range(len(lstatus)):
                    if laserx[i] + 3.5 >= 20 and laserx[i] + 3.5 <= 105 and lasery[i] >= 330 and lasery[i] <= 407 and lstatus[i] == "active" and asthp1 > 0:
                        lstatus[i] = "inactive"
                        asthp1 -= 1
                #Asteroid 2
                for i in range(len(lstatus)):
                    if laserx[i] + 3.5 >= 198 and laserx[i] + 3.5 <= 283 and lasery[i] >= 330 and lasery[i] <= 407 and lstatus[i] == "active" and asthp2 > 0:
                        lstatus[i] = "inactive"
                        asthp2 -= 1
                #Asteroid 3
                for i in range(len(lstatus)):
                    if laserx[i] + 3.5 >= 374 and laserx[i] + 3.5 <= 459 and lasery[i] >= 330 and lasery[i] <= 407 and lstatus[i] == "active" and asthp3 > 0:
                        lstatus[i] = "inactive"
                        asthp3 -= 1
                #Asteroid 4
                for i in range(len(lstatus)):
                    if laserx[i] + 3.5 >= 536 and laserx[i] + 3.5 <= 621 and lasery[i] >= 330 and lasery[i] <= 407 and lstatus[i] == "active" and asthp4 > 0:
                        lstatus[i] = "inactive"
                        asthp4 -= 1

                #Check if friendly laser hits the UFO
                for i in range(len(lstatus)):
                    if laserx[i] + 3.5 >= ufox and laserx[i] + 3.5 <= ufox + 50 and lasery[i] <= ufoy + 19 and lasery[i] + 21 >= ufoy and lstatus[i] == "active" and ufostatus == "spawned":
                        lstatus[i] = "inactive"
                        ufostatus = "despawned"
                        score += random.choice([50, 100, 150])
                        ufox = -51
                        ufoy = 10


                #Check if enemy laser hits anything
                for i in range(len(elaserx)):
                    #Check if it hits a player
                    if elaserx[i] + 3.5 >= x and elaserx[i] + 3.5 <= x + 31 and (elasery[i] + 21 >= y and elasery[i] + 21 <= y + 25) and elstatus[i] == "active":
                        lives -= 1
                        #pygame.draw.rect(screen, THECOLORS['blue'], (x, y, 30, 30))
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

                #Game over conditions
                for i in range(len(ey)):
                    if estatus[i] != "dead" and ey[i] >= 325:
                        gameover = True
                if lives <= 0:
                    gameover = True

                if gameover == True:
                    pygame.draw.rect(screen, THECOLORS["black"], (-1, -1, 700, 700))
                    screen.blit(gameovertext, (170, 200))
                    screen.blit(how2pause, (80, 380))
                    screen.blit(finalscore, (80, 420)) 


                    
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
                            if volume != "mute":
                                lasersfx.play()
                            lstatus.append('active')
                            lcount = 0
                        if ev.key == K_p:
                            pause = True
                            gameover = False
                    
                    elif ev.type == KEYUP: #When you let go of the key, to stop it and not interfere with other keys
                        if direction == 1:
                            if ev.key == K_LEFT:
                                direction = 4
                        if direction == 2:
                            if ev.key == K_RIGHT:
                                direction = 4
            else:
                a=pygame.mouse.get_pos()
                screen.blit(unpausetext, (150, 200))
                screen.blit(menutext, (150, 250))
                screen.blit(quittext, (150, 300))

                blitsound()
                if s.collidepoint(a) and volume!="mute":
                    screen.blit(sound2, (600, 450))
                elif volume == "mute":
                    pygame.mixer.pause()
                    music = "stopped"
                    if m.collidepoint(a):
                        screen.blit(mute2, (600, 450))
                elif music == "stopped" and volume == "sound":
                    pygame.mixer.unpause()
                    music = "playing"
                    if s.collidepoint(a):
                        screen.blit(sound2, (600, 450))
                        
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN: 
                        if ev.key == K_u:
                            pause = False
                        if ev.key == K_m:
                            state="menu"
                            pause = False
                        if ev.key == K_q:
                            pygame.quit()
                    if ev.type == MOUSEBUTTONDOWN:
                        if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"

            pygame.display.flip()

            
        if state=="instructions":
            a=pygame.mouse.get_pos()
            screen.blit(instructbkg1, (0, 0))
            
            blitsound()

            screen.blit(instructionstext1, (100,175))
            screen.blit(instructionstext2, (100,200))
            screen.blit(instructionstext3, (100,225))
            screen.blit(instructionstext4, (100,250))
            screen.blit(instructionstext5, (100,275))
            
            screen.blit(orangeenemy, (425,350))
            screen.blit(blueenemy, (475,350))
            screen.blit(greenenemy, (525,350))

            screen.blit(orange, (425,375))
            screen.blit(blue, (475,375))
            screen.blit(green, (525,375))
            screen.blit(ufopts, (275,375))

            screen.blit(asteroidtext, (75,325))
            screen.blit(enemies, (425,325))
            screen.blit(ufotext, (275,325))

            screen.blit(spaceship1, (400, 175))
            screen.blit(ast1, (75, 350))
            screen.blit(ufo, (275, 350))

            screen.blit(hp, (125, 375))
            bb=screen.blit(btnBack1,(265,400))

            if bb.collidepoint(a):
                screen.blit(instructbkg2, (0, 0))

                blitsound()

                screen.blit(instructionstext1, (100,175))
                screen.blit(instructionstext2, (100,200))
                screen.blit(instructionstext3, (100,225))
                screen.blit(instructionstext4, (100,250))
                screen.blit(instructionstext5, (100,275))
                
                screen.blit(orangeenemy, (425,350))
                screen.blit(blueenemy, (475,350))
                screen.blit(greenenemy, (525,350))

                screen.blit(orange, (425,375))
                screen.blit(blue, (475,375))
                screen.blit(green, (525,375))
                screen.blit(ufopts, (275,375))

                screen.blit(asteroidtext, (75,325))
                screen.blit(enemies, (425,325))
                screen.blit(ufotext, (275,325))

                screen.blit(spaceship1, (400, 175))
                screen.blit(ast1, (75, 350))
                screen.blit(ufo, (275, 350))

                screen.blit(hp, (125, 375))

                bb=screen.blit(btnBack2,(265,400))
                

            if s.collidepoint(a) and volume!="mute":
                screen.blit(sound2, (600, 450))

            elif volume == "mute":
                pygame.mixer.pause()
                music = "stopped"
                if m.collidepoint(a):
                    screen.blit(mute2, (600, 450))
            elif music == "stopped" and volume == "sound":
                pygame.mixer.unpause()
                music = "playing"
                if s.collidepoint(a):
                    screen.blit(sound2, (600, 450))
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    if bb.collidepoint(a):
                        state="menu"
                    else:
                        if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"

        if state=="credits":
            a=pygame.mouse.get_pos()
                
            screen.blit(background, (0, 0))
        
            if volume=="sound":
                s=screen.blit(sound, (600, 450))

            if volume=="mute":
                m=screen.blit(mute, (600, 450))
                
            screen.blit(credittext1, (100,175))
            screen.blit(credittext2, (100,200))
            screen.blit(musictext, (100,225))
            
            screen.blit(credittext11, (400,175))
            screen.blit(credittext22, (400,200))
            screen.blit(musictextt, (400,225))
            
            bb=screen.blit(btnBack1,(265,400))

            if bb.collidepoint(a):
                screen.blit(background2, (0, 0))
                blitsound()
                bb=screen.blit(btnBack2,(265,400))
                screen.blit(credittext1, (100,175))
                screen.blit(credittext2, (100,200))
                screen.blit(musictext, (100,225))
                
                screen.blit(credittext11, (400,175))
                screen.blit(credittext22, (400,200))
                screen.blit(musictextt, (400,225))
                
            if s.collidepoint(a) and volume!="mute":
                screen.blit(sound2, (600, 450))

            elif volume == "mute":
                pygame.mixer.pause()
                music = "stopped"
                if m.collidepoint(a):
                    screen.blit(mute2, (600, 450))
            elif music == "stopped" and volume == "sound":
                pygame.mixer.unpause()
                music = "playing"
                if s.collidepoint(a):
                    screen.blit(sound2, (600, 450))
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: 
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(a):
                        state="menu"
                    else:
                         if m.collidepoint(a) or s.collidepoint(a):
                            if volume=="sound":
                                volume="mute"
                            else:
                                volume="sound"

                  
        pygame.display.flip()
              
finally:
    pygame.quit()  
      
