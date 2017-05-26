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

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display

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

##title = fontObj.render(('Space Invaders'), True, (255,255,255))
btnStart=pygame.image.load("start\startbutt1.png").convert_alpha()
btnInstruct=pygame.image.load("instru\instrubutt1.png").convert_alpha()
btnExit=pygame.image.load("exit\exit1.png").convert_alpha()
btnBack1=pygame.image.load("button1.gif").convert_alpha()

btnStart2=pygame.image.load("start\startbutt2.png").convert_alpha()
btnInstruct2=pygame.image.load("instru\instrubutt2.png").convert_alpha()
btnExit2=pygame.image.load("exit\exit2.png").convert_alpha()
btnBack2=pygame.image.load("button3.gif").convert_alpha()

newgame=smallfont.render(("New Game"), True, (0, 0, 0))
instructions=smallfont.render(("Instructions"), True, (0, 0, 0))
exit1=smallfont.render(("Exit"), True, (0, 0, 0))
back=smallfont.render(("Menu"), True, (0, 0, 0))

welcome = bigfont.render(('Welcome to Space Invaders!'), True, (255,255,255))
instruct = bigfont.render(('How to play:'), True, (255, 255, 255))

state="menu"

try:
    while keepGoing:
        clock.tick(60) #delay
        screen.blit(background, (0, 0))
        x=265
        y=200
        if state=="menu":
##            screen.blit(title, (0, 0))

            a=pygame.mouse.get_pos()
                
            bn=screen.blit(btnStart,(x,y))    #bn- rectangle arround button btnNew

            
            bi=screen.blit(btnInstruct,(x,y+50))    #bi- rectangle arround button btnInrtuct
            
            be=screen.blit(btnExit,(x,y+100))      #be- rectangle arround button btnExit
  
            screen.blit(spaceship, (x-300, y))
##            screen.blit(newgame, (x+10, y+5))
            screen.blit(instructions, (x+10, y+105))
            screen.blit(exit1, (x+10, y+205))
            

            if bn.collidepoint(a):
               bn=screen.blit(btnStart2, (x, y))
##               screen.blit(newgame, (x+10, y+5))

            if bi.collidepoint(a):
               bi=screen.blit(btnInstruct2, (x, y+50))
##               screen.blit(instructions, (x+10, y+105))

            if be.collidepoint(a):
               be=screen.blit(btnExit2, (x, y+100))
##               screen.blit(exit1, (x+10, y+205))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
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
            screen.blit(welcome, (20,50))   # print text welcome
            bb=screen.blit(btnBack1,(x+10,y+105))

            screen.blit(back, (x+20,y+110))

            if bb.collidepoint(pygame.mouse.get_pos()):
               bb=screen.blit(btnBack2, (x+10, y+105))
               screen.blit(back, (x+20, y+110))

            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                    keepGoing = False
                elif ev.type == MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if bb.collidepoint(pos):
                        state="menu"

           
        if state=="instructions":
            # ---------------code for the instructions-------------------
            screen.blit(instruct, (20,70))   # print text instructions
            bb=screen.blit(btnBack1,(x+10,y+105))

            screen.blit(back, (x+20, y+110))

            if bb.collidepoint(pygame.mouse.get_pos()):
               bb=screen.blit(btnBack2, (x+10, y+105))
               screen.blit(back, (x+20, y+110))
            
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
