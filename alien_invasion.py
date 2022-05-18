"""
Главный файл программы создает ряд важных объектов, используемых в ходе игры
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # инициализирует pygame, settings и  объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # создание корабля
    ship = Ship(ai_settings, screen)
    # создание группы для хранения пуль
    bullets = Group()
    # создание приешльца
    aliens = Group()  # группа для хранения всех пришельцев в игре

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # основной цикл игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # проверяет ввод, полученный от игрока
        ship.update()                   # обновляет позицию корабля
        gf.update_bullets(bullets)      # обновляет позиции всех выпущенных пуль
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)    # вывод нового экрана


run_game()
