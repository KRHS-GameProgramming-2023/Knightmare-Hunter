import pygame, sys, math

class Spawner ():
    def __init__(self, pos=[50, 25]):
        self.image = pygame.image.load("images/tiles/Spawner.png")
        self.rect = self.image.get_rect(center = pos)
        
        self.kind = "Spawner"
        
    def update(self, size):
        pass
        
