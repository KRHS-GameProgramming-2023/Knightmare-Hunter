import pygame, sys, math

class Hud():
    def __init__(self, pos=[50,50]):
        self.font = pg.font.Font(None, 64)
        self.image = self.font.render("Score: 0", True, (0, 0, 0))
        self.rect = slef.image.get_rect(center = startPos)
