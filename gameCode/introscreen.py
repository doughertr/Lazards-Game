import sys
import pygame
import math
from pygame import *
from pygame.locals import *
from RandomGeneratedLevelClass import Level
from Animate_class import AnimatePlayer
from OverlaysClass import HealthEnergyOverlay, StartScreenOverlay, EndCreditsOverlay # Added by Connor
pygame.init()
flags =  HWSURFACE | DOUBLEBUF
platTopFileName = "blocks-top.gif"
platMidFileName = "blocks-mid.gif"
platCornerFileName = "blocks-corner.gif"
blueMountainFileName = "background-blueMountain.tga"
pinkMountainFileName = "background-pinkMountain.tga"
skyFileName = "background-sky.tga"
treeFileName = "background-trees.tga"
groundFileName = "background-ground.tga"
cloudsFileName = "background-clouds.tga"
HPFileName = "HPIcon.tga"
energyFileName = "EnergyIcon.tga"
intro = True
displayWidth = 1000
displayHeight = 800
uiScaleFactor = 2
halfWidth = displayWidth//2
halfHeight = displayHeight//2
disp = (displayWidth, displayHeight)
fireEvent = pygame.USEREVENT + 1
displaySurf = pygame.display.set_mode(disp, flags)
intropict = pygame.image.load('intropic.bmp').convert()
intropict = pygame.transform.scale(intropict, disp)
displaySurf.fill((0,0,0))
displaySurf.blit(intropict, (0,0))
