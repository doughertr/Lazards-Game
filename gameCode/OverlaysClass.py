# OverlaysClass.py
# Connor Eccleston

# Health and energy bars overlay

import pygame
from pygame.locals import *

class HealthEnergyOverlay:

    def __init__(self, surface, displayWidth, displayHeight):
        
        
        self.SURF = surface
        self.DWIDTH = displayWidth
        self.DHEIGHT = displayHeight

        self.GREY = (95, 95, 95)

        self.pixel = self.DHEIGHT//100
        self.barLength = int(self.DWIDTH/3.25)

        self.HPIcon = pygame.image.load("GUI/HPIcon.tga").convert_alpha()
        self.EnergyIcon = pygame.image.load("GUI/EnergyIcon.tga").convert_alpha()
        
        self.HPIconWidth = 9*self.pixel
        self.HPIconHeight = 7*self.pixel
        self.HPIcon = pygame.transform.scale(self.HPIcon, (self.HPIconWidth, self.HPIconHeight))

        self.EnergyIconWidth = 7*self.pixel
        self.EnergyIconHeight = 11*self.pixel
        self.EnergyIcon = pygame.transform.scale(self.EnergyIcon, (self.EnergyIconWidth, self.EnergyIconHeight))

    def __blitIcons(self):

        self.SURF.blit(self.HPIcon, (5*self.pixel, 5*self.pixel))
        self.SURF.blit(self.EnergyIcon, (self.DWIDTH - self.EnergyIconWidth - 5*self.pixel, 3*self.pixel))

    def __drawEmptyBars(self):

        xOffset = self.HPIconWidth + 6*self.pixel
        yOffset = 6*self.pixel

        pygame.draw.rect(self.SURF, self.GREY, Rect((xOffset + self.pixel, yOffset), (self.barLength + 2*self.pixel, 5*self.pixel))) #taller health rect
        pygame.draw.rect(self.SURF, self.GREY, Rect((xOffset, yOffset + self.pixel), (self.barLength + 4*self.pixel, 3*self.pixel))) #longer health rect
        pygame.draw.rect(self.SURF, (151, 0, 0), Rect((xOffset + 2*self.pixel, yOffset + self.pixel), (self.barLength, 3*self.pixel))) #inside health rect
        
        pygame.draw.rect(self.SURF, self.GREY, Rect((self.DWIDTH - self.barLength - xOffset + 4*self.pixel - 4*self.pixel, yOffset), (self.barLength + 2*self.pixel, 5*self.pixel))) #taller energy rect
        pygame.draw.rect(self.SURF, self.GREY, Rect((self.DWIDTH - self.barLength - xOffset - 4*self.pixel + 3*self.pixel, yOffset + self.pixel), (self.barLength + 4*self.pixel, 3*self.pixel))) #longer energy rect
        pygame.draw.rect(self.SURF, (30, 30, 125), Rect((self.DWIDTH - self.barLength - xOffset + 2*self.pixel - 1*self.pixel, yOffset + self.pixel), (self.barLength, 3*self.pixel))) #inside energy rect
        
    def __drawMeters(self, healthAmount, energyAmount):

        xMod = self.barLength - int(self.barLength * (energyAmount/100))

        pygame.draw.rect(self.SURF, (255, 0, 0), Rect((self.HPIconWidth + 8*self.pixel, 7*self.pixel), (int(self.barLength * (healthAmount/100)), 3*self.pixel)))
        pygame.draw.rect(self.SURF, (0, 0, 255), Rect((self.DWIDTH - self.barLength - self.HPIconWidth - 1*self.pixel + xMod - 4*self.pixel, 7*self.pixel), (int(self.barLength * (energyAmount/100)), 3*self.pixel)))

    def drawOverlay(self, healthAmount, energyAmount): # Goes inside of screen update loop, health and energy amounts must be 0-100

        healthAmount = int(healthAmount)
        energyAmount = int(energyAmount)

        self.__blitIcons()
        self.__drawEmptyBars()
        self.__drawMeters(healthAmount, energyAmount)

class StartScreenOverlay:

    def __init__(self, surface, displayWidth, displayHeight):
        
        self.SURF = surface
        self.DWIDTH = displayWidth
        self.DHEIGHT = displayHeight

        self.SSBackground = pygame.image.load("GUI/SSBackground.tga").convert()
        self.SSBWidth = self.DWIDTH
        self.SSBHeight = self.DHEIGHT
        self.SSBackground = pygame.transform.scale(self.SSBackground, (self.SSBWidth, self.SSBHeight))
        
        self.LazardsLogo = pygame.image.load("GUI/LazardsLogo.tga").convert_alpha()
        self.LogoHeight = int(0.47*self.DHEIGHT)
        self.LogoWidth = int(self.LogoHeight*(89/29))
        self.LazardsLogo = pygame.transform.scale(self.LazardsLogo, (self.LogoWidth, self.LogoHeight))

        self.pixel = self.LogoHeight//35
        self.Continue = pygame.image.load("GUI/Continue.tga").convert_alpha()
        self.ContinueWidth = int(89*self.pixel) 
        self.ContinueHeight = int(5*self.pixel)
        self.Continue = pygame.transform.scale(self.Continue, (self.ContinueWidth, self.ContinueHeight))

    def drawOverlay(self):

        space = self.DHEIGHT//2+self.LogoHeight//2

        self.SURF.blit(self.SSBackground, (0, 0))
        self.SURF.blit(self.LazardsLogo, (self.DWIDTH//2-self.LogoWidth//2, self.DHEIGHT//2-self.LogoHeight//2))
        self.SURF.blit(self.Continue, (self.DWIDTH//2-self.ContinueWidth//2, space + (self.DHEIGHT-space)//3))

class EndCreditsOverlay:

    def __init__(self, surface, displayWidth, displayHeight):

        self.SURF = surface
        self.DWIDTH = displayWidth
        self.DHEIGHT = displayHeight
        
        self.ECBackground = pygame.image.load("GUI/ECBackground.tga").convert()
        self.ECBWidth = self.DWIDTH
        self.ECBHeight = self.DHEIGHT
        self.ECBackground = pygame.transform.scale(self.ECBackground, (self.ECBWidth, self.ECBHeight))

        self.Credits = pygame.image.load("GUI/Credits.tga").convert_alpha()
        self.CreditsHeight = int(0.9*self.DHEIGHT)
        self.CreditsWidth = int(self.CreditsHeight*0.75)
        self.Credits = pygame.transform.scale(self.Credits, (self.CreditsWidth, self.CreditsHeight))

    def drawOverlay(self):

        self.SURF.blit(self.ECBackground, (0, 0))
        self.SURF.blit(self.Credits, (self.DWIDTH//2-self.CreditsWidth//2, self.DHEIGHT//2-self.CreditsHeight//2))
