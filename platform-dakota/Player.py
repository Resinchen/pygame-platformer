from Constants import PLAYER_SIZE, MOVE_SPEED, GRAVITY, JUMP_POWER, ANIMATION_DELAY, BACKGROUND_COLOR, \
                      PLAYER_STAY,PLAYER_LEFT_1, PLAYER_LEFT_2,\
                      PLAYER_RIGHT_1, PLAYER_RIGHT_2,\
                      PLAYER_UP_L, PLAYER_UP_R

from pygame import Surface, Color, mixer
from pygame.sprite import Sprite, collide_rect

from Platform import Platform, Right_Platform, Null_Platform

from Bonus import Bonus

import pyganim

# Настройка звука Игрока
mixer.pre_init(44100, -16, 1, 512)
mixer.init()

# Анимации
ANIMATION_STAY = [PLAYER_STAY]

ANIMATION_RIGHT = [PLAYER_RIGHT_1,
                   PLAYER_RIGHT_2]

ANIMATION_LEFT = [PLAYER_LEFT_1,
                  PLAYER_LEFT_2]

ANIMATION_UP_L = [PLAYER_UP_L]

ANIMATION_UP_R = [PLAYER_UP_R]


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface(PLAYER_SIZE)
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = make_boltAnim(ANIMATION_STAY, ANIMATION_DELAY)
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimUpL = make_boltAnim(ANIMATION_UP_L, ANIMATION_DELAY)
        self.boltAnimUpL.play()

        self.boltAnimUpR = make_boltAnim(ANIMATION_UP_R, ANIMATION_DELAY)
        self.boltAnimUpR.play()
        self.jump_sound = mixer.Sound('sounds/jump.ogg')
        self.point_sound = mixer.Sound('sounds/point.ogg')


    def update(self, left, right, up, platforms, tg):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))

        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(BACKGROUND_COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if up and right:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.jump_sound.play()
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimUpR.blit(self.image, (0, 0))

        if up and left:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.jump_sound.play()
            self.image.fill(Color(BACKGROUND_COLOR))
            self.boltAnimUpL.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, tg)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, tg)

    def collide(self, xvel, yvel, platforms, tg):
        for pl in platforms:
            if collide_rect(self, pl):
                if type(pl) == Platform or type(pl) == Null_Platform:
                    if xvel > 0:
                        self.rect.right = pl.rect.left
                    if xvel < 0:
                        self.rect.left = pl.rect.right
                    if yvel > 0:
                        self.rect.bottom = pl.rect.top
                        self.onGround = True
                    if yvel < 0:
                        self.rect.top = pl.rect.bottom
                        self.yvel = 0
                elif type(pl) == Right_Platform:
                    if xvel > 0:
                        self.rect.right = pl.rect.left
                elif type(pl) == Bonus:
                    if not tg.is_Has:
                        self.bonus_up(tg)
                        pl.kill()

    def bonus_up(self, tg):
        tg.is_Has = True
        self.point_sound.play()
