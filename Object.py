from Main import *

class Player():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.imagesUp = [pygame.image.load("Player/Images/Playerwithshortsword-Up.png")]
        self.imagesDown = [pygame.image.load("Player/Images/Playerwithshortsword-Down.png")]
        self.imagesRight = [pygame.image.load("Player/Images/Playerwithshortsword-Right.png")]
        self.imagesLeft = [pygame.image.load("Player/Images/Playerwithshortsword-Left.png")]
        
        self.imagesUpShortsword=[pygame.image.load("Player/Images/Standardswingingshortsword-Up.png")]
        self.imagesDownShortsword = [pygame.image.load("Player/Images/Standardswingingshortsword-Down.png")]
        self.imagesRightShortsword = [pygame.image.load("Player/Images/Playerswingingshortsword-Right.png")]
        self.imagesLeftShortsword = [pygame.image.load("Player/Images/Playerswingingshortsword-Left.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
class Monster():
    def __init__(self, speed = [0, 0], startPos=[0, 0]):
        self.images = [pygame.image.load("Boss/Images/Troll.png"),
                      pygame.image.load("Zombie/zombie.png")]
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.rect = self.rect.move(startPos)
         
        self.didbounceX = False
        self.didbounceY = False

# ~ class FloorLoader():
    # ~ def __init__(self, 
