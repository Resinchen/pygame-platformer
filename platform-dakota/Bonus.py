from pygame.sprite import Sprite
from pygame.image import load

from Constants import BONUS_IMAGE


class Bonus(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load(BONUS_IMAGE)  # Текстура платформы
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

