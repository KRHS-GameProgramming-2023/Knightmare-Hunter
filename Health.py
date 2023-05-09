import pygame, sys, math

class Health():
    def __init__(self, pos=[50,50]):
        self.images = [pygame.image.load("Player/Images/Heathbarempty.png"),
                       pygame.image.load("Player/Images/Healthbar25%.png"),
                       pygame.image.load("Player/Images/Healthbar50%.png"),
                       pygame.image.load("Player/Images/Healthbar75%.png"),
                       pygame.image.load("Player/Images/Healthbar100%.png")]
        self.percent = 100;
        self.frame = self.calcFrame()
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, health):
        self.percent = health
        self.frame = self.calcFrame()
        self.image = self.images[self.frame]
        
    def calcFrame(self):
        if self.percent > 87:
            return len(self.images)-1
        elif self.percent > 62:
            return len(self.images)-2
        elif self.percent > 37:
            return len(self.images)-3
        elif self.percent > 12:
            return len(self.images)-4
        else:
            return 0
