import pygame, sys, math


class Player():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.imageUp = [pygame.image.load("Player/Images/Playerwithshortsword-up.png")]
        self.imageDown = [pygame.image.load("Player/Images/Playerwithshortsword-down.png")]
        self.imageRight = [pygame.image.load("Player/Images/Playerwithshortsword-right.png")]
        self.imageLeft = [pygame.image.load("Player/Images/Playerwithshortsword-left.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = 0
        self.speedy = 0
        self.radius = self.rect.height/2
        self.speed = [self.speedx,self.speedy]
        
        self.maxSpeed = maxSpeed
        self.kind = "Player"
        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = self.maxSpeed
        if direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        d = False
        if not self.didbounceY: 
            if self.rect.bottom > height:
                d = "bottom"
            if self.rect.right > width:
                d = "right"
        if not self.didbounceX:
            if self.rect.top < 0:
                d = "top"
            if self.rect.left < 0:
                d = "left"
        if d: print("IN FUNCTION", d)
        return d
    
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
                            self.move()
                            self.speedx = 0
                        if not self.didbounceY:
                            self.speedy = -self.speedy
                            self.didbounceY = True
                            self.move()
                            self.speedy = 0
                        return True
        return False
        
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
            
    def update(self, size):
        self.move()
        self.wallCollide(size)
        
    def move(self):
        self.speed = [self.speedx,self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        if self.rect.bottom > size[1]:
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.speedy = -self.speedy
        
        if self.rect.right > size[0]:
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.speedx = -self.speedx
    
    def attack(self, power):
        print(power + " attack") 
    
        
    def dist(self,other):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = other.rect.centerx
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
