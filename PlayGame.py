import pygame, sys
import math
from pygame import *
import random
from random import *

sys.path.append('gameCode')

from RandomGeneratedLevelClass import Level
from playerAnimateClass import AnimatePlayer, AnimateEnemy, AnimateGun, AnimateLaser
from OverlaysClass import HealthEnergyOverlay, StartScreenOverlay, EndCreditsOverlay # Added by Connor
from introclass import introcreate
from simpleButtonClass001 import simpleButton

pygame.mixer.pre_init(44100, -16, 2, 1024*4)
pygame.init()


flags =  HWSURFACE | DOUBLEBUF
platTopFileName = "GUI/blocks-top.gif"
platMidFileName = "GUI/blocks-mid.gif"
platCornerFileName = "GUI/blocks-corner.gif"
blueMountainFileName = "backgroundImages/background-blueMountain.tga"
pinkMountainFileName = "backgroundImages/background-pinkMountain.tga"
skyFileName = "backgroundImages/background-sky.tga"
treeFileName = "backgroundImages/background-trees.tga"
groundFileName = "backgroundImages/background-ground.tga"
cloudsFileName = "backgroundImages/background-clouds.tga"
HPFileName = "GUI/HPIcon.tga"
energyFileName = "GUI/EnergyIcon.tga"
introFileName = 'GUI/intropic.tga'
lazer_shot = pygame.mixer.Sound('gameSounds/lazergun.wav')
pant_sound = pygame.mixer.Sound('gameSounds/panting.wav')

displayWidth = 1000
displayHeight = 800
uiScaleFactor = 2
halfWidth = displayWidth//2
halfHeight = displayHeight//2
disp = (displayWidth, displayHeight)
fireEvent = pygame.USEREVENT + 1

