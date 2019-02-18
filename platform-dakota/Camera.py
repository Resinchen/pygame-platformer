from pygame import Rect


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def apply(self, target):
        return target.rect.move(self.state.topleft)
