#Jojo was here
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
