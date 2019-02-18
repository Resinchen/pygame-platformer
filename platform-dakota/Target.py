from pygame.sprite import Sprite, collide_rect
from pygame.surface import Surface
from pygame import Color

from Constants import  TARGET_STAY, TARGET_CALLING_1, TARGET_CALLING_2, \
    TARGET_JUMP_1, TARGET_JUMP_2, TARGET_JUMP_3, BACKGROUND_COLOR, ANIMATION_DELAY

import pyganim

ANIMATION_STAY = [TARGET_STAY]

ANIMATION_CALL = [TARGET_CALLING_1, TARGET_CALLING_2]

ANIMATION_JUMP = [TARGET_JUMP_1, TARGET_JUMP_2, TARGET_JUMP_3]


class Target(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((73, 211))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.set_colorkey(Color(BACKGROUND_COLOR))
        self.is_Give = False
        self.is_Has = False
        self.is_Fall = False

        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = make_boltAnim(ANIMATION_STAY, ANIMATION_DELAY)
        self.boltAnimStay.play()

        self.boltAnimCall = make_boltAnim(ANIMATION_CALL, ANIMATION_DELAY * 3)
        self.boltAnimCall.play()

        self.boltAnimJump = make_boltAnim(ANIMATION_JUMP, ANIMATION_DELAY * 3)
        self.boltAnimJump.play()

    def update(self, player):
        if not self.is_Give and not self.is_Has:
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

        if self.is_Has and not self.is_Give:
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimCall.blit(self.image, (0, 0))

        if self.is_Give and self.is_Has:
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        self.collide(player)

    def collide(self, player):
        if collide_rect(self, player):
            if self.is_Has:
                self.is_Give = True
            self.is_Fall = True
