import pygame, sys
from simpleButtonClass001 import simpleButton
from pygame.locals import *

def introcreate(height, width, DISPLAYSURF, introduce):

    BGimageFileName = 'GUI/intropic.png'
    logo = 'GUI/LazardsLogo.tga'
    intro_music = pygame.mixer.music.load('gameSounds/intromusic.wav')
    chuckle_sound = pygame.mixer.Sound('gameSounds/chuckle1.wav')
    BGimage = pygame.image.load(BGimageFileName).convert()
    BGimage = pygame.transform.scale(BGimage, (width, height))
    logoimage = pygame.image.load(logo).convert_alpha()
    logow, logoh = logoimage.get_size()
    logow = int(6.5*logow)
    logoh = int(6.5*logoh)
    logoimage = pygame.transform.scale(logoimage, (logow, logoh))

    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(BGimage, (0,0))
    DISPLAYSURF.blit(logoimage, (width//2-logow//2, height//2-logoh//2))

    tfont = pygame.font.SysFont('Impact', 150)
    ttexts = tfont.render('DICE', True, (255, 255, 0, 0), True)
    ttexts = pygame.transform.rotate(ttexts, 30)

    btext1 = 'Begin Rampage'

    tcolor = (195, 55, 55)
    bcolor = (100, 100, 100)

    text_width, text_height = tfont.size(btext1)
    buttonheight = height//15
    buttonwidth = text_width//3
    bxpos = width//2-buttonwidth//2
    bypos = (3*height)//4
    bpos = (bxpos, bypos)
    playbuton = simpleButton(buttonheight, buttonwidth, bcolor, tcolor, btext1, DISPLAYSURF, (bpos))
    playbuton.Active()
    pygame.mixer.music.play(-1)
    while introduce:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == MOUSEBUTTONDOWN:
                mouseXY = pygame.mouse.get_pos()
                if playbuton.clicked(mouseXY):
                    playbuton.highlighted = True
                    chuckle_sound.play()
                    
                    
            elif event.type == MOUSEBUTTONUP:
                if playbuton.clicked(mouseXY):
                    intro = False
                    pygame.mixer.music.fadeout(900)
                    introduce = False
                    return introduce
                    
        playbuton.displayBut()
        pygame.display.update()


