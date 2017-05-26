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

background = pygame.image.load("bkg\menu1.jpg").convert()

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
btnNew=pygame.image.load("button1.gif").convert()
btnInstruct=pygame.image.load("button1.gif").convert()
btnExit=pygame.image.load("button1.gif").convert()
btnBack1=pygame.image.load("button1.gif").convert()

btnNew2=pygame.image.load("button3.gif").convert()
btnInstruct2=pygame.image.load("button3.gif").convert()
btnExit2=pygame.image.load("button3.gif").convert()
btnBack2=pygame.image.load("button3.gif").convert()

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
        x=300
        y=150
        if state=="menu":
##            screen.blit(title, (0, 0))
            bn=screen.blit(btnNew,(x,y))    #bn- rectangle arround button btnNew

            
            bi=screen.blit(btnInstruct,(x,y+100))    #bi- rectangle arround button btnInrtuct
            
            be=screen.blit(btnExit,(x,y+200))      #be- rectangle arround button btnExit
  
            screen.blit(spaceship, (x-300, y))
            screen.blit(newgame, (x+10, y+5))
            screen.blit(instructions, (x+10, y+105))
            screen.blit(exit1, (x+10, y+205))
            

            if bn.collidepoint(pygame.mouse.get_pos()):
               bn=screen.blit(btnNew2, (x, y))
               screen.blit(newgame, (x+10, y+5))

            if bi.collidepoint(pygame.mouse.get_pos()):
               bi=screen.blit(btnInstruct2, (x, y+100))
               screen.blit(instructions, (x+10, y+105))

            if be.collidepoint(pygame.mouse.get_pos()):
               be=screen.blit(btnExit2, (x, y+200))
               screen.blit(exit1, (x+10, y+205))

            
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
