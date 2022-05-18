"""
Содержит набор функций, выполняющих основную работу в игре
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Реагирует на нажатие клавиш """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Выпускает пулю если максимум еще не достигнут  """
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bulets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ Реагирует на отпускание клавиш """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Обрабатывает нажатия клавиш и события мыши """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Обновляет изображения на экране и отображает новый экран """
    # при каждом проходе цикла перерисовать экран
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Когда вы вызываете метод draw() для группы, Pygame автоматически выводит каждый элемент группы в
    # позиции, определяемой его атрибутом rect. В данном случае вызов aliens.draw(screen) рисует каждого п
    # пришельца в группе на экране.
    aliens.draw(screen)

    # отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets):
    """ Обновляет позиции пуль и удаляет старые пули """
    # обновление позиций пуль
    bullets.update()  # вызывает bullet.update() для каждой пули, включенной в группу bullets.

    # удаление пуль вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        # создание пришельца и размещения его в ряду
        create_alien(ai_settings, screen, aliens, alien_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    # ширина экрана за минусом ширины двух кораблей (отступы от краев)
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # К-во кораблей в ряду (двойное значение ширины т.к. расстояние между кораблями = ширине корабля
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """Создает пришельца и размещает его в ряду."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    # Интервал между соседними пришельцами равен одной ширине пришельца.
    alien = Alien(ai_settings, screen)  # Этот пришелец не войдет во флот, поэтому он не включается в группу aliens.
    alien_width = alien.rect.width      # определяется ширина пришельца
    # Каждый пришелец сдвигается вправо на одну ширину от левого поля. Затем ширина пришельца умножается на 2,
    # чтобы учесть полное пространство, выделенное для одного пришельца, включая пустой интервал справа, а
    # полученная величина умножается на позицию пришельца в ряду.
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
