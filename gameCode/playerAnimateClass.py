#test anims

import pygame
from pygame.locals import *
import sys
import pyganim

pygame.init()


# set up the window



class AnimatePlayer(object):
    def __init__(self, Surface):
        # create the animation objects   ('filename of image',    duration_in_seconds)
        self.right_Anim = pyganim.PygAnimation([('playerAnimations/chrono_proto_run_right_000.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_right_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_right_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_right_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_right_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_right_005.gif', 0.1),])

        self.left_Anim = pyganim.PygAnimation([('playerAnimations/chrono_proto_run_left_000.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_left_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_left_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_left_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_left_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_run_left_005.gif', 0.1),])

        self.right_idleAnim = pyganim.PygAnimation([('playerAnimations/chrono_proto_id_right_000.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_005.gif', 0.1)])

        self.left_idleAnim = pyganim.PygAnimation([('playerAnimations/chrono_proto_id_left_000.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_left_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_left_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_left_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_left_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_left_005.gif', 0.1)])

        self.right_jumpAnim = pyganim.PygAnimation([('playerAnimations/chrono_proto_jump_right_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_005.gif', 0.1),
                                         ('playerAnimations/chrono_proto_id_right_006.gif', 0.1)])

        self.left_jumpAnim = pyganim.PygAnimation([('playerAnimations/chrono_proto_jump_left_001.gif', 0.1),
                                         ('playerAnimations/chrono_proto_jump_left_002.gif', 0.1),
                                         ('playerAnimations/chrono_proto_jump_left_003.gif', 0.1),
                                         ('playerAnimations/chrono_proto_jump_left_004.gif', 0.1),
                                         ('playerAnimations/chrono_proto_jump_left_005.gif', 0.1),
                                         ('playerAnimations/chrono_proto_jump_left_006.gif', 0.1)])
        

        self.right_Anim.stop()
        self.right_idleAnim.play()# there is also a pause() and stop() method
        self.left_Anim.stop()
        self.left_idleAnim.stop()
        self.left_jumpAnim.stop()
        self.right_jumpAnim.stop()

        self.SURFACE = Surface
        self.RIGHT = 'right'
        self.LEFT = 'left'

    def moveR(self):
        self.right_Anim.play()
        self.right_idleAnim.stop()
        self.left_Anim.stop()
        self.left_idleAnim.stop()
        self.right_jumpAnim.stop()
        self.left_jumpAnim.stop()

    def moveL(self):
        self.left_Anim.play()
        self.right_idleAnim.stop()
        self.right_Anim.stop()
        self.left_idleAnim.stop()
        self.right_jumpAnim.stop()
        self.left_jumpAnim.stop()
    def stopForJump(self):
        self.left_Anim.stop()
        self.right_idleAnim.stop()
        self.right_Anim.stop()
        self.left_idleAnim.stop()
    def idleR(self):
        self.right_Anim.stop()
        self.right_idleAnim.play()
        self.left_Anim.stop()
        self.left_idleAnim.stop()
    def idleL(self):
        self.right_Anim.stop()
        self.right_idleAnim.stop()
        self.left_Anim.stop()
        self.left_idleAnim.play()
    def blit(self):
        self.SURFACE.fill((0,0,0,0))
        self.right_Anim.blit(self.SURFACE, (0, 0))
        self.right_idleAnim.blit(self.SURFACE, (0, 0))
        self.left_Anim.blit(self.SURFACE, (0, 0))
        self.left_idleAnim.blit(self.SURFACE, (0,0))
        self.left_jumpAnim.blit(self.SURFACE, (0, 0))
        self.right_jumpAnim.blit(self.SURFACE, (0, 0))
        
class AnimateGun(object):
    def __init__(self, Surface):
        self.right_gun = pyganim.PygAnimation([('playerAnimations/chrono_gun_right_001.gif', 0.1),
                                          ('playerAnimations/chrono_gun_right_002.gif', 0.1)])
        
        self.left_gun =  pyganim.PygAnimation([('playerAnimations/chrono_gun_left_001.gif', 0.1),
                                          ('playerAnimations/chrono_gun_left_002.gif', 0.1)])
        self.SURFACE = Surface
        self.right_gun.stop()
        self.left_gun.stop()
    def moveR(self):
        self.right_gun.play()
        self.left_gun.stop()
    def moveL(self):
        self.right_gun.stop()
        self.left_gun.play()   
    def blit(self):
        self.SURFACE.fill((0,0,0,0))
        self.right_gun.blit(self.SURFACE, (0, 0))
        self.left_gun.blit(self.SURFACE, (0, 0))
       
class AnimateLaser(AnimateGun):
    def __init__(self, Surface):
        self.right_gun = pyganim.PygAnimation([('playerAnimations/chrono_laser_right_001.gif', 0.1)])
               
        self.left_gun =  pyganim.PygAnimation([('playerAnimations/chrono_laser_left_001.gif', 0.1),])
        self.SURFACE = Surface
        self.right_gun.stop()
        self.left_gun.stop()        
    def moveR(self):
        AnimateGun.moveR(self)
    def moveL(self):
        AnimateGun.moveL(self)
    def blit(self):
        AnimateGun.blit(self)

class AnimateEnemy(AnimatePlayer):
    def __init__(self, Surface):
        AnimatePlayer.__init__(self, Surface)
    def moveR(self):
        AnimatePlayer.moveR(self)
    def moveL(self):
        AnimatePlayer.moveL(self)
    def stopForJump(self):
        AnimatePlayer.stopForJump(self)
    def idleR(self):
        AnimatePlayer.idleR(self)
    def idleL(self):
        AnimatePlayer.idleL(self)
    def blit(self):
        AnimatePlayer.blit(self)