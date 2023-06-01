import pygame, sys, math, random
from Health import *
from Player import *
from Wall import *
# ~ from Object import *
from Monster import *
# ~ from Spawner import *
from Hud import *

pygame.init()
if not pygame.font: print('Warning, fonts disabled')

Clock = pygame.time.Clock();

size = [900, 700]
screen = pygame. display.set_mode(size)

counter = 0;
player = Player(5,[450,350])
monsters = [player]
health = Health([0, 0])
h =100
score = Hud("Score: ",[0,0])
#timer = Hud("Time: ", [900-200, 0])
 
level = 1 
#tiles = loadFloor("levels/"+str(level)+"floor2")
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
                    view = "floor 2"
                    

        screen.fill((127, 127, 127))
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        Clock.tick(60)
        
    if view == "floor 2":
        bgImage = pygame.image.load("Backgrounds/floor2.png")
        bgRect = bgImage.get_rect()
        castleWallwithNorthDoorImage = pygame.image.load("Backgrounds/floor2.png")
        castleWallwithNorthDoorRect = castleWallwithNorthDoorImage.get_rect(center = [450,100])
    while view == "floor 2":
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
        if counter >= 5:
            counter = 0;
            monsters +=[Monster([random.randint(-3, 3), random.randint(-3, 3)],
                [random.randint(50, 350), random.randint(50, 250)])
            ] 
            for monster in monsters:
                if monsters[-1].monsterCollide(monster):
                    monsters.remove(monsters[-1])
                    break
            
        for monster in monsters:
            monster.update(size)
            
        health.update(player.hp)
        
        for hittingMonster in monsters:
            for hitMonster in monsters:
                if hittingMonster.monsterCollide(hitMonster):
                    if hittingMonster.kind == "player":
                        monsters.remove(hitMonster)
                        health += 1
            #for wall in walls:
                #hittingMonster.wallTileCollide(wall)
                
        # ~ d = player.wallCollide(size)
        # ~ print("IN MAIN",player.wallCollide(size))
        # ~ if d:
            # ~ print("????????????")
            # ~ if level == 2 and d == "right":
                # ~ level = 3
                # ~ tiles = loadLevel("levels/"+str(level)+"floor2")
                # ~ walls = tiles[0]
                # ~ spawners = tiles[1]
                # ~ player.rect.left = 1
            # ~ elif level == 3 and d == "left":
                # ~ level = 2
                # ~ tiles = loadLevel("levels/"+str(level)+"floor3")
                # ~ walls = tiles[0]
                # ~ spawners = tiles[1]
                # ~ player.rect.right = size[0]-1
            # ~ elif level == 3 and d == "right":
                # ~ level = 4
                # ~ tiles = loadLevel("levels/"+str(level)+"floor3")
                # ~ walls = tiles[0]
                # ~ spawners = tiles[1]
                # ~ player.rect.left = 1
            # ~ elif level == 4 and d == "left":
                # ~ level = 3
                # ~ tiles = loadLevel("levels/"+str(level)+"floor4")
                # ~ walls = tiles[0]
                # ~ spawners = tiles[1]
                # ~ player.rect.right = 1
            
           
                 
            player.update(size)

            screen.fill((127, 127, 127))
            screen.blit(bgImage, bgRect)
            screen.blit(castleWallwithNorthDoorImage, castleWallwithNorthDoorRect)
            for monster in monsters:
                screen.blit(monster.image,monster.rect)
            screen.blit(health.image, health.rect)
            pygame.display.flip()
            Clock.tick(60)
