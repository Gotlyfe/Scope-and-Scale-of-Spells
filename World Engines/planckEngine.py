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
        self.x = x
        self.y = y
        self.energy = 1.0
        self.density = 1.0
        self.fitness = 1.0 / random.randint(1, 100)
        self.magic_color = random.randint(0x0,0xFF), random.randint(0x0,0xFF), random.randint(0x0,0xFF)
    
    def updateEnergy(self):
        self.energy = self.energy + self.fitness

    def updatePosition(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

        

class bloop():
    def __init__(self):
        self.energy = 20.0
        self.density = 0.5
        self.fitness = 1.0
        self.speed = 0, 0
        self.magic_color  = random.randint(0x0,0xFF), random.randint(0x0,0xFF), random.randint(0x0,0xFF)

    def die(self):
        print("oops, you died")

    def updateSpeed(self,x,y):
        self.speed = (self.speed[0] + x, self.speed[1] + y)
        self.updateEnergy(- self.fitness)

    def updateEnergy(self, amount):
        self.energy = self.energy + amount
        if self.energy <= 0:
            self.die()
            


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
maxNutrients = 1000
minNutrients = 10


#Player
player = bloop()
playerSpeed = 1

#effects
flicker = False


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
    if(len(nutrients) < maxNutrients):
        nutrients.append(qnutrient(random.randint(0,windowWidth), random.randint(0,windowHeight)))

    
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
                    player.updateSpeed(0, - playerSpeed)
                if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]):
                    player.updateSpeed(- playerSpeed, 0)
                if (pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]): 
                    player.updateSpeed(0, playerSpeed)
                if (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]):
                    player.updateSpeed(playerSpeed, 0)
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
    if(flicker):
        window.fill(black_color)
        flicker = False
    else:
        flicker = True

    for qn in nutrients:
        qn.updatePosition(- player.speed[0], - player.speed[1])
        if not (qn.y > windowHeight * 2 or qn.y < windowHeight * -2 or qn.x > windowWidth * 2 or qn.x < windowWidth * -2):
            pygame.draw.circle(window, qn.magic_color, (qn.x, qn.y), qn.energy)
        else:
            nutrients.remove(qn)

        pygame.draw.circle(window, player.magic_color, (windowWidth // 2, windowHeight // 2), player.energy)

    pygame.display.flip()
    """#
    #Post-Draw Phase
    #"""

    #variable clean up
    pygame.time.wait(40)