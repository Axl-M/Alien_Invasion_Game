import sys
import pygame

def run_game():
    # инициализирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # основной цикл игры
    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # отображение оследнего прорисованного экрана
        pygame.display.flip()

run_game()

