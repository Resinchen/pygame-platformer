import sys
from pygame import font, Color, event, QUIT, KEYDOWN, K_ESCAPE, display, mouse, K_DOWN, K_UP, MOUSEBUTTONDOWN, K_RETURN

from Constants import BACKGROUND_COLOR


class Menu:
    def __init__(self, clauses = [120, 140, u'Clause', (250, 250, 30), (250, 30, 250), 0]):
        self.clauses = clauses

    def render(self, surface, font, number):
        for clause in self.clauses:
            if number == clause[5]:
                surface.blit(font.render(clause[2], 1, clause[4]), (clause[0], clause[1]-30))
            else:
                surface.blit(font.render(clause[2], 1, clause[3]), (clause[0], clause[1]-30))

    def menu(self, window, screen, info_string):
        done = True
        font_menu = font.Font(None, 50)
        punkt = 0
        while done:
            info_string.fill(Color(BACKGROUND_COLOR))
            screen.fill(Color(BACKGROUND_COLOR))

            mp = mouse.get_pos()
            for clause in self.clauses:
                if mp[0] > clause[0] and mp[0] < clause[0] + 155 and mp[1] > clause[1] and mp[1] < clause[1] + 50:
                    punkt = clause[5]
            self.render(screen, font_menu, punkt)

            for e in event.get():  # Обработка событий
                if e.type == QUIT:  # Событие выхода
                    sys.exit()

                if e.type == KEYDOWN:  # Событие нажатия клавиши
                    if e.key == K_ESCAPE:  # Выход с клавиатуры
                        sys.exit()
                    if e.key == K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == K_DOWN:
                        if punkt < len(self.clauses) - 1:
                            punkt += 1
                    if e.key == K_RETURN:
                        if punkt == 0:
                            done = False
                        elif punkt == 1:
                            sys.exit()

                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))
            display.flip()