def main():
    global cameraX, cameraY
    global direction
    global entities
    global platform
    global player
    global game
    global score
    score = 0
    intro = True
    FOV = 30 #DEFAULT is 30
    playerFireTimer = 400
    direction = "right"
    tileSize = 32 #TODO implement this so that we can resize every square
    displaySurf = pygame.display.set_mode(disp, flags)    
    
    pygame.display.set_caption("Lazards Game Test")
    timer = pygame.time.Clock()
    playerFireTimer = 200
    playerJump = playerLeft = playerRight = playerDown = False
    playerFire = True
    enemies = []
    entities = pygame.sprite.Group() #This is a type of list called a sprite group that stores all game sprites
    player = Player(50,75,enemies,entities)
    playerLaserGun = LaserGun(player.rect.x, player.rect.y, 115,100)
    #entities.add(playerLaserGun)
    platforms = [] #List to store all collidable platforms
    
    levelX = levelY = 0
    levelLength = 50 # amount of chucks or in other words levelLength*8 = how many horizontal squares the level will be
    gameLevel = Level(levelLength)
    level = gameLevel.buildLevel() #builds a random level using magic
    #print(gameLevel.getChoiceDict()) #this will print out a bunch of 'P's. Its only here to test how effectively the random distribution is working
    for row in level: #This nested for loop reads all the P's that we created and places platforms in their position
        for col in row[:FOV]:
            if col == "P":
                plat = Platform(levelX,levelY,tileSize, platTopFileName)
                platforms.append(plat)
                entities.add(plat)
            if col == "X":
                plat = Platform(levelX,levelY,tileSize, platMidFileName)
                platforms.append(plat)
                entities.add(plat)
            if col == "L":
                plat = Platform(levelX,levelY,tileSize, platCornerFileName)
                platforms.append(plat)
                entities.add(plat)
            if col == "R":
                plat = Platform(levelX,levelY,tileSize, platCornerFileName)
                plat.image = pygame.transform.flip(plat.image, True, False)
                platforms.append(plat)
                entities.add(plat)  
            if col == "E":
                enem = Enemy(levelX,levelY,platforms)
                enemies.append(enem)
                entities.add(enem)
                
                
                
            levelX+=32
        levelY+=32
        levelX=0
    colNum = FOV
    levelY = 0
    levelX = FOV*32
    
    backgroundList = [
        Background(0,20,displayWidth, displayHeight,15,pinkMountainFileName),
        Background(50,20,displayWidth, displayHeight,15,pinkMountainFileName),
        Background(0,20,displayWidth, displayHeight,5,blueMountainFileName),
        Background(0,0,displayWidth, displayHeight,2.5,groundFileName),
        Background(0,0,displayWidth, displayHeight,2.5,treeFileName),
        Background(0,0,displayWidth, displayHeight,10,cloudsFileName)
    ]
    
    HPXpos = 18
    energyXpos = displayWidth-380
    uiList = [
        UserInterface(HPXpos,50,20,20,uiScaleFactor, displaySurf, HPFileName),
        UserInterface(energyXpos,50,20,20,uiScaleFactor, displaySurf, energyFileName)
    ]
    
    hpBar = UIbar(displaySurf, None,(255,0,0), False,HPXpos)
    energyBar = UIbar(displaySurf, None, (85,197,255), True, energyXpos)
    uiList.append(hpBar)
    uiList.append(energyBar)
    
    entireLevelWidth = len(level[0])*32
    entireLevelHeight = len(level)*32
    camera = Camera(entireLevelWidth,entireLevelHeight, cameraMovement)
    introduce = True
    while introduce:
        introduce = introcreate(displayHeight, displayWidth, displaySurf, introduce)
    game = True
    game_music = pygame.mixer.music.load('gameSounds/backgroundGameMusic.wav')
    pygame.mixer.music.play(-1)
    pant_sound1 = pygame.mixer.Sound('gameSounds/panting.wav')
    pant_sound2 = pygame.mixer.Sound('gameSounds/panting.wav')
    jump_sound = pygame.mixer.Sound('gameSounds/jump.wav')
    while game:
        timer.tick(60) #60fps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if playerFire == True and energyBar.getAmt() > 21:
                    lazer_shot.play()
                    player.fireLaser()
                    playerFire = False
                    energyBar.subtractAmt(20)
                    pygame.time.set_timer(fireEvent, playerFireTimer)
            if event.type == KEYDOWN and event.key == K_w:
                playerJump = True
                jump_sound.play()
            if event.type == KEYDOWN and event.key == K_s:
                playerDown = True
            if event.type == KEYDOWN and event.key == K_a:
                playerLeft = True
                playerRight = False
                pant_sound.play()
                if direction != "left": #fliping the sprite
                    direction = "left"
            if event.type == KEYDOWN and event.key == K_d:
                playerRight = True
                playerLeft = False
                pant_sound.play()
                if direction != "right": #fliping the sprite
                    direction = "right"
                
            if event.type == KEYUP and event.key == K_w:
                playerJump = False
            if event.type == KEYUP and event.key == K_s:
                playerDown = False
            if event.type == KEYUP and event.key == K_a:
                playerLeft = False
            if event.type == KEYUP and event.key == K_d:
                playerRight = False
                
            if event.type == fireEvent:
                playerFire = True
                
                pygame.time.set_timer(fireEvent, 0)
        camera.update(player) #camera "focuses" on player or in other words the entire level is moving with respect to the player's button imputs
        if playerRight:
            if(player.rect.x//32 + FOV > colNum):
                levelX=colNum*32 
                for row in level:  
                    if ([(k.x,k.y) for k in platforms].count((levelX,levelY)) < 1):
                        for col in row[colNum]:
                            if col == "P":
                                plat = Platform(levelX,levelY,tileSize, platTopFileName)
                                platforms.append(plat)
                                entities.add(plat)
                            if col == "X":
                                plat = Platform(levelX,levelY,tileSize, platMidFileName)
                                platforms.append(plat)
                                entities.add(plat)
                            if col == "L":
                                plat = Platform(levelX,levelY,tileSize, platCornerFileName)
                                platforms.append(plat)
                                entities.add(plat)
                            if col == "R":
                                plat = Platform(levelX,levelY,tileSize, platCornerFileName)
                                plat.image = pygame.transform.flip(plat.image, True, False)
                                platforms.append(plat)
                                entities.add(plat)
                            if col == "E":
                                tempInt = randint(0,1)
                                if tempInt == 1:
                                    enem = Enemy(levelX,levelY,platforms)
                                    enemies.append(enem)
                                    entities.add(enem)
                                                       
                    levelY+=32
                        
                removePlatList = filter(lambda t: isinstance(t,Platform) and t.x <= levelX - 48*int(FOV*1.6), entities)
                for platFm in removePlatList:
                    platforms.remove(platFm)  
                    entities.remove(platFm)
                #removeEnemyList = filter(lambda e: isinstance(e,Enemy) and (e.rect.x <= levelX - 48*int(FOV*1.6) or e.rect.y >= displayHeight), entities)
                #for enemy in removeEnemyList:
                    #enemies.remove(enemy)  
                    #entities.remove(enemy)                   
                colNum += 1
        levelY = 0
        displaySurf.fill((130,209,220))
        for en in enemies:
            if en.rect.x > levelX:
                en.setEnemyOffScreen()
            elif en.rect.x <= levelX - 48*int(FOV*1.6):
                en.setEnemyOffScreen()
                enemies.remove(en)  
                entities.remove(en)                         
            else:
                en.setEnemyOnScreen()        
        for back in backgroundList:
            back.update(displaySurf, player, camera)
        for ui in uiList:
            ui.update()
             

        #gameBars.drawOverlay(playerHealth, playerEnergy) # Added by Connor
            
        for ent in entities:
            displaySurf.blit(ent.image, camera.blitToCam(ent))
            ent.update()
        if direction == "right":
            displaySurf.blit(playerLaserGun.image, (camera.blitToCam(playerLaserGun).x -5 , camera.blitToCam(playerLaserGun).y- 15))
        else:
            displaySurf.blit(playerLaserGun.image, (camera.blitToCam(playerLaserGun).x -55 , camera.blitToCam(playerLaserGun).y- 15))
        displaySurf.blit(player.image, (camera.blitToCam(player).x - 30 , camera.blitToCam(player).y-20))
        
        player.update( playerJump, playerDown, playerLeft, playerRight, playerFire, direction, platforms,camera,hpBar)
        playerLaserGun.update(player)
        pygame.display.update()
        #print(timer.get_fps())
        #print(len(entities))
        #print(len(enemies))
        #print((camera.levelRect.x,halfWidth-player.rect.x))
        print(player.rect.y)
    
class Camera:
    def __init__(self,width,height,func):
        self.levelRect = Rect(0,0,width,height) #this rectangle holds the entire level
        self.cameraFunc = func
    def blitToCam(self, obj):
        return obj.rect.move(self.levelRect.x, self.levelRect.y) #blits all game objects to the camera's rectangle
    def update(self, obj):
        self.levelRect = self.cameraFunc(self.levelRect, obj)

def cameraMovement(camera, target):
    l, t, _, _ = target.rect
    _, _, w, h = camera
    l, t, _, _ = -l+halfWidth, -t+halfHeight, w, h
    
    l = min(camera.x, l)
    t = max (200, t)
    return Rect(l, t, w, h)
    
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #all entities extend the Sprite class, by extending the sprite class objects gain an image and collision rect
    def update(self):
        pass
class Player(Entity, AnimatePlayer):
    def __init__(self, x , y, enemies, entities):
        Entity.__init__(self)
        self.playerXVelocity = 0
        self.playerYVelocity = 0
        self.onGround = False
        self.hit = False
        self.image = pygame.Surface((128,128), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()        
        self.rect = Rect(0,0,x,y) #collision rectangle
        self.x = x
        self.y = y
        self.hurt_sound = pygame.mixer.Sound('gameSounds/hurt.wav')
        self.death_sound = pygame.mixer.Sound('gameSounds/death.wav')

        # Enemy related variables
        self.enem = enemies
        self.ent = entities

        #health
        self.Health = 100
        self.ticks = pygame.time.get_ticks()

        AnimatePlayer.__init__(self,self.image)
    def update(self, jump, down, left, right, fire, direction, platforms, cam,healthBar):
        self.camera = cam
        self.direction = direction
        
        if jump:
            AnimatePlayer.stopForJump(self)
            if self.onGround:
                self.playerYVelocity = -20 #Jump velocity, starts decreasing as soon as onGround is false which happens when there is no collision with the top of a platform
        if down:
            pass
        if left:
            AnimatePlayer.moveL(self)
            self.playerXVelocity = -8
            
        if right:
            AnimatePlayer.moveR(self)
            self.playerXVelocity = 8
            
        if not self.onGround:
            self.playerYVelocity += .75 #accelerated fall
            if self.playerYVelocity > 100:
                self.playerYVelocity = 100 # terminal veloctiy
        if not(left or right):
            if direction == "right":
                AnimatePlayer.idleR(self)
            else:
                AnimatePlayer.idleL(self)
            self.playerXVelocity = 0
        if fire:
            pass
        
        #moving the collision rectangle/player accordingly
        
        self.rect.x += self.playerXVelocity
        self.collide(self.playerXVelocity,0,platforms, self.camera,healthBar)
        
        self.rect.y += self.playerYVelocity
        self.onGround = False;
        self.collide(0,self.playerYVelocity,platforms, self.camera,healthBar)
        
        AnimatePlayer.blit(self)
        
        
    def collide(self, xvel, yvel, platforms, cam,healthBar):
        self.plat = platforms
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0: #right collide
                    self.rect.right = p.rect.left # sets player's right position = to the platforms
                    self.playerXVelocity = 0
                if xvel < 0: #left collide
                    self.rect.left = p.rect.right
                    self.playerXVelocity = 0
                if yvel > 0: #bottom collide/on the ground
                    self.rect.bottom = p.rect.top
                    self.onGround = True #as long as this is true the player ain't fallin'
                    self.playerYVelocity = 0
                if yvel < 0: #top collide
                    self.rect.top = p.rect.bottom
                    self.playerYVelocity = 0
        if abs (cam.levelRect.x - (halfWidth-self.rect.x)) >500:
            self.rect.left = abs(cam.levelRect.x)
            self.playerXVelocity = 0

            #if collision with enem

        for enem in self.enem:
            if pygame.sprite.collide_rect(self, enem):
                self.hit == True
                cooldown = 1000
                now = pygame.time.get_ticks()
                if now - self.ticks >= cooldown:
                    healthBar.subtractAmt(20)
                    self.hurt_sound.play()
                    self.ticks = now
                    print("hit and cooldown") #So we don't get hit like 60 times a tick when in a monster
                    self.hit == False
                    if healthBar.getAmt() <= 0:
                        self.death_sound.play()
                        pygame.mixer.music.load('gameSounds/deadmusic.wav')
                        pygame.mixer.music.play(-1)
                        
                        
                    
                    
    def fireLaser(self):
        if self.direction == "right":
            laser = Laser(self.rect.x + 64 , self.rect.y + 25, 32, direction, self.ent, self.enem, self.plat, self)
        else:
            laser = Laser(self.rect.x -64, self.rect.y + 25, 32, direction, self.ent, self.enem, self.plat, self)
        entities.add(laser)
        
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False) #flips the player sprite
    def getPos(self):
        return (self.x, self.y)
class Enemy(Entity,AnimateEnemy):
    def __init__(self, x, y, platforms):
        Entity.__init__(self)
        self.yVel = 0 # y velocity is 0 as we are placed on ground
        self.xVel = randrange(2, 8) # start moving immediately
        self.x = x # x postion
        self.y = y # y position
        self.platforms = platforms
        self.image = pygame.Surface((128,128), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()  
        #self.rect = Rect(0,0,x,y) 
        self.rect = Rect(self.x, self.y, 50, 90) # place at location
        self.onGround = False # Set onGround to false so our update can work
        self.onScreen = False
        AnimateEnemy.__init__(self,self.image)
    def update(self):
        if(self.onScreen):
            if not self.onGround:
                self.yVel += 0.3 # if not onGround, increment down till on ground
    
            self.rect.left += self.xVel # increment in x direction
            self.collide(self.xVel, 0, self.platforms) # do x-axis collisions
            self.rect.top += self.yVel # increment in y direction
            self.onGround = False; # assuming we're in the air
            self.collide(0, self.yVel, self.platforms) # do y-axis collisions
        else:
            self.onScreen = True
            self.xVel *= -1
        if self.xVel >= 1:
            AnimateEnemy.moveR(self)
        if self.xVel < 1:
            AnimateEnemy.moveL(self)
        AnimateEnemy.blit(self)
    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                    #self.yVel = -10
                if xVel < 0:
                    self.rect.left = p.rect.right
                    #self.xVel *= -1 # hit wall, so change direction
                    self.yVel = -12
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom
                    self.yVel *= -1
            
    def setEnemyOnScreen(self):
        self.onScreen = True
    def setEnemyOffScreen(self):
        self.onScreen = False
class Laser(Entity, AnimateLaser):
    def __init__(self,x,y,size,direction,entities,enemies,platforms, player):
        Entity.__init__(self)
        self.velocity = 0
        self.direction = direction
        self.xSize = 60
        self.ySize = 36
        self.ent = entities
        self.enem = enemies
        self.player = player
        self.plat = platforms
        self.image = pygame.Surface((self.xSize,self.ySize), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()  
        self.rect = Rect(x,y,self.xSize,self.ySize)
        AnimateLaser.__init__(self,self.image)
        self.disentegration = pygame.mixer.Sound('gameSounds/disentegration.wav')
        
        if direction == "right":
            AnimateLaser.moveR(self)
        else:
            AnimateLaser.moveL(self)
        
    def update(self):
        global score
        self.velocity = -25 if self.direction == "left" else 25
        self.rect.x += self.velocity #+ (player.playerXVelocity if self.direction == direction else -1*player.playerXVelocity)
        # for each enemies, if the laser collides, remove the enemies and laser
        for enem in self.enem:
            if pygame.sprite.collide_rect(self, enem):
                entities.remove(enem)
                self.enem.remove(enem)
                entities.remove(self)
                self.disentegration.play()
                score +=1
                print(score)
        # for each platform, if the laser collides, remove the laser
        for p in self.plat:
            if pygame.sprite.collide_rect(self, p):
                entities.remove(self)
        AnimateLaser.blit(self)
class LaserGun(Entity,AnimateGun):
    def __init__(self, x, y, w, h):
        Entity.__init__(self)
        self.rect = Rect(x,y,w,h)
        self.image = pygame.Surface((w,h), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha() 
        AnimateGun.__init__(self,self.image)
    def update(self,obj):
        if obj.direction == "right":
            AnimateGun.moveR(self)
        else:
            AnimateGun.moveL(self)
        self.rect.x = obj.rect.x
        self.rect.y = obj.rect.y
        AnimateGun.blit(self)
class Platform(Entity):
    def __init__(self, x, y,size,img):
        Entity.__init__(self)
        self.size = size
        self.drawn = False
        self.x = x
        self.y = y
        self.imgFile = img
        self.image = pygame.image.load(self.imgFile).convert_alpha()        
        self.rect = Rect(self.x, self.y, self.size, self.size)        
    def getPos(self):
        return (self.x,self.y)
    def update(self):
        pass
class Background(Entity):
    def __init__(self, x, y,width, height,speed,file):
        Entity.__init__(self)
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.rect2 = Rect(self.width, self.y, self.width, self.height)
    def update(self,surf,obj, cam):
        self.backXVel = -obj.playerXVelocity//self.speed
        self.backYVel = -obj.playerYVelocity/5
        
        if(self.rect.x <= -self.width):
            self.rect.left = self.rect2.right
        if(self.rect2.x <= -self.width):
            self.rect2.left = self.rect.right
        if halfWidth-obj.rect.x == cam.levelRect.x:
            self.rect.x += self.backXVel
            self.rect2.x += self.backXVel
        if not obj.rect.y>=200:
            self.rect.y += self.backYVel
            self.rect2.y += self.backYVel
    
        surf.blit(self.image, self.rect)
        surf.blit(self.image, self.rect2)

class UserInterface(Entity):
    def __init__(self, x, y, w, h,scaleFact, surface, fileName):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.scale = scaleFact
        self.rect = Rect(x,y,w,h)
        if fileName != None:
            self.image = pygame.image.load(fileName).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width*self.scale,self.height*self.scale))
        self.surf = surface
    def update(self):
        self.surf.blit(self.image, self.rect)
class UIbar(UserInterface):
    def __init__(self,surface, fileName, col, regen,iPos):
        #UserInterface.__init__(self, x, y, w, h,scaleFact, surface, fileName)
        self.GREY = (95, 95, 95)
        self.pixel = displayHeight//100
        self.rectLength = int(displayHeight/3.25)
        self.iconPos = iPos
        self.regen = regen
        self.color = col
        self.surf = surface
        self.HP = 100
        self.rect = Rect((self.iconPos + 8*self.pixel, 7*self.pixel), (int(self.rectLength * (self.HP/100)), 3*self.pixel))
        self.image = Surface((self.rect.w,self.rect.h))
        self.image.fill(self.color)
        
              
    def update(self):
        if self.regen and self.HP < 100:
            self.HP += .2
        self.image = pygame.transform.scale(self.image, (int(self.rectLength * (self.HP/100)),(3*self.pixel)))
        
        self.underColor = (self.color[0]//3, self.color[1]//3, self.color[2]//3)
        xOffset = self.iconPos + 6*self.pixel  
        yOffset = 6*self.pixel
        pygame.draw.rect(self.surf, self.GREY, Rect((xOffset + self.pixel, yOffset), (self.rectLength + 2*self.pixel, 5*self.pixel))) #taller health rect
        pygame.draw.rect(self.surf, self.GREY, Rect((xOffset, yOffset + self.pixel), (self.rectLength + 4*self.pixel, 3*self.pixel))) #longer health rect
        pygame.draw.rect(self.surf, self.underColor, Rect((xOffset + 2*self.pixel, yOffset + self.pixel), (self.rectLength, 3*self.pixel))) #inside health rect
    
               
        UserInterface.update(self)
        self.surf.blit(self.image, self.rect)
    def addAmt(self, amt):
        if amt + self.HP >= 100:
            self.HP = 100
        else:
            self.HP += amt
    def subtractAmt(self, amt):
        if self.HP - amt <= 0:
            self.HP = 0
        else:
            self.HP -= amt
    def getAmt(self):
        return self.HP
    
if __name__ == '__main__': main()    
