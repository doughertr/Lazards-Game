import random
from random import randint
import sys
import pygame
from pygame import *

class Level:
    def __init__(self, numChunks):
        self.levelLength = numChunks #this is how many choice or chunks the level will be. each choice is 8 blocks long and 'levelHeight' blocks high 
        self.levelHeight = 16 #amount of vertical squares. This probably wont ever change
        self.startingZone = [
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                                ",
            "                               ",
            "                   E E E        ",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
        self.choices = [[
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "   E  E ",
            "        ",
            "PPPPPPPP",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",],[
                
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "   E    ",
            "        ",
            "  LPPR  ",
            "        ",
            "   E    ",
            "        ",
            "PPPPPPPP",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",],[

            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "   E    ",
            "        ",
            "   LR   ",
            "  LXXR  ",
            " LXXXXR ",
            "PXXXXXXP",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",],[

            "        ",
            "        ",
            "        ",
            "   E E  ",
            "  LPPR  ",
            "        ",
            "        ",
            "        ",
            "    E   ",
            "        ",
            "   E    ",
            "        ",
            "PPPPPPPP",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",],[

            "        ",
            "        ",
            "        ",
            "        ",
            "       L",
            "   E  LX",
            "     LXX",
            "E   LXXX",
            "   LXXXX",
            "  LXXXXX",
            " LXXXXXX",
            "LXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",] ]
        
        self.caveChoices = [[
            'PPPPPPPPPPPPPPPP',
            ' PPPPPPPPPPPPPPP',
            '   PPPPPPPPPPPPP',
            '             PPP',
            '              PP',
            '                ',
            '                ',
            '                ',
            '                ',
            '                ',
            '                ',
            '             E  ',
            '   E            ',
            'PPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPP',],[
                
            'PPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPP ',
            'PPPPPPPPPPPPP   ',
            'PPP             ',
            'PP              ',
            '                ',
            '                ',
            '                ',
            '                ',
            '                ',
            '                ',
            '                ',
            'E E    E        ',
            'PPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPP',],[
                
            'PPPPPPPP',
            'PPPPPPPP',
            'PPPPPPPP',
            '        ',
            '        ',
            '        ',
            '        ',
            '        ',
            '   E    ',
            '        ',
            '        ',
            '        ',
            '   E E  ',
            'PPPPPPPP',
            'PPPPPPPP',
            'PPPPPPPP',],[            
                
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPP     PPP          PPPPPPPPP      PPPPPPPP',
            'PPPP         PP           PPPPPPP        PPP    ',
            ' P            P           PPPPPPP        P      ',
            '                            PPPP         P      ',
            '                             PPP                ',
            '                              P                 ',
            '   E               E                            ',
            '    PP              P                  E        ',
            '   PPP             PPPP              PPPP       ',
            '  PPPPP    E     PPPPPP        E    PPPPPP      ',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',],[
                
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP PP',
            'PP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP       P',
            '        PPPPPPPPPPPPPPPPPPPPPPPPPPP             ',
            '            PPPPPPPPPPPPPPPPPPPP                ',
            '                PPPPPPPPPP                      ',
            '                    PPPPP                       ',
            '           E         PPP                E       ',
            '                           E                    ',
            '                                                ',
            '   E E                                           ',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',
            'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',] ]               
        #self.choiceDict = {tuple(self.choices[k]):0 for k in range(len(self.choices))}
        self.caveChoiceDict = {tuple(self.caveChoices[l]):0 for l in range(len(self.caveChoices))}
        self.choiceDict = {tuple(self.choices[0]):0,tuple(self.choices[1]):15,tuple(self.choices[2]):15, tuple(self.choices[3]):20, tuple(self.choices[4]):100} #this is used to count how many of each choice is created. Its useful later
        self.level = [""]*(self.levelHeight) #creates a blank level to start with
    def buildLevel(self):
        self.outsideLength = self.levelLength
        self.caveLength = 10
        #BUILDING STARTING ZONE
        self.pos = 0
        self._addChunk(self.startingZone,self.pos)   
        #BUILDING OUTSIDE
        for i in range(self.outsideLength): #stops after creating levelLength amount of chunks/choices
            self.pos = 0
            self.chunk = self._selectiveRandom(self.choices,self.choiceDict)
            '''if (len(self.chunk[0])//8 > (self.outsideLength - i)):
                i-=1
                continue'''
            self.choiceDict[tuple(self.chunk)] += 1 
            self._addChunk(self.chunk,self.pos)
        #BUILDING CAVE
        self.caveRandPos = random.randint(1, self.levelLength - 1) * 8
        for z in range(self.caveLength): #stops after creating levelLength amount of chunks/choices
            self.pos = 0
            self.caveChunk = self._selectiveRandom(self.caveChoices,self.caveChoiceDict)
            '''if (len(self.caveChunk[0])//8 > (self.outsideLength - z)):
                z-=1
                continue'''
            self.caveChoiceDict[tuple(self.caveChunk)] += 1 
            self._addChunk(self.caveChunk,self.pos)      
        return self.level
    def _addChunk(self, chnk, pos):
        for row in chnk: #steps through the chosen chunk's rows and collumn's and adds it to the level
            for col in row:
                self.level[self.pos] += col
            self.pos += 1        
    def _selectiveRandom(self, cl, dic): #custom random function that makes a chunk/choice less weighted the more that are created
        #this will basically make a more even random, making it almost impossible to see 20 of 1 type of chunk generated
        self.weightedChoice = []
        for i in range(len(cl)):
            self.weightedChoice += [cl[i]]*int(100/(1 + dic[tuple(cl[i])])) #if no chunks of a given type are created, then there is a 10 in 50 chance that one will be created. If 1 chunk of a given type is created, then there is a 5 in 50 chance that another one will be created 
        return random.choice(self.weightedChoice)
        
    def getChoiceDict(self):
        return self.choiceDict
            
