import sys
import pygame


def check_events(ship):
    """ обрабатывает нажатия клавишь и события мыши """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # переместить корабль вправо
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            # ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """ обновляет изображения на экране и отображает новый экран """
    # при каждом проходе цикла перерисовать экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # отображение оследнего прорисованного экрана
    pygame.display.flip()