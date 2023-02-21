from Main import *


class Player(Knight):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Knight.__init__(self, [0,0], startPos)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
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
