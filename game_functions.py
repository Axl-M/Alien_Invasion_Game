"""
Содержит набор функций, выполняющих основную работу в игре
"""
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """ Обрабатывает нажатия клавиш и события мыши """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ Запускает новую игру при нажатии кнопки Play. """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: # чтобы НЕ реагировала на нажатие на невидимую кнопку PLAY
        # скрыть указатель мыши
        pygame.mouse.set_visible(False)
        # сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True

        # очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
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

    # Кнопка Play отображается в том случае, если игра неактивна.
    if not stats.game_active:
        play_button.draw_button()

    # отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ Обновляет позиции пуль и удаляет старые пули """
    # обновление позиций пуль
    bullets.update()  # вызывает bullet.update() для каждой пули, включенной в группу bullets.

    # удаление пуль вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """ Обработка коллизий пуль и пришельцев """
    # Проверка попаданий в пришельцев
    # при обнаружении попадания удалить пулю и пришельца
    # Метод sprite.groupcollide() сравнивает прямоугольник rect каждой пули с прямоугольником rect каждого
    # пришельца и возвращает словарь с пулями и пришельцами, между которыми обнаружены коллизии.
    # Каждый ключ в словаре представляет пулю, а ассоциированное с ним значение — пришельца, в которого попала пуля.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Сначала перебирает все пули в группе bullets, а затем перебирает всех пришельцев в группе aliens.
    # Каждый раз, когда между прямоугольником пули и пришельца обнаруживается перекрытие, groupcollide()
    # добавляет пару «ключ — значение» в возвращаемый словарь. Два аргумента True сообщают Pygame, нужно ли
    # удалять столкнувшиеся объекты: пулю и пришельца. (Чтобы создать сверхмощную пулю, которая будет
    # уничтожать всех пришельцев на своем пути, можно передать в первом аргументе False, а во втором True.
    # Пришельцы, в которых попадает пуля, будут исчезать, но все пули будут оставаться активными до верхнего
    # края экрана.)

    if len(aliens) == 0:    # группа пуста - все корабли уничтожены
        # уничтожение существующих пуль и создание нового флота
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Создание флота пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # создание пришельца и размещения его в ряду
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    # ширина экрана за минусом ширины двух кораблей (отступы от краев)
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # К-во кораблей в ряду (двойное значение ширины т.к. расстояние между кораблями = ширине корабля
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
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
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране."""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ Проверяет, достиг ли флот края экрана, после чего
    обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # проверка коллизии "корабль - пришелец"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Проверка пришельцев, добравшихся до нижнего края экрана.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """ Реагирует на достижение пришельцем края экрана """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ Опускает весь флот и меняет направление движения флота. """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Обрабатывает столкновение корабля с пришельцем. """
    if stats.ships_left > 0:
        # Уменьшение ships_left.
        stats.ships_left -= 1
        # print('ships_left - ', stats.ships_left )
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Очистка списков пришельцев и пуль.
    aliens.empty()
    bullets.empty()

    # Создание нового флота и размещение корабля в центре.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # пауза
    sleep(0.5)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ Проверяет, добрались ли пришельцы до нижнего края экрана. """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что при столкновении с кораблем.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
