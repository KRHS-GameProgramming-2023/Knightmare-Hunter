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
