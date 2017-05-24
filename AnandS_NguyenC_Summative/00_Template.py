""" 
A basic template for starting to program in Pygame
"""

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
pygame.display.set_caption("Yeah, Hello There!")
spaceship1 = pygame.image.load("Spaceship1.png").convert_alpha()
background = pygame.image.load("Background.png").convert()

#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the display
x = 0
y = 400

#The game loop
clock = pygame.time.Clock() #<-- used to control the frame rate
keepGoing = True 	    #<-- a 'flag' variable for the game loop condition

try:
    while keepGoing:
        clock.tick(60) #<-- Set a constant frame rate, argument is frames per second
        screen.blit(background, (-1, -1))
        screen.blit(spaceship1, (x, y))
        #Handle any events in the current frame
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: #<-- this special event type happens when the window is closed
                keepGoing = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT and x > 0:
                    x -= 3
                if ev.key == pygame.K_RIGHT and x + 70 < 640:
                    x += 3
        pygame.display.flip()
finally:
    pygame.quit()  # Kseep this IDLE friendly 
