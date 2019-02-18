from Constants import PLATFORM_IMAGE, LAVA_IMAGE

from pygame.sprite import Sprite
from pygame.image import load


class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load(PLATFORM_IMAGE)  # Текстура платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Right_Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load(PLATFORM_IMAGE)  # Текстура платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Lava_Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load(LAVA_IMAGE)  # Текстура платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Null_Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load(PLATFORM_IMAGE)  # Текстура платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
