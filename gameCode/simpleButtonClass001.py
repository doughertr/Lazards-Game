# simpleButtonClass.py

import pygame
from pygame.locals import *


class simpleButton:

    # class that creates button objects

    def __init__(self, height, width, color, textColor, label, surf, position):

        # define some values

        self.SURF = surf
        self.POS = position
        self.BUTCOLOR  = color
        self.BUTGREY   = (color[0] * .25, color[1] * .25, color[2] * .25)
        self.HIGHLIGHTCOLOR = (color[0] + ((255 - color[0])//3),
                               color[1] + ((255 - color[1])//3),
                               color[2] + ((255 - color[2])//3))
                               
        self.TEXTCOLOR = textColor
        self.BLACK = (0, 0, 0)

        self.HEIGHT   = height
        self.WIDTH  = width
        self.RADIUS   = self.HEIGHT//2
        THEIGHT  = int(self.HEIGHT * .72)

        self.active = True
        self.highlighted = False

        BUTFONT = pygame.font.SysFont("Impact", THEIGHT)
        # Render a Text Surface
        self.TEXTSURF = BUTFONT.render(label, True, textColor, None)

        w, h   = self.TEXTSURF.get_size()
        
        self.XPOS   = (self.WIDTH - w)//2
        self.YPOS   = int((self.HEIGHT - h)//2)
        twidth = w

        self.BUTTONSURF = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.BUTTONSURF.fill((0, 0, 0, 0))

    def __buttonBG(self, color):

        # create square with rounded corners
       
        pygame.draw.circle(self.BUTTONSURF, color, (self.RADIUS, self.RADIUS),
                           self.RADIUS)
        pygame.draw.circle(self.BUTTONSURF, color,
                           (self.WIDTH - self.RADIUS, self.RADIUS), self.RADIUS)

        pygame.draw.rect(self.BUTTONSURF, color,  Rect((self.RADIUS, 0), (self.WIDTH - 2 * self.RADIUS, self.HEIGHT)))

    def __buttonText(self):

        # Draw Text
        self.BUTTONSURF.blit(self.TEXTSURF, (self.XPOS, self.YPOS))

    def clicked(self, mouseXY):
        yesORno = False
        P1 = self.POS
        P2 = (P1[0] + self.WIDTH, P1[1] + self.HEIGHT)
        yesORno = (self.active and P1[0] <= mouseXY[0] <= P2[0] and
                   P1[1] <= mouseXY[1] <= P2[1])

        return yesORno

    def Active(self):
        self.active = True
        return True

    def InActive(self):
        self.active = False
        return False


    def displayBut(self):
        
        if self.active:
            if self.highlighted:
                self.__buttonBG(self.HIGHLIGHTCOLOR)
                self.__buttonText()
                self.SURF.blit(self.BUTTONSURF, self.POS)
            else:
                self.__buttonBG(self.BUTCOLOR)
                self.__buttonText()
                self.SURF.blit(self.BUTTONSURF, self.POS)

        
## if B1.clicked(mouseXY)
##                B1.displayBut()
##                setValue(dieobjlist)
       
