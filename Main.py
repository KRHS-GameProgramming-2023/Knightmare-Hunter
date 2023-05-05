import pygame, sys, math, random
from Hud import *
from Player import *
from Wall import *
from Troll import *
from Ghoul import *
from Vampire import *
from Object import *
from Boss import *
from LevelLoader import *
# ~ from Spawner import *


pygame.init()
if not pygame.font: print('Warning, fonts disabled')

Clock = pygame.time.Clock();

size = [900, 700]
screen = pygame. display.set_mode(size)

counter = 0;
player = Player(5,[450,350])
monsters = [player]
#score = Hud("Score: ", [0, 0])
#timer = Hud("Time: ", [900-200, 0])

level = 1
#tiles = loadLevel("levels/"+str(level)+".lvl")
#walls = tiles[0]
#spawners = tiles[1]

kills = 0
time = 0

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
        castleWallwithNorthDoorImage = pygame.image.load("Backgrounds/floor1.1.png")
        castleWallwithNorthDoorRect = castleWallwithNorthDoorImage.get_rect(center = [450,100])
    while view == "floor 1":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.goKey("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("down")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.goKey("sup")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("sdown")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left click
                    player.attack("light")
                elif event.button == 3: #right click
                    player.attack("heavy")
                    
        time += 1
        counter += 1
        if counter >= 10:
            counter = 0;
            monsters +=[Monster([
        
             
        player.update(size)

        screen.fill((127, 127, 127))
        screen.blit(bgImage, bgRect)
        screen.blit(castleWallwithNorthDoorImage, castleWallwithNorthDoorRect)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        Clock.tick(60)
