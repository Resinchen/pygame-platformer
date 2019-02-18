from Constants import DISPLAY, PLATFORM_SIZE, BACKGROUND_COLOR, LEVEL_1, WINDOW

from Platform import Platform, Right_Platform, Lava_Platform

from Player import Player

from Bonus import Bonus

from Camera import Camera

from Menu import Menu

from Target import Target

from pygame import display, Surface, init, sprite, mixer, time, font, Rect,\
                   Color, event, QUIT, KEYDOWN, KEYUP,\
                   K_UP, K_RIGHT, K_ESCAPE, K_LEFT

init()  # Инициализация pygame
window = display.set_mode(WINDOW)  # Создание окна
display.set_caption("Dakota`s run")  # Название окна
screen = Surface(DISPLAY)  # Создание видимой поверхности

# Строка состояния
info_string = Surface((640, 30))

#  Шрифты
font.init()
inf_font = font.Font(None, 32)


# Создание героя
hero = Player(320, 1320)
left = right = up = False

# Создание уровня
with open(LEVEL_1, 'r') as level1:
	level_mas = level1.read().split('\n')

sprite_group = sprite.Group()
sprite_group.add(hero)
platforms = []

x = 0
y = 0
for row in level_mas:
    for col in row:
        if col == "1":
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        if col == "r":
            pl = Right_Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        if col == "l":
            pl = Lava_Platform(x, y)
            sprite_group.add(pl)
        if col == "b":
            pl = Bonus(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        if col == "t":
            target = Target(x, y-167)
            sprite_group.add(target)
        x += PLATFORM_SIZE
    y += PLATFORM_SIZE
    x = 0

# Настройка звука
mixer.pre_init(44100, -16, 1, 512)
mixer.init()
sound = mixer.Sound('sounds/back.ogg')
sound.play(-1)

# Главный цикл
main_loop = True
timer = time.Clock()

# Создаем меню

clauses = [(270, 210, u'Game', (250, 250, 30), (250, 30, 250), 0),
           (270, 280, u'Quit', (250, 250, 30), (250, 30, 250), 1)]

game = Menu(clauses)
game.menu(window, screen, info_string)

# Камера


def camera_func(camera, target_rect):

    l = -target_rect.x + DISPLAY[0]/2
    t = -target_rect.y + DISPLAY[1]/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - DISPLAY[0]), l)
    t = max(-(camera.height - DISPLAY[1]), t)
    t = min(0, t)

    return Rect(l, t, w, h)

total_level_width = len(level_mas[0]) * 40
total_level_height = len(level_mas) * 40

camera = Camera(camera_func, total_level_width, total_level_height)

TEXT = "Голос: Найди его"


while main_loop:
    for e in event.get():  # Обработка событий
        if e.type == QUIT:  # Событие выхода
            main_loop = False

        if e.type == KEYDOWN:  # Событие нажатия клавиши
            if e.key == K_ESCAPE:  # Выход с клавиатуры
                game.menu(window, screen, info_string)
            if e.key == K_LEFT:  # Движение влево
                left = True
            if e.key == K_RIGHT:  # Движение вправо
                right = True
            if e.key == K_UP:  # Движение вверх
                up = True

        if e.type == KEYUP:  # Событие отжатия клавиши
            if e.key == K_LEFT:  # Движение влево
                left = False
            if e.key == K_RIGHT:  # Движение вправо
                right = False
            if e.key == K_UP:  # Движение вверх
                up = False

    screen.fill(Color(BACKGROUND_COLOR))  # Заливка видимой поверхности
    info_string.fill(Color("#000000"))

    target.update(hero)
    if target.is_Has and not target.is_Give:
        TEXT = "Голос: Принеси его мне"
    if target.is_Give and target.is_Has:
        TEXT = "Сонч: Спасибочки!!!!"
    if target.is_Fall and not target.is_Has:
        TEXT = "Сонч: Ты не принесла его((("

    hero.update(left, right, up, platforms, target)

    camera.update(hero)
    for s in sprite_group:
        screen.blit(s.image, camera.apply(s))

    info_string.blit(inf_font.render(TEXT, 1, (255, 255, 255)), (40, 5))

    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 30))
    display.flip()  # Обновление всего на экране
    timer.tick(60)
