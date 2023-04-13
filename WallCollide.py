from Main import *

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
