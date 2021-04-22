"""
This is a simple enginge for testing soul - magic interfaces

"""
#import exit from system for closing the engine
from sys import exit as SystemExit

#import all of random
import random

#import all of pygame
import pygame




"""#
#Soul Definition Phase
definitions for any souls to be instantiated
#"""

#do not ask of the slug for it does not know
class Slug():
    functional_health = 2.0
    functional_energy = 8.0
    magic_color = 0x0, 0x0, 0x0 
    volume = 8.0
    mass = 8.0
    intent = ""

    def __init__(self, environmentFavorability):
        functional_health = 2.0 * environmentFavorability
        functional_energy = 8.0 * environmentFavorability
        volume = 8.0 * environmentFavorability
        mass = 8.0 * environmentFavorability
        magic_color = 0x0, 0x0, 0x0
        #intent = ""
        for color in magic_color:
            color = random.randint(0x0, 0xFF)
        if environmentFavorability > 1:
            intent = "-"
        elif environmentFavorability < 1:
            intent = "+"
    


"""#
#Instantiation Phase
All global variables created and initialized here
#"""

#Tuple object of window size ( width and height integet objects)
screenSize = screenWidth, screenHeight = 512, 512  
#Create surface object for displaying images
screen = pygame.display.set_mode(screenSize)
#Create image object for storing background image and rectangle of the same size
background_image = pygame.transform.scale(pygame.image.load("Assets/stars1.jpeg"), screenSize)
background_image_rect = pygame.Rect((0,0), screenSize)

#Color Palette
black_color = 0x0, 0x0, 0x0
white_color = 0xFF, 0xFF, 0xFF
blue_color = 0x1B, 0x9A, 0xAA
yellow_color = 0xF6, 0xFE, 0xAA
red_color = 0x94, 0x1C, 0x2F
green_color = 0x69, 0x7A, 0x21

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

    marcus = Slug(1)
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

    screen.fill(black_color)
    
    screen.blit(background_image, background_image_rect)

    pygame.display.flip()
    """#
    #Post-Draw Phase
    #"""

    #variable clean up