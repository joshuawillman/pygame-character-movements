'''
Copyright 2018, Joshua Willman, All rights reserved
Red Huli Machine Learning

Basic Pygame foundational code

GNU All-Permissive License - Version 1.0
Copying and distribution of this file, with or without modification, 
are permitted in any medium without royalty provided the copyright 
notice and this notice are preserved. This file is offered as-is, 
without any warranty.
'''

# import the necessary packages
import pygame, sys
from pygame import *

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 400

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Empty Screen')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()