import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Класс для управления пулями выпущенными кораблем """
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()  # для правильной реализации наследования от Sprite.
        # super().__init__()  # в Python3 можно так
        self.screen = screen

        # создание пули в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Перемещает пулю по экрану """
        self.y -= self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """ Вывод пули на экран """
        pygame.draw.rect(self.screen, self.color, self.rect)
