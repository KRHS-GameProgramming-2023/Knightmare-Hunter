import pygame, sys, math

class Wall ():
    def __init__(self, pos=[250, 250]):
        self.image = pygame.image.load("images/tiles/Wall.png")
        self.rect = self.image.get_rect(center = pos)
        
        self.kind = "wall"
        
    def update (self, size):
        pass
