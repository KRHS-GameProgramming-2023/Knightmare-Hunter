import pygame, sys, math, os, pickle
from Object import *
from Player import *
from Monster import *

# ~ def floorLoader(user, coin, shop, monster, player, door = False):
    # ~ outList = []
    # ~ for row in range(14):
        # ~ outRow = []
        # ~ for col in range(18):
            # ~ outRow += [" "]
        # ~ outList += [outRow]
        
    # ~ size = 50
    # ~ offset = size/2
    # ~ for coin in coins:
        # ~ x = int((item.rect.centerx - offset)/size)
        # ~ y = int((item.rect.centery - offset)/size)
        # ~ outList[y][x] = item.char
    # ~ for shop in shops:
        # ~ x = int((item.rect.centerx - offset)/size)
        # ~ y = int((item.rect.centery - offset)/size)
        # ~ outList[y][x] = item.char
    # ~ for monster in monsters:
        # ~ if(enemy.rect.centerx - offset) < 55:
            # ~ x = int((enemy.rect.centerx + offset)/size)
        # ~ elif(enemy.rect.centerx - offset) > (900-55):
            # ~ x = int((enemy.rect.centerx - 2*offset)/size)
        # ~ else:
            # ~ x = int((enemy.rect.centery - offset)/size)
            
        # ~ if(enemy.rect.centery - offset) < 55:
            # ~ y = int((enemy.rect.centery + offset)/size)
        # ~ elif(enemy.rect.centery - offset) > (900-55):
            # ~ y = int((enemy.rect.centery - 2*offset)/size)
        # ~ else:
            # ~ y = int((enemy.rect.centery - offset)/size)
            
        # ~ outList[y][x] = enemy.char
        
    # ~ out = ""
    # ~ for row in range(len(outList)):
        # ~ for col in range(len(outList[row])):
            # ~ out += outList[row][col]
        # ~ out += '\n'
        
    # ~ f = open("Inventories/" + user + "/" + user + ".inv", 'wb')
    # ~ pickle.Pickler(f).dump(player.inventory)
    # ~ f.close()
    
    # ~ f = open("Inventories/" + user + "/" + user + ".hp", 'wb')
    # ~ pickle.Pickler(f).dump(player.hp)
    # ~ f.close()
    
    # ~ f = open("Inventories/" + user + "/" + user + ".ap", 'wb')
    # ~ picklr.Pickler(f).dump([player.weaponChoice])
    # ~ f.close()
    
    # ~ if door:
        # ~ direct = "Rooms/Sav/" + user + "/" + str(player.prevCoord[1] + str(player.prevCoord[0]) + ".sav"
    # ~ elif not door:
        # ~ direct = "Rooms/Sav/" + user + "/" + str(player.coord[1]) + str(player.coord[0]) + ".sav"
    # ~ f = open(direct, 'w')
    # ~ f.write(out)
    # ~ f.close()
    
    # ~ def loadFloor(user, coord = [1, 1], enter = "def"):
        # ~ size = 50
        # ~ offset = size/2
        # ~ tiles = []
        # ~ walls = []
        # ~ doors = []
        # ~ playerLoc = []
        # ~ coins = []
        # ~ shop = []
        # ~ monsters = []
        # ~ hides = []
        # ~ appear = none
        
        # ~ newLines = []
        # ~ newLines2 = []
        
        # ~ direct = "Rooms/Lvl/" + str(coord[1]) + str(coord[0]) + ".lvl"
        # ~ f = open(direct, 'r')
        # ~ lines = f.readLines()
        # ~ f.close()
        
        # ~ for line in lines:
            # ~ newLine = ""
            # ~ for c in line:
                # ~ if c != "\n":
                    # ~ newLine += c
            # ~ newLines += [newLine]
        # ~ lines = newLines
        
        # ~ for y, line in enumerate(lines):
            # ~ for x, c in  enumerate(line):
                # ~ if c == "#":
                    # ~ walls += [Object([x*size + offset, y*size + offset], "wall")]
                # ~ if c == "@":
                    # ~ walls += [Object([x*size + offset, y*size + offset], "door")]
                # ~ if c == "-":
                    # ~ doors += [Object([x*size + 2*offset, y*size + offset], "top")]
                # ~ if c == "_":
                    # ~ doors += [Object([x*size + 2*offset, y*size + offset], "bottom")]
                # ~ if c == "|":
                    # ~ doors += [Object([x*size + 2*offset, y*size + offset], "left")]
                # ~ if c == "/":
                    # ~ doors += [Object([x*size + 2*offset, y*size + 2*offset], "right")]
                # ~ if c == "0":
                    # ~ doors += [Object([x*size + 2*offset, y*size + 2*offset], "doorway1")]
                # ~ if c == "o":
                    # ~ doors += [Object([x*size + 2*offset, y*size + 2*offset], "doorway2")]
                # ~ if c == "D" and enter == "def":
                    # ~ playerLoc = [x*size + offset, y*size + offset]
                # ~ elif c == "%" and (enter == "bottom" or enter == "tutorialExit"):
                    # ~ playerLoc = [x*size + 2*offset, y*size + offset]
                # ~ elif c == "&" and (enter == "top" or enter == "tutorialEntrance"):
                    # ~ playerLoc = [x*size + 2*offset, y*size + offset]
                # ~ elif c == "(" and (enter == "right" ot enter == "portal1"):
                    # ~ playerLoc = [x*size + offset, y*size + 2*offset]
                # ~ elif c == ")" and (enter == "left" or enter == "portal2"):
                    # ~ playerLoc = [x*size + offset, y*size + 2*offset]
                
        # ~ if os.path.isfile("Rooms/Sav/" + user + "/" + str(coord[1]) + str(coord[0]) + ".sav"):
            # ~ direct2 = "Rooms/Sav/" + user + "/" + str(coord[1]) + str(coord[0]) + ".sav"
            # ~ g = open(direct2, 'r')
            # ~ lines2 = g.readlines()
            # ~ g.close()
            
            
            # ~ for line in lines2:
                # ~ newLine2 = ""
                # ~ for c in line:
                    # ~ if c != "\n":
                        # ~ newLine2 += c
                # ~ newLines2 += [newLine2]
            # ~ lines2 = newLines2
            
            # ~ for y, line in enumerate(line2):
                # ~ for x, c in enumerate(line):
                    # ~ if c == "!":
                        # ~ items += [Item([x*size + offset, y*size + offset], "shortSword", '!')]
                    # ~ if c == "*":
                        # ~ items += [Item([x*size + offset, y*size + offset], "FuryoftheEmperor", '*')]
                    # ~ if c == "~":
                        # ~ items += [Item([x*size + offset, y*size + offset], "battleAxe", '~')]
                    # ~ if c == ";":
                        # ~ items += [Item([x*size + offset, y*size + offset], "HealthPotion", ';')]
                    # ~ if c == ":":
                        # ~ items += [Item([x*size + offset, y*size + offset], "staminaPotion", ':')]
                    # ~ if c == "$":
                        # ~ items += [Item([x*size + offset, y*size + offset], "Coin", '$')]
                    # ~ if c == "1":
                        # ~ enemies += [Enemy([x*size + offset, y*size + offset], "basic")]
                    
