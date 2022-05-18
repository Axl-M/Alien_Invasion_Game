import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Класс представляющий одного пришельца """
    def __init__(self, ai_settings, screen):
        """ Инициализирует пришельца и задает его начальную позицию. """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения пришельца и назначение атрбута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        # Изначально каждый пришелец размещается в левом верхнем углу экрана,
        # при этом слева от него добавляется интервал, равный ширине пришельца,
        # а над ним — интервал, равный высоте
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)