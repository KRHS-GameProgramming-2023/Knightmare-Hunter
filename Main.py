import pygame, sys, math, random
from Player import *
from Wall import *
from Troll import *
from Ghoul import *
from Vampire import *
from Object import *
from Boss import *


pygame.init()

Clock = pygame.time.Clock();

size = [900, 700]
screen = pygame. display.set_mode(size)

view = "title"
while True:
    if view == "title":
        bgImage = pygame.image.load("Backgrounds/titlescreen.png")
        bgRect = bgImage.get_rect()
    while view == "title":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    view = "floor 1"
                    

        screen.fill((127, 127, 127))
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        Clock.tick(60)
        
    if view == "floor 1":
        bgImage = pygame.image.load("Backgrounds/floor1.png")
        bgRect = bgImage.get_rect()
    while view == "floor 1":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            
                    

        screen.fill((127, 127, 127))
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        Clock.tick(60)
