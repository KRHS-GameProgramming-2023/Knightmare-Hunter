import pygame, sys, math
from Main import *
from Troll import *
from Ghoul import *
from Vampire import *
from Boss import *

class Monster():
    def __init__(self, speed = [0, 0], startPos=[0, 0]):
        self.images = [pygame.image.load("images/troll/troll.png"),
                      pygame.image.load("images/troll/troll1.png")]
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rectwidth/2)/2
        
        self.rect = self.rect.move(startPos)
        
        self.didbounceX = False
        self.didbounceY = False
        
        self.kind = "troll"
        
    def update(self, size):
        self.move()
        
        self.didbounceX = False
        self.didbounceY = False
        
        self.wallCollide(size)
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didbounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didbounceY = True
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.didbounceX = True
        if not self.didbounceX:
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.didbounceY = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.didbounceX = True
    def playerCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist (other) < self.rad + other.rad:
                                if not self.didbounceX:
                                    self.speedx = -self.speedx
                                if not self.didbounceY:
                                    self.speedy = -self.speedy
                                return True
        return False
        
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if not self.didbounceX:
                            self.speedx = -self.speedx
                            self.didbounceX = True
                        if not self.didbounceY:
                            self.speedy = -self.speedy
                            self.didbounceY = True
                        return True
        return False
        
    def dist(self,other):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = other.rect.centerx
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
        
        
