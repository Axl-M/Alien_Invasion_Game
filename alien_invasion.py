import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # инициализирует pygame, settings и  объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # создание корабля
    ship = Ship(screen)

    # цвет фона
    bg_color = (230, 230, 230)


    # основной цикл игры
    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # при каждом проходе цикла перерисовать экран
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # отображение оследнего прорисованного экрана
        pygame.display.flip()

run_game()

