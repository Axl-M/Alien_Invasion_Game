import pygame.font


class Scoreboard:
    """ Класс для вывода игровой информации. """
    def __init__(self, ai_settings, screen, stats):
        """ Инициализирует атрибуты подсчета очков. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Настройки шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #   Подготовка изображений счетов.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """ Преобразует текущий счет в графическое изображение. """
        rounded_score = round(self.stats.score, -1)   # -1 округлить до десятков
        # score_str = str(self.stats.score)
        score_str = "{:,}".format(rounded_score)      # форматировать разряды запятыми
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Вывод счета в правой верхней части экрана. И расширяется влево с ростом значения и ширины числа
        self.score_rect = self.score_img.get_rect()
        # смещаем его правую сторону на 20 пикселов от правого края экрана
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """ Преобразует рекордный счет в графическое изображение. """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # горизонтальное вы- равнивание прямоугольника по центру экрана
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """ Выводит счет на экран. """
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
