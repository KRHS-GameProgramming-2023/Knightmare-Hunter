import pygame, sys, math

class Hud():
    def __init__(self, pos=[50,50]):
        self.images = [pygame.image.load("Player/images/Healthbarempty.png"),
                       pygame.image.load("Player/images/Healthbar25%.png"),
                       pygame.image.load("Player/images/Healthbar50%.png"),
                       pygame.image.load("Player/images/Healthbar75%.png"),
                       pygame.image.load("Player/images/Healthbar100%.png")
                       ]
        self.percent = 100;
        self.frame = self.calcFrame()
        self.image = self.images(self.frame)
        self.rect = self.image.get_rect(center = startPos)
        
    def __init__(self, baseText, startPos=[0,0]):
        self.font = pygame.font.Font(None, 48)
        self.baseText = baseText
        self.image = self.font.render("Kills: 0", True, (0, 0, 0))
        self.rect = self.image.get_rect(topright = startPos)
        
    def update(self, health):
        self.percent = health
        self.number = kills
        self.frame = self.calcFrame()
        self.image = self.images(self.frame)
        
    def update(self, kills):
        text = self.baseText + str(kills)
        self.image = self.font.render(text , True, (0, 0, 0))
        self.rect = self.image.get_rect(topright = self.rect.topright)
        
        
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
