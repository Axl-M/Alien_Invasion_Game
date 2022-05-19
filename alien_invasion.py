"""
Главный файл программы создает ряд важных объектов, используемых в ходе игры
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from button import Button


def run_game():
    # инициализирует pygame, settings и  объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    # создание корабля
    ship = Ship(ai_settings, screen)
    # создание группы для хранения пуль
    bullets = Group()
    # создание пришельца
    aliens = Group()  # группа для хранения всех пришельцев в игре

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # основной цикл игры
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)  # проверяет ввод, полученный от игрока
        if stats.game_active:
            ship.update()                           # обновляет позицию корабля
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)       # обновляет позиции всех выпущенных пуль
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)   # обновление флота пришельцев

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)  # вывод нового экрана


run_game()
