'''
Copyright 2018, Joshua Willman, All rights reserved
Red Huli Machine Learning

Basic Pygame sprite creation

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

# Constants 
WINDOWWIDTH = 500
WINDOWHEIGHT = 400
FPS = 30 

BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
    '''This class represents the player'''
    def __init__(self, width, height):
        '''call the base (Sprite) constructor class'''
        super().__init__()

        # Create the player with width, height and color attributes
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)

        # Draw the hero
        self.rect = self.image.get_rect()

# FPS to control screen updates
FPSCLOCK = pygame.time.Clock()

# create display surface
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('The Lone Character')

# List that contains all sprites in the game
active_sprites_list = pygame.sprite.Group()
        
# Spawn sprite and set x, y location
player = Player(30, 30)
player.rect.x = WINDOWWIDTH / 2 - player.rect.centerx
player.rect.y = 330

# Add the sprites to the list of objects
active_sprites_list.add(player)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Game logic goes here
    active_sprites_list.update()

    # Drawing code goes here
    DISPLAYSURF.fill(BLACK)
        
    # Draw sprites at once all/refresh the position of the player
    active_sprites_list.draw(DISPLAYSURF)

    pygame.display.update() # update screen
    FPSCLOCK.tick(FPS) # limit frames per second