"""
This is a simple enginge for tiny soul - magic interfaces

"""
#import exit from system for closing the engine
from sys import exit as SystemExit

#import all of random
import random

#import all of math
import math

#import all of pygame
import pygame




"""#
#Soul Definition Phase
definitions for any souls to be instantiated
#"""

class qnutrient():
    def __init__(self,x,y):
        energy = 1.0
        fitness = 1.0 / randint()
        magic_color = randint(0x0,0xFF), randint(0x0,0xFF), randint(0x0,0xFF)
    
    update():
        energy = energy + fitness
        
        return true

class bloop():
    def

"""#
#Instantiation Phase
All global variables created and initialized here
#"""

#Tuple object of window size ( width and height integet objects)
windowSize = windowWidth, windowHeight = 512, 512  
#Create surface object for displaying images
window = pygame.display.set_mode(windowSize)

#Color Palette
black_color = 0x0, 0x0, 0x0
white_color = 0xFF, 0xFF, 0xFF
blue_color = 0x1B, 0x9A, 0xAA
yellow_color = 0xF6, 0xFE, 0xAA
red_color = 0x94, 0x1C, 0x2F
green_color = 0x69, 0x7A, 0x21

#QNutrients
nutrients = []
maxNutrients = 100
minNutrients = 10

"""#
#Pre-Calculative Phase
functions and methods
#"""

#functions

"""#
#Calculative Phase
#"""

#expressions

"""#
#Engine Loop Phase
#"""

while True:   
    """
    Each iteration of this while loop is comparable to a single moment of time.
    """ 

    """#
    #Initialization Phase
    all scope specific variables here
    #"""

    #instantiation

    """#
    #Pre-Event Phase
    #"""

    #code

    #

    """#
    #Event Phase
    All of the pygame events are handled
    #"""
    for event in pygame.event.get():    #   for each pygame event in the list of pygame events
        if event.type == pygame.QUIT:   #   in the case of the QUIT event
            SystemExit()
        if pygame.key.get_focused():
            if event.type == pygame.KEYDOWN:    #   Checking for keypress
                #   if game window is focused, touched the ground recently, and key is pressed, move amount
                if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]): 
                    pass
                if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]):
                    pass
                if (pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]): 
                    pass
                if (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]):
                    pass
            elif event.type == pygame.KEYUP:
                if (not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_w]): 
                    pass
                if (not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_a]):
                    pass
                if (not pygame.key.get_pressed()[pygame.K_DOWN] and not pygame.key.get_pressed()[pygame.K_s]): 
                    pass
                if (not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_d]):
                    pass
    
    """#
    #Post-Event Phase
    #"""

    #code

    """#
    #Pre-Draw Phase
    #"""

    #code

    """#
    #Draw Phase
    #"""
    window.fill(black_color)

    for qn in nutrients
        pygame.draw.circle(window, (0,0,0), (400, 300), 100, 5)


    pygame.display.flip()
    """#
    #Post-Draw Phase
    #"""

    #variable clean up