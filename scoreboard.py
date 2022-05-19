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
        #  Подготовка исходного изображения.
        self.prep_score()

    def prep_score(self):
        """ Преобразует текущий счет в графическое изображение. """
        rounded_score = round(self.stats.score, -1)   # -1 округлить до десятков
        # score_str = str(self.stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Вывод счета в правой верхней части экрана. И расширяется влево с ростом значения и ширины числа
        self.score_rect = self.score_img.get_rect()
        # смещаем его правую сторону на 20 пикселов от правого края экрана
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ Выводит счет на экран. """
        self.screen.blit(self.score_img, self.score_rect)
