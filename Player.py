import pygame, sys, math



class Player():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.image = pygame.image.load("Player/Images/Playerwithshortsword.png")
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
