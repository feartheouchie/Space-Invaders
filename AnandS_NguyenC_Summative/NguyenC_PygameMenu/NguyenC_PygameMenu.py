import pygame
import random
from pygame.locals import *  

from pygame.color import THECOLORS

pygame.init()  

import os, time

import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

size = (640,480)  
screen = pygame.display.set_mode(size) 

pygame.display.set_caption("Menu")

background = pygame.image.load("background\menu1.jpg").convert()
background2= pygame.image.load("background\menu2.jpg").convert()
background3= pygame.image.load("background\spaceback.png").convert_alpha()
background4= pygame.image.load("background\spaceback.png").convert_alpha()


pygame.display.flip() 

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition
# Set up the font and the size 

bigfont = pygame.font.SysFont("comic sans ms", 42)
smallfont=pygame.font.SysFont("verdana", 13)


##pygame.font.init()
##font_path = "elitedangerbold.ttf"
##font_size = 100
##fontObj = pygame.font.Font(font_path, font_size)

spaceship=pygame.image.load("spaceship1.png").convert_alpha()
mute=pygame.image.load("volume\mute.png").convert_alpha()
sound=pygame.image.load("volume\sound.png").convert_alpha()

##title = fontObj.render(('Space Invaders'), True, (255,255,255))
btnStart=pygame.image.load("start\startbutt1.png").convert_alpha()
btnInstruct=pygame.image.load("instru\instrubutt1.png").convert_alpha()
btnExit=pygame.image.load("exit\exit1.png").convert_alpha()
btnBack1=pygame.image.load("back\\back1.png").convert_alpha()

btnStart2=pygame.image.load("start\startbutt2.png").convert_alpha()
btnInstruct2=pygame.image.load("instru\instrubutt2.png").convert_alpha()
btnExit2=pygame.image.load("exit\exit2.png").convert_alpha()
btnBack2=pygame.image.load("back\\back2.png").convert_alpha()

state="menu"

try:
    while keepGoing:
        clock.tick(60)
        screen.blit(background, (0, 0))
        x=265
        y=200
        if state=="menu":

            a=pygame.mouse.get_pos()
        
            bn=screen.blit(btnStart,(x,y))    

        
            bi=screen.blit(btnInstruct,(x,y+50))    
        
            be=screen.blit(btnExit,(x,y+100))

            s=screen.blit(sound, (x, y))
            m=screen.blit(mute, (x+100, y))

            if bn.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart2, (x, y))
                bi=screen.blit(btnInstruct,(x,y+50))    
                be=screen.blit(btnExit,(x,y+100))
                
            if bi.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart, (x, y))
                bi=screen.blit(btnInstruct2,(x,y+50))    
                be=screen.blit(btnExit,(x,y+100))

            if be.collidepoint(a):
                screen.blit(background2, (0, 0))
                bn=screen.blit(btnStart, (x, y))
                bi=screen.blit(btnInstruct,(x,y+50))    
                be=screen.blit(btnExit2,(x,y+100))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bn.collidepoint(pos):
                        state="game"
                    elif bi.collidepoint(pos):
                        state="instructions"
                    elif be.collidepoint(pos):
                        keepGoing = False
            
        if state=="game":  
            # ---------------code for the game-------------------               
            screen.blit(background3, (0, 0))
            bb=screen.blit(btnBack1,(x+10,y+105))


            if bb.collidepoint(pygame.mouse.get_pos()):
               bb=screen.blit(btnBack2, (x+10, y+105))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(pos):
                        state="menu"

           
        if state=="instructions":
            screen.blit(background3, (0, 0))
            bb=screen.blit(btnBack1,(x+10,y+105))


            if bb.collidepoint(pygame.mouse.get_pos()):
               bb=screen.blit(btnBack2, (x+10, y+105))
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(pos):
                        state="menu"

                  
        pygame.display.flip()
              
                    

finally:
    pygame.quit()  # Keep this IDLE friendly 
