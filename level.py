import pygame
from settings import *
from player import Player

class Level :
    def __init__(self):
        # this is the same of surface of main.py
        # this allows the level to draw straight on the main display tha we are going to display to the player
        # makes organizing the entire thing
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        # this help us to draw and update any kind of sprite
        self.all_sprites = pygame.sprite.Group()
        
        self.setup()
    
    def setup(self) :
        self.player = Player((640, 360), self.all_sprites)
    
    def run(self, dt) :
        # we can run the entire game inside of it
        # which is helping considerabley to keep the entire clean and organized
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)